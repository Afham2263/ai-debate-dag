import os
from dotenv import load_dotenv
from groq import Groq
from langchain_core.runnables import Runnable
from typing import Dict
from logger import log_message

load_dotenv()

class JudgeNode(Runnable):
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def invoke(self, state: Dict, config=None) -> Dict:
        topic = state["topic"]
        history = "\n".join(state["history"])
        prompt = (
            f"You are the Judge. Topic: {topic}\n\nTranscript:\n{history}\n\n"
            "Summarize and declare winner."
        )
        resp = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5, max_tokens=400
        )
        verdict = resp.choices[0].message.content.strip()
        log_message("[Judge] " + verdict)
        return {"verdict": verdict}
