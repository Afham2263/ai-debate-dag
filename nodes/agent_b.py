import os
from dotenv import load_dotenv
from groq import Groq
from langchain_core.runnables import Runnable
from typing import Dict

load_dotenv()

class AgentB(Runnable):
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def invoke(self, state: Dict, config=None) -> Dict:
        topic = state["topic"]
        last = state["last"] or "None"
        prompt = f"You are Agent B. Topic: {topic}. Opponent said: {last}\nYour argument:"
        resp = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7, max_tokens=300
        )
        reply = resp.choices[0].message.content.strip()
        return {"last": "AgentB: " + reply}
