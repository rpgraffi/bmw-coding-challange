from pydantic import BaseModel
from typing import Any, Dict

from models.intent.sushi_intent import UserSushiIntent
from repositories.sushi_service import SushiService
from services.intent_service import IntentService
class SushiResponse(BaseModel):
    data: Dict[str, Any]

class SushiIntentService(IntentService):
    def __init__(self):
        self.sushi_service = SushiService()

    def handle_intent(self, intent: UserSushiIntent) -> Dict[str, Any]:
        """
        Orchestrates data retrieval based on user intent
        Returns aggregated data from all relevant queries
        """
        data = {}
        
        # Basic restaurant info if specific restaurant is mentioned
        if intent.specific_restaurant_name:
            data["restaurant_info"] = self.sushi_service.get_position(intent.specific_restaurant_name)
        
        # Handle each query type
        if "list_all" in intent.query_types:
            data["all_restaurants"] = self.sushi_service.get_all_sushi_restaurants_names()
            
        if "reviews" in intent.query_types:
            if intent.specific_restaurant_name:
                data["reviews"] = self.sushi_service.get_reviews(intent.specific_restaurant_name)
            
        if "business_hours" in intent.query_types:
            if intent.specific_restaurant_name:
                data["hours"] = self.sushi_service.get_business_hours(intent.specific_restaurant_name)
                
        if "price_check" in intent.query_types:
            if intent.specific_restaurant_name:
                data["price"] = self.sushi_service.get_price_summary(intent.specific_restaurant_name)
                
        if "contact" in intent.query_types:
            if intent.specific_restaurant_name:
                data["contact"] = self.sushi_service.get_contact_info(intent.specific_restaurant_name)
                
        if "nearby" in intent.query_types:
            if intent.location:
                data["nearby"] = self.sushi_service.get_position(intent.location)

        return SushiResponse(data=data)
