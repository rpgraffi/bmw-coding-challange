from typing import List, Literal, Optional, Set

from pydantic import BaseModel, Field

from models.intent.assistant_model import AssistantModel


class UserParkingIntent(AssistantModel):
    """Determines what parking information the user is looking for"""
    query_types: List[Literal[
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
    ]] = Field(
        description="Types of parking information the user is requesting. Can be multiple."
    )

    # Optional parameters based on query types
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
