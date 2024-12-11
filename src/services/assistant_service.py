import os
import instructor
from openai import OpenAI
from dotenv import load_dotenv
from src.services.core.messages_service import MessagesService
from src.models.intent.user_interest_intent import UserInterestIntent
from src.models.intent.assistant_model import AssistantModel
from src.services.user.user_interest_service import get_user_interest

class SushiParkingAssistant:
    def __init__(self):
        load_dotenv()
        self.client = instructor.patch(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))
        self.openai_model = "gpt-3.5-turbo"
        
        self.messages_service = MessagesService()
        self._setup_system_prompt()

    def _setup_system_prompt(self):
        system_prompt = """You are an assistant that helps users find sushi restaurants and parking spots in Munich. 
        When a user expresses interest in either sushi or parking:
        1. Provide relevant parking or restaurant information
        2. When the user just wants to chat and currently available informations are sufficient, respond with a natural language message
        3. You can switch between sushi and parking information at any time, but only do it if its obvious that the user wants to switch
        4. Try to only provide the information that is relevant to the user's interest (you can be generous and add more information if you think it helps the user experience)
        """
        self.messages_service.add_system_message(system_prompt)

    def process_user_message(self, user_input: str) -> str:
        """Process a single user message and return the assistant's response"""
        self.messages_service.add_user_message(user_input)
        
        # Get user interest
        interest_intent: UserInterestIntent = self.client.chat.completions.create(
            model=self.openai_model,
            messages=self.messages_service.get_messages(),
            response_model=UserInterestIntent,
        )

        self.messages_service.add_function_message(UserInterestIntent.__name__, interest_intent.interest)

        # Get appropriate response model and service based on user interest
        response_model, intent_service = get_user_interest(interest_intent.interest)

        # Get specific intent (sushi or parking or chatting)
        intent = self.client.chat.completions.create(
            model=self.openai_model,
            messages=self.messages_service.get_messages(),
            response_model=response_model,
        )


        # If not a assistance intent, handle intent and get result
        if intent_service is not None:
            self.messages_service.add_function_message(intent.__class__.__name__, intent)
            result = intent_service.handle_intent(intent)
            self.messages_service.add_function_message(intent_service.handle_intent.__name__, result)

            # llm generates final response based on intent and result
            response = self.client.chat.completions.create(
                model=self.openai_model,
                messages=self.messages_service.get_messages(),
                response_model=AssistantModel,
            )

            self.messages_service.add_assistant_message(response.assistant_message)
            self.messages_service.print_messages()
            return response.assistant_message
        
        self.messages_service.add_assistant_message(intent.assistant_message)
        self.messages_service.print_messages()
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