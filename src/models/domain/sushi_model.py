from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')
class SushiData(BaseModel, Generic[T]):
    title: str
    data: T

class Position(BaseModel):
    lat: float
    lng: float

class BusinessHours(BaseModel):
    formattedHours: List[str]
    nextStatusChange: str
    currentStatus: str

class Reviews(BaseModel):
    averageRating: Optional[float] = None
    reviewCount: Optional[int] = None

class ContactInfo(BaseModel):
    phoneNumber: str

class PriceSummary(BaseModel):
    priceRangeLevel: Optional[str] = None
    free: bool

class SushiRestaurant(BaseModel):
    title: str
    position: Position
    distance_from_current_location: str
    duration_from_current_location: Optional[str] = None
    address: str
    categories: List[str]
    businessHours: Optional[BusinessHours] = None
    reviews: Optional[Reviews] = None
    foodTypes: List[str]
    contactInfo: ContactInfo
    priceSummary: PriceSummary
