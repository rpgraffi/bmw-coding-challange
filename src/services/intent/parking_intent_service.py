from typing import Any, Dict
from pydantic import BaseModel

from services.core.intent_service import IntentService
from data_providers.parking_data_provider import ParkingDataProvider
from models.intent.parking_intent import UserParkingIntent

class ParkingResponse(BaseModel):
    data: Dict[str, Any]

class ParkingIntentService(IntentService):
    def __init__(self):
        self.data_provider = ParkingDataProvider()

    def handle_intent(self, intent: UserParkingIntent) -> Dict[str, Any]:
        """
        Orchestrates database queries based on user intent
        Returns aggregated data from all relevant queries
        """
        data = {}
            
        if "list_all" in intent.query_types:
            data["all_spots"] = self.data_provider.get_all_parking_spots_names()
            
        if "cheapest" in intent.query_types:
            data["cheapest"] = self.data_provider.get_cheapest_spots(
                hours=intent.duration_hours or 2
            )
            
        if "height_check" in intent.query_types:
            if intent.height_requirement:
                data["height_suitable"] = self.data_provider.find_spots_by_height(
                    intent.height_requirement
                )
                
        if "availability" in intent.query_types:
            data["available"] = self.data_provider.get_available_spots()
            
        if "accessibility" in intent.query_types:
            data["disabled_access"] = self.data_provider.find_spots_with_disabled_access()
            
        if "nearby" in intent.query_types:
            data["nearby"] = self.data_provider.get_spots_near_location()
        
        
        # Handle specific parking spot
        spot_name = None
        if intent.specific_spot_name:
            spot_name = intent.specific_spot_name
          
        if intent.response_detail == "detailed":
            data["parking_info"] = self.data_provider.get_parking_info(intent.specific_spot_name)
            
        if "business_hours" in intent.query_types:
            data["hours"] = self.data_provider.get_business_hours(spot_name)
            
        if "payment_info" in intent.query_types:
            data["payment_methods"] = self.data_provider.get_payment_methods(spot_name)
            
        if "price_check" in intent.query_types:
            data["price"] = self.data_provider.get_price_summary(spot_name)
            
        if "contact" in intent.query_types:
            data["contact"] = self.data_provider.get_contact_info(spot_name)


        return ParkingResponse(data=data)