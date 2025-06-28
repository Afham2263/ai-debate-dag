from langchain_core.runnables import Runnable
from typing import Dict

class UserInputNode(Runnable):
    def invoke(self, state: Dict, config=None) -> Dict:
        # Only set topic, history, verdict on the first call
        if "topic" not in state:
            state["topic"] = input("Enter topic for debate: ")
            state["history"] = []
            state["verdict"] = ""
        return state
