import json
from typing import List, Optional, Tuple, Callable, TypeVar
from pathlib import Path

from src.models.domain.parking_model import (
    ParkingSpot, Position, BusinessHours, ContactInfo,
    PriceSummary, ParkingInfo, PriceStructured, ParkingData
)
from src.const.constants import PARKING_PATH

T = TypeVar('T')

class ParkingDataProvider:
    def __init__(self):
        self._parking_spots = self._load_parking_data()

    def _load_parking_data(self) -> List[ParkingSpot]:
        """Load parking data with proper model validation"""
        json_path = Path(PARKING_PATH)
        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)
        return [ParkingSpot(**spot) for spot in data]


    def _get_data_for_spots(self, 
                           title: Optional[str], 
                           data_getter: Callable[[ParkingSpot], T]
                           ) -> List[ParkingData[T]]:
        """Generic helper method to get data from parking spots"""
        if title is None:
            return [ParkingData(title=spot.title, data=data_getter(spot)) 
                   for spot in self._parking_spots]
        return [ParkingData(title=spot.title, data=data_getter(spot)) 
                for spot in self._parking_spots if spot.title == title]
        
        
    def get_all_parking_spots_names(self) -> List[str]:
        """Returns all parking spot names"""
        return [spot.title for spot in self._parking_spots]

    def get_position(self, title: str) -> Optional[Position]:
        """Returns the position of a specific parking spot"""
        for spot in self._parking_spots:
            if spot.title == title:
                return spot.position
        return None


    def get_business_hours(self, title: Optional[str] = None) -> List[ParkingData[BusinessHours]]:
        """Returns business hours for all spots or a specific parking spot if title is provided"""
        return self._get_data_for_spots(title, lambda spot: spot.businessHours)

    def get_contact_info(self, title: Optional[str] = None) -> List[ParkingData[ContactInfo]]:
        """Returns contact info for all spots or a specific parking spot if title is provided"""
        return self._get_data_for_spots(title, lambda spot: spot.contactInfo)

    def get_price_summary(self, title: Optional[str] = None) -> List[ParkingData[PriceSummary]]:
        """Returns price summary for all spots or a specific parking spot if title is provided"""
        return self._get_data_for_spots(title, lambda spot: spot.priceSummary)

    def get_parking_info(self, title: Optional[str] = None) -> List[ParkingData[ParkingInfo]]:
        """Returns parking info for all spots or a specific parking spot if title is provided"""
        return self._get_data_for_spots(title, lambda spot: spot.parking)

    def get_payment_methods(self, title: Optional[str] = None) -> List[ParkingData[List[str]]]:
        """Returns payment methods for all spots or a specific parking spot if title is provided"""
        return self._get_data_for_spots(title, lambda spot: spot.paymentMethods)

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

    def get_spots_near_location(self) -> List[Tuple[str, Position, str]]:
        """Returns titles, positions and distances of spots near a location"""
        return [(spot.title, spot.position, spot.distance_from_current_location) 
                for spot in self._parking_spots 
                if spot.distance_from_current_location]
