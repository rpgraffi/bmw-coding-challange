parking_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_parking_spots",
            "description": "Get parking spots in Munich",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the sushi restaurant, e.g. Sasou",
                        },
                    },
                    "required": ["title"],
                    "additionalProperties": False,
                },
        }
    }
]