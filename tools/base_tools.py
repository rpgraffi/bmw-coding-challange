from typing import Dict, List, Type
from abc import ABC, abstractmethod

class BaseTools(ABC):
    """Base class for tool definitions"""
    
    @property
    @abstractmethod
    def tools(self) -> List[Dict]:
        """Return list of tool definitions"""
        pass
    
    @property
    @abstractmethod
    def function_mapping(self) -> Dict:
        """Return mapping of tool names to implementations"""
        pass 