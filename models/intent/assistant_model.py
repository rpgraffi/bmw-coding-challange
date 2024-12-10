from pydantic import BaseModel, Field


class AssistantModel(BaseModel):
    """Base class for assistant tools"""
    
    assistant_message: str = Field(
        description="Message that the assistant will send to the user"
    )
