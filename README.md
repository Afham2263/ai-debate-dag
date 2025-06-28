
# 🧠 AI Debate Simulator

A structured, multi-agent debate system powered by LangGraph and GroqCloud.  
Two AI agents engage in a round-based debate on a user-provided topic. After 8 turns (4 per agent), a judge node analyzes the discussion and declares a winner.

---

## 📂 Project Structure

````

debate-dag/
├── cli.py             # CLI interface to run the debate
├── debate\_graph.py    # LangGraph DAG structure
├── logger.py          # Logging system
├── .gitignore         # Ensures .env and other sensitive files are ignored
├── requirements.txt   # Python dependencies
├── nodes/
│   ├── agent\_a.py     # Debate agent A (scientist persona)
│   ├── agent\_b.py     # Debate agent B (philosopher persona)
│   ├── memory.py      # Memory node for tracking conversation history
│   ├── judge.py       # Final judging logic
│   └── user\_input.py  # Initial topic intake

````

---

## ⚙️ Requirements

- Python 3.10 or higher
- A free [Groq API key](https://console.groq.com/)
- Internet connection to access GroqCloud-hosted models

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
````

---

## 🔐 Environment Variable

The project uses the GroqCloud-hosted Mixtral model. You’ll need to set your API key as an environment variable:

#### Windows (CMD):

```cmd
set GROQ_API_KEY=your_key_here
```

#### PowerShell:

```powershell
$env:GROQ_API_KEY="your_key_here"
```

---

## 🚀 Usage

Run the CLI interface:

```bash
python cli.py
```

You’ll be prompted to enter a topic. The system will simulate 8 alternating debate rounds and produce a final verdict from the judge.

---

## 🧠 DAG: Debate Flow

```text
[UserInput]
     |
     v
  [AgentA]
     |
     v
  [Memory]
     |
     v
  [AgentB]
     |
     v
  [Memory]
     |
     .
     .
(repeats 4 total rounds)
     .
     .
     v
   [Judge]
     |
     v
    [END]
```

---

## 📝 Logging

Each debate session is logged automatically. You’ll find a log file in the root directory, capturing:

* The topic
* All agent responses
* State transitions
* The final verdict

---



## 💬 Feedback

Feel free to fork or clone this repo to experiment with other agent behaviors, model integrations, or debate formats. For suggestions or issues, open a GitHub issue or pull request.

---

**Built with LangGraph, GroqCloud**

```

