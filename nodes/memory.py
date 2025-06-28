from langchain_core.runnables import Runnable
from typing import Dict

class MemoryNode(Runnable):
    def invoke(self, state: Dict, config=None) -> Dict:
        entry = state.get("last", "")
        history = state.get("history", [])
        if entry:
            history.append(entry)
        return {"history": history}
