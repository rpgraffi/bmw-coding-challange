from pydantic import BaseModel, Field


class AssistantModel(BaseModel):
    """Base class for assistant tools"""
    
    assistant_message: str = Field(
        description="Just help the user or analyze the data if there is any"
    )
