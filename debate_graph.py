from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from nodes.agent_a import AgentA
from nodes.agent_b import AgentB
from nodes.memory import MemoryNode
from nodes.judge import JudgeNode

class DebateState(TypedDict):
    topic: str
    history: List[str]
    last: str           # the last argument from an agent
    verdict: str

builder = StateGraph(state_schema=DebateState)

builder.add_node("AgentA", AgentA())
builder.add_node("Memory", MemoryNode())
builder.add_node("AgentB", AgentB())
builder.add_node("Memory2", MemoryNode())  # reuse MemoryNode for B’s turn
builder.add_node("Judge", JudgeNode())

builder.set_entry_point("AgentA")

# Round 1 A → Memory → B → Memory → A → Memory → B → Memory → Judge
for _ in range(4):
    builder.add_edge("AgentA", "Memory")
    builder.add_edge("Memory", "AgentB")
    builder.add_edge("AgentB", "Memory2")

builder.add_edge("Memory2", "Judge")
builder.add_edge("Judge", END)

graph = builder.compile()
