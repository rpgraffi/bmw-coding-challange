user_interest_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_user_interest",
            "description": "Get the user's interest, Sushi, Parking or Both",
            "parameters": {
                "type": "object",
                "properties": {
                    "interest": {
                        "type": "string",
                        "enum": ["SUSHI", "PARKING", "BOTH"],
                        "description": "The user's interest, e.g. sushi, parking or both",
                    },
                    "assistant_message": {
                        "type": "string",
                        "description": "Friendly message to display to user"
                    }
                },
                "required": ["interest", "assistant_message"],
                "additionalProperties": False,
            },
        },
    }
]