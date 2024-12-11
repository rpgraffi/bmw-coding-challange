from typing import Dict
from src.services.assistant_service import SushiParkingAssistant


class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, SushiParkingAssistant] = {}

    def get_or_create_session(self, session_id: str) -> SushiParkingAssistant:
        if session_id not in self.sessions:
            self.sessions[session_id] = SushiParkingAssistant()
        return self.sessions[session_id]