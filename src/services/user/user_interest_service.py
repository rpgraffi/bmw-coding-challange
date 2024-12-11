from src.enums.user_interest_enum import UserInterestEnum
from src.models.intent.assistant_model import AssistantModel
from src.models.intent.parking_intent import UserParkingIntent
from src.models.intent.sushi_intent import UserSushiIntent
from src.services.intent.parking_intent_service import ParkingIntentService
from src.services.intent.sushi_intent_service import SushiIntentService


def get_user_interest(user_interest: UserInterestEnum):
    if user_interest == UserInterestEnum.SUSHI:
        return UserSushiIntent, SushiIntentService()
    elif user_interest == UserInterestEnum.PARKING:
        return UserParkingIntent, ParkingIntentService()
    elif user_interest == UserInterestEnum.ASSISTANT:
        return AssistantModel, None
    # else:
    #     return UserParkingIntent + UserSushiIntent, ParkingIntentService + SushiIntentService



