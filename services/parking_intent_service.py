from typing import Any, Dict
from pydantic import BaseModel

from models.intent.parking_intent import UserParkingIntent
from repositories.parking_service import ParkingService
from services.intent_service import IntentService

class ParkingResponse(BaseModel):
    data: Dict[str, Any]

class ParkingIntentService(IntentService):
    def __init__(self):
        self.parking_service = ParkingService()

    def handle_intent(self, intent: UserParkingIntent) -> Dict[str, Any]:
        """
        Orchestrates database queries based on user intent
        Returns aggregated data from all relevant queries
        """
        data = {}
        
        # Basic spot info if specific spot is mentioned
        if intent.specific_spot_name:
            data["parking_info"] = self.parking_service.get_parking_info(intent.specific_spot_name)
        
        # Handle each query type
        if "list_all" in intent.query_types:
            data["all_spots"] = self.parking_service.get_all_parking_spots_names()
            
        if "cheapest" in intent.query_types:
            data["cheapest"] = self.parking_service.get_cheapest_spots(
                hours=intent.duration_hours or 2
            )
            
            
        if "height_check" in intent.query_types:
            if intent.height_requirement:
                data["height_suitable"] = self.parking_service.find_spots_by_height(
                    intent.height_requirement
                )
                
        if "availability" in intent.query_types:
            data["available"] = self.parking_service.get_available_spots()
            
        if "accessibility" in intent.query_types:
            data["disabled_access"] = self.parking_service.find_spots_with_disabled_access()
            
        if "nearby" in intent.query_types:
            if intent.location:
                data["nearby"] = self.parking_service.get_spots_near_location(intent.location)
        
        spot_name = None
        if intent.specific_spot_name:
            spot_name = intent.specific_spot_name
            
        if "business_hours" in intent.query_types:
            data["hours"] = self.parking_service.get_business_hours(spot_name)
            
        if "payment_info" in intent.query_types:
            data["payment_methods"] = self.parking_service.get_payment_methods(spot_name)
            
        if "price_check" in intent.query_types:
            data["price"] = self.parking_service.get_price_summary(spot_name)
            
        if "contact" in intent.query_types:
            data["contact"] = self.parking_service.get_contact_info(spot_name)
            
        if "detailed_info" in intent.query_types:
            # Aggregate all available information
            data.update({
                "parking_info": self.parking_service.get_parking_info(spot_name),
                "hours": self.parking_service.get_business_hours(spot_name),
                "price": self.parking_service.get_price_summary(spot_name),
                "contact": self.parking_service.get_contact_info(spot_name),
                "payment_methods": self.parking_service.get_payment_methods(spot_name),
                "position": self.parking_service.get_position(spot_name)
            })


        return ParkingResponse(data=data)