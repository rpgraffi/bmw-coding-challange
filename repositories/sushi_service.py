import json
from typing import List, Optional
from pathlib import Path

from models.sushi_model import (
    SushiRestaurant, Position, BusinessHours, Reviews,
    ContactInfo, PriceSummary
)

class SushiService:
    def __init__(self):
        self._restaurants = self._load_sushi_data()

    def _load_sushi_data(self) -> List[SushiRestaurant]:
        """Load sushi data with proper model validation"""
        json_path = Path("data/sushi.json")
        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)
        return [SushiRestaurant(**restaurant) for restaurant in data]

    def get_all_sushi_restaurants_names(self) -> List[str]:
        """Returns all restaurant names"""
        return [restaurant.title for restaurant in self._restaurants]

    def get_position(self, title: str) -> Optional[Position]:
        """Returns the position of a specific restaurant"""
        for restaurant in self._restaurants:
            if restaurant.title == title:
                return restaurant.position
        return None

    def get_business_hours(self, title: str) -> Optional[BusinessHours]:
        """Returns the business hours of a specific restaurant"""
        for restaurant in self._restaurants:
            if restaurant.title == title:
                return restaurant.businessHours
        return None

    def get_reviews(self, title: str) -> Optional[Reviews]:
        """Returns the reviews of a specific restaurant"""
        for restaurant in self._restaurants:
            if restaurant.title == title:
                return restaurant.reviews
        return None

    def get_contact_info(self, title: str) -> Optional[ContactInfo]:
        """Returns the contact information of a specific restaurant"""
        for restaurant in self._restaurants:
            if restaurant.title == title:
                return restaurant.contactInfo
        return None

    def get_price_summary(self, title: str) -> Optional[PriceSummary]:
        """Returns the price summary of a specific restaurant"""
        for restaurant in self._restaurants:
            if restaurant.title == title:
                return restaurant.priceSummary
        return None
