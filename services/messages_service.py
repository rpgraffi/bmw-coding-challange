from pydantic import BaseModel


class MessagesService:
    def __init__(self):
        self.messages = []
        
    def _prepare_message(self, data):
        if isinstance(data, BaseModel):
            return data.model_dump_json()
        return (data)
        
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
        
    def add_assistant_message(self, message):
        content = self._prepare_message(message)
        self.messages.append({"role": "assistant", "content": content})
        
    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})
        
    def add_function_message(self, function_name, function_arguments):
        
        content = self._prepare_message(function_arguments)
        
        self.messages.append({
            "role": "function",
            "name": function_name,
            "content": content
        })
        
    def add_function_messages(self, messages):
        for message in messages:
            self.add_function_message(message["name"], message["content"])
