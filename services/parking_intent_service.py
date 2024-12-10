from typing import Any, Dict, List
from models.parking_model import ParkingSpot
from tools.parking_tools import UserParkingIntent
from services.parking_service import ParkingService

class ParkingIntentService:
    def __init__(self):
        self.parking_service = ParkingService()

    def handle_intent(self, intent: UserParkingIntent) -> Dict[str, Any]:
        """
        Orchestrates database queries based on user intent
        Returns data and recommendation based on the intent
        """
        handlers = {
            "list_all": self._handle_list_all,
            "specific_spot": self._handle_specific_spot,
            "cheapest": self._handle_cheapest,
            "nearby": self._handle_nearby,
            "availability": self._handle_availability,
            "accessibility": self._handle_accessibility,
            "height_check": self._handle_height_check,
            "business_hours": self._handle_business_hours,
            "payment_info": self._handle_payment_info,
            "price_check": self._handle_price_check,
            "contact": self._handle_contact,
            "detailed_info": self._handle_detailed_info
        }
        
        handler = handlers.get(intent.query_type)
        if not handler:
            raise ValueError(f"Unknown query type: {intent.query_type}")
            
        return handler(intent)

    def _handle_list_all(self, intent: UserParkingIntent) -> Dict[str, Any]:
        spots = self.parking_service.get_all_parking_spots_names()
        return {
            "data": spots,
            "recommendation": f"There are {len(spots)} parking spots available in Munich: {', '.join(spots)}"
        }

    def _handle_cheapest(self, intent: UserParkingIntent) -> Dict[str, Any]:
        hours = intent.duration_hours or 2
        spots = self.parking_service.get_cheapest_spots(hours=hours)
        spot_name, price_summary, _ = spots  # Assuming this returns a tuple as in original service
        
        return {
            "data": {
                "spot": spot_name,
                "price": price_summary.priceSummaryText
            },
            "recommendation": (
                f"The cheapest parking for {hours} hours is {spot_name} "
                f"at {price_summary.priceSummaryText}"
            )
        }

    def _handle_height_check(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.height_requirement:
            return {"error": "Height requirement not specified"}
            
        spots = self.parking_service.find_spots_by_height(intent.height_requirement)
        suitable_spots = [name for name, _ in spots]  # Unpack tuples
        
        location_context = f" near {intent.location}" if intent.location else ""
        return {
            "data": suitable_spots,
            "recommendation": (
                f"Found {len(suitable_spots)} parking spots{location_context} that can fit "
                f"vehicles up to {intent.height_requirement}m tall: {', '.join(suitable_spots)}"
            )
        }

    def _handle_specific_spot(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.specific_spot_name:
            return {"error": "Parking spot name not specified"}
            
        spot_info = self.parking_service.get_parking_info(intent.specific_spot_name)
        if not spot_info:
            return {"error": f"Parking spot '{intent.specific_spot_name}' not found"}
            
        return {
            "data": spot_info,
            "recommendation": (
                f"{intent.specific_spot_name} has {spot_info.spotsNumber} total spots"
                f"{f', with {spot_info.freeSpotsNumber} currently available' if spot_info.freeSpotsNumber else ''}"
            )
        }

    def _handle_availability(self, intent: UserParkingIntent) -> Dict[str, Any]:
        available = self.parking_service.get_available_spots()
        spots_info = [f"{name} ({info.freeSpotsNumber} spots)" for name, info in available]
        
        return {
            "data": available,
            "recommendation": (
                f"Currently available parking spots: {', '.join(spots_info)}"
                if spots_info else "No parking spots with available spaces found"
            )
        }

    def _handle_accessibility(self, intent: UserParkingIntent) -> Dict[str, Any]:
        spots = self.parking_service.find_spots_with_disabled_access()
        accessible_spots = [
            f"{name} ({info.disabledSpotsNumber} disabled spots)" 
            for name, info in spots
        ]
        
        return {
            "data": spots,
            "recommendation": (
                f"Parking spots with disabled access: {', '.join(accessible_spots)}"
                if accessible_spots else "No parking spots with disabled access found"
            )
        }

    def _handle_business_hours(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.specific_spot_name:
            return {"error": "Parking spot name not specified"}
            
        hours = self.parking_service.get_business_hours(intent.specific_spot_name)
        return {
            "data": hours,
            "recommendation": (
                f"{intent.specific_spot_name} hours: {hours.formattedHours[0]}. "
                f"Current status: {hours.currentStatus}"
            )
        }
        
    def _handle_nearby(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.location:
            return {"error": "Location not specified"}
            
        spots = self.parking_service.get_spots_near_location(intent.location)
        nearby_spots = [
            f"{name} ({distance})" 
            for name, _, distance in spots
        ]
        
        return {
            "data": spots,
            "recommendation": (
                f"Found {len(nearby_spots)} parking spots near {intent.location}: "
                f"{', '.join(nearby_spots)}"
            )
        }

    def _handle_payment_info(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.specific_spot_name:
            return {"error": "Parking spot name not specified"}
            
        methods = self.parking_service.get_payment_methods(intent.specific_spot_name)
        readable_methods = [method.replace('_', ' ').title() for method in methods]
        
        return {
            "data": methods,
            "recommendation": (
                f"{intent.specific_spot_name} accepts the following payment methods: "
                f"{', '.join(readable_methods)}"
            )
        }

    def _handle_price_check(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.specific_spot_name:
            return {"error": "Parking spot name not specified"}
            
        price_summary = self.parking_service.get_price_summary(intent.specific_spot_name)
        if not price_summary:
            return {"error": f"No price information found for {intent.specific_spot_name}"}
            
        return {
            "data": price_summary,
            "recommendation": (
                f"Parking at {intent.specific_spot_name} costs "
                f"{price_summary.priceSummaryText}"
                f"{' (Free parking)' if price_summary.free else ''}"
            )
        }

    def _handle_contact(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.specific_spot_name:
            return {"error": "Parking spot name not specified"}
            
        contact = self.parking_service.get_contact_info(intent.specific_spot_name)
        if not contact:
            return {"error": f"No contact information found for {intent.specific_spot_name}"}
            
        return {
            "data": contact,
            "recommendation": (
                f"You can contact {intent.specific_spot_name} at: "
                f"{contact.phoneNumber}"
            )
        }

    def _handle_detailed_info(self, intent: UserParkingIntent) -> Dict[str, Any]:
        if not intent.specific_spot_name:
            return {"error": "Parking spot name not specified"}
            
        spot_info = self.parking_service.get_parking_info(intent.specific_spot_name)
        hours = self.parking_service.get_business_hours(intent.specific_spot_name)
        price = self.parking_service.get_price_summary(intent.specific_spot_name)
        
        if not spot_info:
            return {"error": f"No information found for {intent.specific_spot_name}"}
            
        details = []
        details.append(f"Total spots: {spot_info.spotsNumber}")
        if spot_info.freeSpotsNumber is not None:
            details.append(f"Available spots: {spot_info.freeSpotsNumber}")
        if spot_info.disabledSpotsNumber:
            details.append(f"Disabled spots: {spot_info.disabledSpotsNumber}")
        details.append(f"Max height: {spot_info.parkingDimensionRestriction.height}m")
        if hours:
            details.append(f"Hours: {hours.formattedHours[0]}")
        if price:
            details.append(f"Price: {price.priceSummaryText}")
        
        return {
            "data": {
                "parking_info": spot_info,
                "business_hours": hours,
                "price_summary": price
            },
            "recommendation": (
                f"Detailed information for {intent.specific_spot_name}:\n"
                f"{' | '.join(details)}"
            )
        }


# Usage example:
"""
# Initialize service
intent_service = ParkingIntentService()

# Handle user query
intent = UserParkingIntent(
    query_type="cheapest",
    duration_hours=3,
    response_detail="brief"
)

result = intent_service.handle_intent(intent)
print(result["recommendation"])  # Natural language response
print(result["data"])           # Structured data for further processing
""" 