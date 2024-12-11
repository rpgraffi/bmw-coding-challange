import os
import instructor
from openai import OpenAI
from dotenv import load_dotenv
from services.core.messages_service import MessagesService
from models.intent.user_interest_intent import UserInterestIntent
from models.intent.assistant_model import AssistantModel
from services.user.user_interest_service import get_user_interest

class SushiParkingAssistant:
    def __init__(self):
        # Initialize OpenAI
        load_dotenv()
        self.client = instructor.patch(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))
        self.openai_model = "gpt-3.5-turbo"
        
        # Initialize services
        self.messages_service = MessagesService()
        self._setup_system_prompt()

    def _setup_system_prompt(self):
        system_prompt = """You are an assistant that helps users find sushi restaurants and parking spots in Munich. 
        When a user expresses interest in either sushi, parking, or both:
        1. Use the set_user_interest function to record their preference
        2. Provide relevant parking or restaurant information
        3. ALWAYS respond with a natural language message summarizing the information for the user
        """
        self.messages_service.add_system_message(system_prompt)

    def process_user_message(self, user_input: str) -> str:
        """Process a single user message and return the assistant's response"""
        # Add user message
        self.messages_service.add_user_message(user_input)
        
        # Get user interest
        interest_intent: UserInterestIntent = self.client.chat.completions.create(
            model=self.openai_model,
            messages=self.messages_service.get_messages(),
            response_model=UserInterestIntent,
        )

        self.messages_service.add_assistant_message(interest_intent.assistant_message)
        self.messages_service.add_function_message(UserInterestIntent.__name__, interest_intent.interest)

        # Get appropriate response model and service based on user interest
        response_model, intent_service = get_user_interest(interest_intent.interest)

        # Get specific intent
        intent = self.client.chat.completions.create(
            model=self.openai_model,
            messages=self.messages_service.get_messages(),
            response_model=response_model,
        )

        self.messages_service.add_function_message(intent.__class__.__name__, intent)

        # If not a assistance intent, handle intent and get result
        if not isinstance(intent_service, AssistantModel):
            result = intent_service.handle_intent(intent)
            self.messages_service.add_function_message(intent_service.handle_intent.__name__, result)

            # llm generates final response based on intent and result
            response = self.client.chat.completions.create(
                model=self.openai_model,
                messages=self.messages_service.get_messages(),
                response_model=AssistantModel,
            )

            self.messages_service.add_assistant_message(response.assistant_message)
            return response.assistant_message
        
        return intent.assistant_message

    def chat(self):
        """Start an interactive chat session"""
        print("Welcome to Munich Sushi & Parking Assistant! (Type 'quit' to exit)")
        print("-" * 50)
        
        while True:
            user_input = input("\nUser: ")
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye!")
                break
                
            response = self.process_user_message(user_input)
            print(f"\nAssistant: {response}")

def main():
    assistant = SushiParkingAssistant()
    assistant.chat()

if __name__ == "__main__":
    main() 