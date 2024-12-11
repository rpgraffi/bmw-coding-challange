import json
from typing import List, Optional, TypeVar, Callable
from pathlib import Path

from src.models.domain.sushi_model import (
    SushiData, SushiRestaurant, Position, BusinessHours, Reviews,
    ContactInfo, PriceSummary, DistanceInfo
)
from src.const.constants import SUSHI_PATH

T = TypeVar('T')

class SushiDataProvider:
    def __init__(self):
        self._restaurants = self._load_sushi_data()

    def _load_sushi_data(self) -> List[SushiRestaurant]:
        """Load sushi data with proper model validation"""
        json_path = Path(SUSHI_PATH)
        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)
        return [SushiRestaurant(**restaurant) for restaurant in data]

    def _get_data_for_restaurants(self, 
                                title: Optional[str], 
                                data_getter: Callable[[SushiRestaurant], T]
                                ) -> List[SushiData[T]]:
        """Generic helper method to get data from restaurants"""
        if title is None:
            return [SushiData(title=restaurant.title, data=data_getter(restaurant)) 
                   for restaurant in self._restaurants]
        return [SushiData(title=restaurant.title, data=data_getter(restaurant)) 
                for restaurant in self._restaurants if restaurant.title == title]

    def get_all_sushi_restaurants_names(self) -> List[str]:
        """Returns all restaurant names"""
        return [restaurant.title for restaurant in self._restaurants]

    def get_position(self, title: Optional[str] = None) -> List[SushiData[Position]]:
        """Returns the position of restaurants"""
        return self._get_data_for_restaurants(title, lambda r: r.position)

    def get_distance_info(self, title: Optional[str] = None) -> List[SushiData[DistanceInfo]]:
        """Returns the distance information of restaurants"""
        return self._get_data_for_restaurants(
            title,
            lambda r: DistanceInfo(
                distance_from_current_location=r.distance_from_current_location,
                duration_from_current_location=r.duration_from_current_location
            )
        )

    def get_business_hours(self, title: Optional[str] = None) -> List[SushiData[BusinessHours]]:
        """Returns the business hours of restaurants"""
        return self._get_data_for_restaurants(title, lambda r: r.businessHours)

    def get_reviews(self, title: Optional[str] = None) -> List[SushiData[Reviews]]:
        """Returns the reviews of restaurants"""
        return self._get_data_for_restaurants(title, lambda r: r.reviews)

    def get_contact_info(self, title: Optional[str] = None) -> List[SushiData[ContactInfo]]:
        """Returns the contact information of restaurants"""
        return self._get_data_for_restaurants(title, lambda r: r.contactInfo)

    def get_price_summary(self, title: Optional[str] = None) -> List[SushiData[PriceSummary]]:
        """Returns the price summary of restaurants"""
        return self._get_data_for_restaurants(title, lambda r: r.priceSummary)
    
    def get_sushi_restaurants(self, title: Optional[str] = None) -> List[SushiRestaurant]:
        """Returns the sushi restaurants"""
        return self._get_data_for_restaurants(title, lambda r: r)
