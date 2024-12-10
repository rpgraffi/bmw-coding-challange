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
        
        