

from pydantic import BaseModel, Field

from src.enums.user_interest_enum import UserInterestEnum


class UserInterestIntent(BaseModel):
    interest: UserInterestEnum = Field(..., description="""Get the user's interest, Sushi, Parking, or Chatting.
    If already answered just use chatting.                                     
    If already selected, remain in context unless it is somewhere clear that the user has a different interest.""")


