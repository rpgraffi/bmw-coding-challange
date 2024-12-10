from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field

class UserParkingIntent(BaseModel):
    """Determines what parking information the user is looking for"""
    query_type: Literal[
        "list_all",          # get_all_parking_spots_names
        "specific_spot",     # get_parking_spots with specific title
        "cheapest",          # get_cheapest_spots
        "nearby",            # get_position (with location context)
        "availability",      # get_available_spots
        "accessibility",     # find_spots_with_disabled_access
        "height_check",      # find_spots_by_height
        "business_hours",    # get_business_hours
        "payment_info",      # get_payment_methods
        "price_check",       # get_price_summary
        "contact",           # get_contact_info
        "detailed_info"      # get_parking_info
    ] = Field(
        description="Type of parking information the user is requesting"
    )

    # Optional parameters based on query type
    specific_spot_name: Optional[str] = Field(
        default=None,
        description="Name of specific parking spot if user asks about one"
    )
    
    duration_hours: Optional[int] = Field(
        default=None,
        description="If user specified duration for parking, in hours"
    )
    
    height_requirement: Optional[float] = Field(
        default=None,
        description="If user specified vehicle height requirement, in meters",
        ge=1,
        le=3
    )
    
    location: Optional[str] = Field(
        default=None,
        description="If user specified a location"
    )
    
    needs_disabled_access: Optional[bool] = Field(
        default=None,
        description="If user specifically asked about disabled parking"
    )
    
    payment_method_preference: Optional[str] = Field(
        default=None,
        description="If user asked about specific payment methods (e.g., 'cash', 'credit card')"
    )

    response_detail: Literal["brief", "detailed"] = Field(
        default="brief",
        description="How detailed the response should be"
    )

# Example usage:
"""
User: "What's the cheapest parking spot for 3 hours?"
Intent:
{
    "query_type": "cheapest",
    "duration_hours": 3,
    "response_detail": "brief"
}

User: "Is there parking near Marienplatz that can fit a van that's 2.5m tall?"
Intent:
{
    "query_type": "height_check",
    "location": "Marienplatz",
    "height_requirement": 2.5,
    "response_detail": "brief"
}

User: "Tell me everything about the City parking garage"
Intent:
{
    "query_type": "detailed_info",
    "specific_spot_name": "City",
    "response_detail": "detailed"
}

User: "Are there any available spots with disabled parking?"
Intent:
{
    "query_type": "accessibility",
    "needs_disabled_access": true,
    "response_detail": "brief"
}

User: "What time does Marienplatz parking close?"
Intent:
{
    "query_type": "business_hours",
    "specific_spot_name": "Marienplatz",
    "response_detail": "brief"
}
"""
