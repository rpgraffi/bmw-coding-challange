sushi_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_sushi_restaurants",
            "description": "Get sushi restaurants in Munich",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the sushi restaurant, e.g. Sasou"
                    }
                },
                "required": ["title"],
                "additionalProperties": False
            }
        }
    }
]