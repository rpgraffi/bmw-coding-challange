

from pydantic import BaseModel, Field
from enums.user_interest_enum import UserInterestEnum


class UserInterest(BaseModel):
    interest: UserInterestEnum = Field(..., description="Get the user's interest, Sushi, Parking or Chatting")
    assistant_message: str = Field(..., description="Subtle reassurance message to user about selected interest")


