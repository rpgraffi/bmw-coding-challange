from json import JSONEncoder
from dataclasses import asdict, is_dataclass
from pydantic import BaseModel

class ModelEncoder(JSONEncoder):
    """Custom JSON encoder for model classes"""
    def default(self, obj):
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj) 