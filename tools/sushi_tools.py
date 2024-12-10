from typing import Dict, List
from tools.base_tools import BaseTools
from services.sushi_service import get_all_sushi_restaurants_names, get_position, get_business_hours, get_reviews, get_contact_info, get_price

class SushiTools(BaseTools):
    @property
    def tools(self) -> List[Dict]:
        return sushi_tools
    
    @property
    def function_mapping(self) -> Dict:
        return {
            "get_all_sushi_restaurants_names": get_all_sushi_restaurants_names,
            "get_position": get_position,
            "get_business_hours": get_business_hours,
            "get_reviews": get_reviews,
            "get_contact_info": get_contact_info,
            "get_price": get_price,
        }
        
        
sushi_tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_sushi_restaurants",
                    "description": "Get sushi restaurants in Munich",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "The title of the sushi restaurant, e.g. Sasou"
                            },
                            "assistant_message": {
                                "type": "string",
                                "description": "Friendly message to display to user"
                            }
                        },
                        "required": ["title", "assistant_message"],
                        "additionalProperties": False
                    }
                }
            }
        ]