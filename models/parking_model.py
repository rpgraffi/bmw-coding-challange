from typing import List, Optional
from pydantic import BaseModel


class Position(BaseModel):
    lat: float
    lng: float

class BusinessHours(BaseModel):
    formattedHours: List[str]
    nextStatusChange: str
    currentStatus: str

class ContactInfo(BaseModel):
    phoneNumber: str

class PriceSummary(BaseModel):
    priceSummaryText: str
    free: bool

class ListPrice(BaseModel):
    service: str
    price: str

class PriceStructured(BaseModel):
    listPrices: List[ListPrice]

class ParkingDimensionRestriction(BaseModel):
    height: float
    width: Optional[float] = None

class ParkingInfo(BaseModel):
    spotsNumber: int
    freeSpotsNumber: Optional[int] = None
    disabledSpotsNumber: Optional[int] = None
    parkingDimensionRestriction: ParkingDimensionRestriction
    services: Optional[List[str]] = None
    types: List[str]
    operator: str

class ParkingSpot(BaseModel):
    title: str
    position: Position
    distance_from_current_location: str
    duration_from_current_location: Optional[str] = None
    address: str
    categories: List[str]
    businessHours: BusinessHours
    contactInfo: ContactInfo
    paymentMethods: List[str]
    priceSummary: PriceSummary
    priceStructured: PriceStructured
    parking: ParkingInfo
    availability: Optional[str] = None
