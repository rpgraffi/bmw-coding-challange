from typing import Any, Dict, Protocol

class IntentService(Protocol):
    def handle_intent(self, intent: Any) -> Dict[str, Any]:
        ...