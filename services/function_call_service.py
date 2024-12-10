from typing import Any, Dict, Optional, List
from tools.parking_tools import ParkingTools
from tools.sushi_tools import SushiTools
from core.json_service import dump_json_data
from core.messages_service import MessagesService
import json

class FunctionCallService:
    """Service for handling function calls from AI responses"""
    
    def __init__(self, messages_service: MessagesService):
        """
        Initialize the FunctionCallService
        
        Args:
            messages_service (MessagesService): Service for handling message history
        """
        self.messages_service = messages_service
        self._initialize_tools()
    
    def _initialize_tools(self) -> None:
        """Initialize tool handlers and function mappings"""
        self._tool_handlers = [
            ParkingTools(),
            SushiTools()
        ]
        
        # Combine all function mappings
        self._function_mapping = {}
        for handler in self._tool_handlers:
            self._function_mapping.update(handler.function_mapping)
    
    @property
    def all_tools(self) -> List[Dict]:
        """Get all available tools from all handlers"""
        tools = []
        for handler in self._tool_handlers:
            tools.extend(handler.tools)
        return tools
    
    def execute_function(self, function_name: str, arguments: Dict[str, Any]) -> Optional[Any]:
        """Execute a function by name with the provided arguments"""
        if function_name not in self._function_mapping:
            raise ValueError(f"Unknown function: {function_name}")
            
        try:
            result = self._function_mapping[function_name](**arguments)
            
            if result is not None:
                result_json = dump_json_data(result)
                self.messages_service.add_function_message(function_name, result_json)
            
            return result
            
        except Exception as e:
            error_message = f"Error executing {function_name}: {str(e)}"
            print(error_message)
            raise RuntimeError(error_message) from e
    
    def handle_ai_message(self, message: Any) -> Optional[Any]:
        """Handle an AI message containing function calls"""
        if not hasattr(message, 'tool_calls') or not message.tool_calls:
            return None
            
        function_name = message.tool_calls[0].function.name
        arguments = json.loads(message.tool_calls[0].function.arguments)
        
        return self.execute_function(function_name, arguments) 