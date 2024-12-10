import json
from core.model_encoder import ModelEncoder

def dump_json_data(data):
    """Dumps data to JSON string using custom encoder"""
    return json.dumps(data, cls=ModelEncoder, ensure_ascii=False)

def load_json_data(file_path: str):
    """Loads JSON data from file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)