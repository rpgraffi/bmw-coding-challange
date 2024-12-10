from typing import List
from enums.user_interest_enum import UserInterestEnum
from models.intent.assistant_model import AssistantModel
from models.intent.parking_intent import UserParkingIntent
from models.intent.sushi_intent import UserSushiIntent
from services.parking_intent_service import ParkingIntentService
from services.sushi_intent_service import SushiIntentService



def get_user_interest(user_interest: UserInterestEnum):
    if user_interest == UserInterestEnum.SUSHI:
        return UserSushiIntent, SushiIntentService()
    elif user_interest == UserInterestEnum.PARKING:
        return UserParkingIntent, ParkingIntentService()
    elif user_interest == UserInterestEnum.ASSISTANT:
        return AssistantModel
    # else:
    #     return UserParkingIntent + UserSushiIntent, ParkingIntentService + SushiIntentService



