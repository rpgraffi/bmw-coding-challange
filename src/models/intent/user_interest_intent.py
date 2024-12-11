

from pydantic import BaseModel, Field

from enums.user_interest_enum import UserInterestEnum


class UserInterestIntent(BaseModel):
    interest: UserInterestEnum = Field(..., description="Get the user's interest, Sushi, Parking, or Chatting. If already selected, remain in context unless it is obvious that the user has a different interest.")
    assistant_message: str = Field(..., description="Subtle reassurance message to user about selected interest")


