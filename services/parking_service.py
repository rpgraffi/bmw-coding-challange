import json
from typing import List, Optional
from models.parking_model import (
    ParkingSpot, Position, BusinessHours, ContactInfo,
    PriceSummary, ParkingInfo, PriceStructured
)

def _load_parking_data() -> List[dict]:
    with open('data/parking.json') as file:
        return json.load(file)

def get_all_parking_spots_names() -> List[dict]:
    """Returns all parking spot names"""
    parking_data = _load_parking_data()
    return [{"parking": spot['title']} for spot in parking_data]

def get_position(title: str) -> Optional[Position]:
    """Returns the position of a specific parking spot"""
    parking_data = _load_parking_data()
    for spot in parking_data:
        if spot['title'] == title:
            return Position(**spot['position'])
    return None

def get_business_hours(title: str) -> Optional[BusinessHours]:
    """Returns the business hours of a specific parking spot"""
    parking_data = _load_parking_data()
    for spot in parking_data:
        if spot['title'] == title:
            return BusinessHours(**spot['businessHours'])
    return None

def get_contact_info(title: str) -> Optional[ContactInfo]:
    """Returns the contact information of a specific parking spot"""
    parking_data = _load_parking_data()
    for spot in parking_data:
        if spot['title'] == title:
            return ContactInfo(**spot['contactInfo'])
    return None

def get_price_summary(title: str) -> Optional[PriceSummary]:
    """Returns the price summary of a specific parking spot"""
    parking_data = _load_parking_data()
    for spot in parking_data:
        if spot['title'] == title:
            return PriceSummary(**spot['priceSummary'])
    return None

def get_parking_info(title: str) -> Optional[ParkingInfo]:
    """Returns the parking information (spots, restrictions, etc.) of a specific parking spot"""
    parking_data = _load_parking_data()
    for spot in parking_data:
        if spot['title'] == title:
            return ParkingInfo(**spot['parking'])
    return None

def get_payment_methods(title: str) -> List[str]:
    """Returns the available payment methods for a specific parking spot"""
    parking_data = _load_parking_data()
    for spot in parking_data:
        if spot['title'] == title:
            return spot['paymentMethods']
    return []

def get_available_spots() -> List[tuple[str, ParkingInfo]]:
    """Returns titles and parking info of spots that have free spaces"""
    parking_data = _load_parking_data()
    available_spots = []
    
    for spot in parking_data:
        parking_info = ParkingInfo(**spot['parking'])
        if (hasattr(parking_info, 'freeSpotsNumber') and 
            parking_info.freeSpotsNumber is not None and 
            parking_info.freeSpotsNumber > 0):
            available_spots.append((spot['title'], parking_info))
    
    return available_spots

def find_spots_by_height(min_height: float) -> List[tuple[str, ParkingInfo]]:
    """Returns titles and parking info of spots that can accommodate vehicles of specified height"""
    parking_data = _load_parking_data()
    suitable_spots = []
    
    for spot in parking_data:
        parking_info = ParkingInfo(**spot['parking'])
        if parking_info.parkingDimensionRestriction.height >= min_height:
            suitable_spots.append((spot['title'], parking_info))
    
    return suitable_spots

def get_cheapest_spots(hours: int = 2) -> List[tuple[str, PriceSummary, PriceStructured]]:
    """Returns titles and price information of spots sorted by hourly rate"""
    parking_data = _load_parking_data()
    price_info = []
    
    def get_hourly_rate(spot_data: tuple) -> float:
        _, _, price_structured = spot_data
        for price in price_structured.listPrices:
            if "hour" in price.price.lower():
                try:
                    price_str = price.price.split('€')[0].split(':')[-1].strip()
                    return float(price_str)
                except (ValueError, IndexError):
                    continue
        return float('inf')
    
    for spot in parking_data:
        price_summary = PriceSummary(**spot['priceSummary'])
        price_structured = PriceStructured(**spot['priceStructured'])
        price_info.append((spot['title'], price_summary, price_structured))
    
    return sorted(price_info, key=get_hourly_rate)

def find_spots_with_disabled_access() -> List[tuple[str, ParkingInfo]]:
    """Returns titles and parking info of spots that have disabled parking spaces"""
    parking_data = _load_parking_data()
    disabled_spots = []
    
    for spot in parking_data:
        parking_info = ParkingInfo(**spot['parking'])
        if ((parking_info.services and 'DISABLED' in parking_info.services) or
            (parking_info.disabledSpotsNumber and parking_info.disabledSpotsNumber > 0)):
            disabled_spots.append((spot['title'], parking_info))
    
    return disabled_spots
