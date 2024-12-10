from typing import List
from enums.user_interest_enum import UserInterestEnum
from models.intent.parking_intent import UserParkingIntent
from models.intent.sushi_intent import UserSushiIntent



def get_user_interest(user_interest: UserInterestEnum) -> List[dict]:
    if user_interest == UserInterestEnum.SUSHI:
        return UserSushiIntent
    elif user_interest == UserInterestEnum.PARKING:
        return UserParkingIntent
    else:
        return UserParkingIntent + UserSushiIntent



