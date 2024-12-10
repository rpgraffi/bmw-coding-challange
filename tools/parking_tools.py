from typing import Dict, List
from tools.base_tools import BaseTools
from services.parking_service import (
    get_all_parking_spots_names, get_position,
    get_business_hours, get_contact_info, get_price_summary,
    get_parking_info, get_payment_methods, get_available_spots,
    find_spots_by_height, get_cheapest_spots, find_spots_with_disabled_access
)

class ParkingTools(BaseTools):
    @property
    def tools(self) -> List[Dict]:
        return parking_tools
    
    @property
    def function_mapping(self) -> Dict:
        return {
            "get_all_parking_spots_names": get_all_parking_spots_names,
            "get_position": get_position,
            "get_business_hours": get_business_hours,
            "get_contact_info": get_contact_info,
            "get_price_summary": get_price_summary,
            "get_parking_info": get_parking_info,
            "get_payment_methods": get_payment_methods,
            "get_available_spots": get_available_spots,
            "find_spots_by_height": find_spots_by_height,
            "get_cheapest_spots": get_cheapest_spots,
            "find_spots_with_disabled_access": find_spots_with_disabled_access,
        }





parking_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_parking_spots",
            "description": "Get parking spots in Munich",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the parking spot",
                    },
                    "assistant_message": {
                        "type": "string",
                        "description": "Friendly message to display to user"
                    }
                },
                "required": ["title", "assistant_message"],
                "additionalProperties": False,
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_all_parking_spots_names",
            "description": "Returns all parking spot names in Munich",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_position",
            "description": "Get the position (coordinates) of a specific parking spot",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the parking spot"
                    }
                },
                "required": ["title"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_business_hours",
            "description": "Get the business hours of a specific parking spot",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the parking spot"
                    }
                },
                "required": ["title"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_contact_info",
            "description": "Get the contact information of a specific parking spot",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the parking spot"
                    }
                },
                "required": ["title"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_price_summary",
            "description": "Get the price summary of a specific parking spot",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the parking spot"
                    }
                },
                "required": ["title"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_parking_info",
            "description": "Get detailed parking information including spots and restrictions",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the parking spot"
                    }
                },
                "required": ["title"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_payment_methods",
            "description": "Get available payment methods for a specific parking spot",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the parking spot"
                    }
                },
                "required": ["title"],
            },
        }    },
    {
        "type": "function",
        "function": {
            "name": "get_available_spots",
            "description": "Get parking spots that currently have free spaces",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_spots_by_height",
            "description": "Find parking spots that can accommodate vehicles of a specific height",
            "parameters": {
                "type": "object",
                "properties": {
                    "min_height": {
                        "type": "number",
                        "description": "Minimum height clearance required in meters"
                    }
                },
                "required": ["min_height"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_cheapest_spots",
            "description": "Get parking spots sorted by hourly rate",
            "parameters": {
                "type": "object",
                "properties": {
                    "hours": {
                        "type": "integer",
                        "description": "Number of hours for price comparison",
                        "default": 2
                    }
                },
                "required": [],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_spots_with_disabled_access",
            "description": "Find parking spots that have disabled parking spaces",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        }
    },
]
