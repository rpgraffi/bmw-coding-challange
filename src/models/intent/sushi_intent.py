from typing import Literal, Optional, Set
from pydantic import BaseModel, Field


class UserSushiIntent(BaseModel):
    """Determines what sushi restaurant information the user is looking for"""
    query_types: Set[Literal[
        "list_all",          # get_all_sushi_restaurants_names
        "specific_restaurant", # get_restaurant with specific title
        "reviews",           # get_reviews
        "nearby",            # get_position (with location context)
        "business_hours",    # get_business_hours
        "price_check",       # get_price_summary
        "contact"            # get_contact_info
    ]] = Field(
        description="""Types of sushi restaurant information the user is requesting. Can be multiple.
        You can be generouse and add more query types if you think it is necessary.
        If user mentions any time add "business_hours" to the query_types.
        If user want to talk to someone, add "contact" to the query_types.
        If user want to know the price or costs, add "price_check" to the query_types.
        """
    )

    specific_restaurant_name: Optional[str] = Field(
        default=None,
        description="Name of specific sushi restaurant if user asks about one"
    )
    
    location: Optional[str] = Field(
        default=None,
        description="If user specified a location"
    )
    
    response_detail: Literal["brief", "detailed"] = Field(
        default="brief",
        description="If the user request is very very complex or the user is asking for a lot of information, the response should be detailed"
    )

