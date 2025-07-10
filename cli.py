from debate_graph import graph
from logger import log_message

def main():
    print("\n Welcome to the AI Debate Simulator!\n")
    topic = input("Enter topic for debate: ").strip()
    state = {"topic": topic, "history": [], "last": "", "verdict": ""}
    log_message(f"[CLI] Topic: {topic}")
    final_state = graph.invoke(state)
    print("\n Debate Finished!\n")
    for line in final_state["history"]:
        print(line)
    print("\n Verdict:\n" + final_state["verdict"])
    log_message("[CLI] Final Verdict: " + final_state["verdict"])

if __name__ == "__main__":
    main()
