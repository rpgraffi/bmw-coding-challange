import json
from typing import List
from models.sushi_model import Position, BusinessHours, Reviews, ContactInfo, PriceSummary

def _load_sushi_data():
    with open('data/sushi.json') as file:
        return json.load(file)
    

def get_all_sushi_restaurants_names() -> List[dict]:
    sushi_data = _load_sushi_data()
    return [{"restaurants": restaurant['title']} for restaurant in sushi_data]

def get_position(title: str) -> Position:
    sushi_data = _load_sushi_data()
    for restaurant in sushi_data:
        if restaurant['title'] == title:
            return Position(**restaurant['position'])
    return None

def get_business_hours(title: str) -> BusinessHours:
    sushi_data = _load_sushi_data()
    for restaurant in sushi_data:
        if restaurant['title'] == title:
            return BusinessHours(**restaurant['businessHours'])
    return None

def get_reviews(title: str) -> Reviews:
    sushi_data = _load_sushi_data()
    for restaurant in sushi_data:
        if restaurant['title'] == title:
            # Some restaurants might not have reviews
            if 'reviews' in restaurant:
                return Reviews(**restaurant['reviews'])
    return None

def get_contact_info(title: str) -> ContactInfo:
    sushi_data = _load_sushi_data()
    for restaurant in sushi_data:
        if restaurant['title'] == title:
            return ContactInfo(**restaurant['contactInfo'])
    return None

def get_price(title: str) -> PriceSummary:
    sushi_data = _load_sushi_data()
    for restaurant in sushi_data:
        if restaurant['title'] == title:
            return PriceSummary(**restaurant['priceSummary'])
    return None
