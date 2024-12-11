from typing import Literal, Optional, Set
from pydantic import BaseModel, Field


class UserParkingIntent(BaseModel):
    """Determines what parking information the user is looking for"""
    query_types: Set[Literal[
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
    ]] = Field(
        description="""Types of parking information the user is requesting. Can be multiple.
        You can be generouse and add more query types if you think it is necessary.
        If user mention any time add "business_hours" to the query_types.
        If user want to talk to someone, add "contact" to the query_types.
        If user want to know the price or costs, add "price_check" and "payment_info" to the query_types.
        """
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
        description="If user mention vehicle height/size",
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
        description="If user asked about payment methods (e.g., 'cash', 'credit card')"
    )

    response_detail: Literal["brief", "detailed"] = Field(
        default="brief",
        description="If the user request is very very complex, the response should be detailed"
    )
