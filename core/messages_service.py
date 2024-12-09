import json

from services.enum_encoder import EnumEncoder


class MessagesService:
    def __init__(self):
        self.messages = []
        
    def get_messages(self) -> list[dict]:
        return self.messages
    
    def get_last_message(self) -> dict:
        return self.messages[-1]
    
    def print_messages(self):
        for message in self.messages:
            print(message)
            
    def print_last_message(self):
        print(self.messages[-1])
    
    def clear_messages(self):
        self.messages = []
        
    def add_system_message(self, message):
        self.messages.append({"role": "system", "content": message})
        
    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})
        
    def add_function_message(self, function_name, function_arguments):
        if not isinstance(function_arguments, str):
            function_arguments = json.dumps(function_arguments, cls=EnumEncoder)
        
        self.messages.append({
            "role": "function",
            "name": function_name,
            "content": function_arguments
        })
        
    def add_function_messages(self, messages):
        for message in messages:
            self.add_function_message(message["name"], message["content"])
