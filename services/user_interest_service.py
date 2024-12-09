from typing import List
from enums.user_interest_enum import UserInterest

from services.sushi_service import get_all_sushi_restaurants_names  
from services.parking_service import get_all_parking_spots_names

def get_user_interest(user_interest: str) -> List[dict]:
    user_interest = user_interest.upper()
    if user_interest == "SUSHI":
        return get_all_sushi_restaurants_names()
    elif user_interest == "PARKING":
        return get_all_parking_spots_names()
    else:
        return get_all_sushi_restaurants_names() + get_all_parking_spots_names()
    
    



