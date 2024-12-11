from pydantic import BaseModel, Field


class AssistantModel(BaseModel):
    """Base class for assistant tools"""
    
    assistant_message: str = Field(
        description="Help the user with their request and provide the data if there is any"
    )
