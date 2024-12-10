import json
from typing import List, Optional, Tuple
from pathlib import Path

from models.parking_model import (
    ParkingSpot, Position, BusinessHours, ContactInfo,
    PriceSummary, ParkingInfo, PriceStructured
)

class ParkingService:
    def __init__(self):
        self._parking_spots = self._load_parking_data()

    def _load_parking_data(self) -> List[ParkingSpot]:
        """Load parking data with proper model validation"""
        json_path = Path("data/parking.json")
        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)
        return [ParkingSpot(**spot) for spot in data]

    def get_all_parking_spots_names(self) -> List[str]:
        """Returns all parking spot names"""
        return [spot.title for spot in self._parking_spots]

    def get_position(self, title: str) -> Optional[Position]:
        """Returns the position of a specific parking spot"""
        for spot in self._parking_spots:
            if spot.title == title:
                return spot.position
        return None

    def get_business_hours(self, title: str) -> Optional[BusinessHours]:
        """Returns the business hours of a specific parking spot"""
        for spot in self._parking_spots:
            if spot.title == title:
                return spot.businessHours
        return None

    def get_contact_info(self, title: str) -> Optional[ContactInfo]:
        """Returns the contact information of a specific parking spot"""
        for spot in self._parking_spots:
            if spot.title == title:
                return spot.contactInfo
        return None

    def get_price_summary(self, title: str) -> Optional[PriceSummary]:
        """Returns the price summary of a specific parking spot"""
        for spot in self._parking_spots:
            if spot.title == title:
                return spot.priceSummary
        return None

    def get_parking_info(self, title: str) -> Optional[ParkingInfo]:
        """Returns the parking information of a specific parking spot"""
        for spot in self._parking_spots:
            if spot.title == title:
                return spot.parking
        return None

    def get_payment_methods(self, title: str) -> List[str]:
        """Returns the available payment methods for a specific parking spot"""
        for spot in self._parking_spots:
            if spot.title == title:
                return spot.paymentMethods
        return []

    def get_available_spots(self) -> List[Tuple[str, ParkingInfo]]:
        """Returns titles and parking info of spots that have free spaces"""
        available_spots = []
        for spot in self._parking_spots:
            if (hasattr(spot.parking, 'freeSpotsNumber') and 
                spot.parking.freeSpotsNumber is not None and 
                spot.parking.freeSpotsNumber > 0):
                available_spots.append((spot.title, spot.parking))
        return available_spots

    def find_spots_by_height(self, min_height: float) -> List[Tuple[str, ParkingInfo]]:
        """Returns titles and parking info of spots that can accommodate vehicles of specified height"""
        suitable_spots = []
        for spot in self._parking_spots:
            if spot.parking.parkingDimensionRestriction.height >= min_height:
                suitable_spots.append((spot.title, spot.parking))
        return suitable_spots

    def get_cheapest_spots(self, hours: int = 2) -> Tuple[str, PriceSummary, PriceStructured]:
        """Returns title and price information of cheapest spot"""
        def get_hourly_rate(spot: ParkingSpot) -> float:
            for price in spot.priceStructured.listPrices:
                if "hour" in price.price.lower():
                    try:
                        price_str = price.price.split('€')[0].split(':')[-1].strip()
                        return float(price_str)
                    except (ValueError, IndexError):
                        continue
            return float('inf')
        
        sorted_spots = sorted(self._parking_spots, key=get_hourly_rate)
        if not sorted_spots:
            return None
        
        spot = sorted_spots[0]
        return (spot.title, spot.priceSummary, spot.priceStructured)

    def find_spots_with_disabled_access(self) -> List[Tuple[str, ParkingInfo]]:
        """Returns titles and parking info of spots that have disabled parking spaces"""
        disabled_spots = []
        for spot in self._parking_spots:
            if ((spot.parking.services and 'DISABLED' in spot.parking.services) or
                (spot.parking.disabledSpotsNumber and spot.parking.disabledSpotsNumber > 0)):
                disabled_spots.append((spot.title, spot.parking))
        return disabled_spots

    def get_spots_near_location(self, location: str) -> List[Tuple[str, Position, str]]:
        """Returns titles, positions and distances of spots near a location"""
        # In a real application, this would use geocoding and actual distance calculation
        return [(spot.title, spot.position, spot.distance_from_current_location) 
                for spot in self._parking_spots 
                if spot.distance_from_current_location]
