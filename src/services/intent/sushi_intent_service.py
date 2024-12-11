from pydantic import BaseModel
from typing import Any, Dict

from src.services.core.intent_service import IntentService
from src.data_providers import SushiDataProvider
from src.models.intent.sushi_intent import UserSushiIntent

class SushiResponse(BaseModel):
    data: Dict[str, Any]

class SushiIntentService(IntentService):
    def __init__(self):
        self.data_provider = SushiDataProvider()

    def handle_intent(self, intent: UserSushiIntent) -> Dict[str, Any]:
        """
        Orchestrates data retrieval based on user intent
        Returns aggregated data from all relevant queries
        """
        data = {}
        
        spot_name = intent.specific_restaurant_name
        
        if "list_all" in intent.query_types:
            data["all_restaurants"] = self.data_provider.get_all_sushi_restaurants_names()
            
        if "reviews" in intent.query_types:
            data["reviews"] = self.data_provider.get_reviews(spot_name)
            
        if "business_hours" in intent.query_types:
            data["hours"] = self.data_provider.get_business_hours(spot_name)
                
        if "price_check" in intent.query_types:
            data["price"] = self.data_provider.get_price_summary(spot_name)
                
        if "contact" in intent.query_types:
            data["contact"] = self.data_provider.get_contact_info(spot_name)
                
        if "nearby" in intent.query_types:
            data["nearby"] = self.data_provider.get_position(spot_name)
            
        if intent.response_detail == "detailed":
            data["restaurants"] = self.data_provider.get_sushi_restaurants(spot_name)

        return SushiResponse(data=data)
