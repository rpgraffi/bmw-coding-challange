from pydantic import BaseModel, Field
from typing import List, Optional
from enums.user_interest_enum import UserInterestEnum

class UserInterestResponse(BaseModel):
    assistant_message: str
    interest: UserInterestEnum = Field(..., description="The user's interest")

class ParkingSpotResponse(BaseModel):
    name: str
    price_summary: str
    hourly_rates: List[dict]

class SushiRestaurantResponse(BaseModel):
    name: str
    rating: float
    location: str 