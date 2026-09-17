# 🤖 AutoTaskerAI — Multi-Agent AI System

> **A Gemini-powered multi-agent AI system that transforms complex tasks into structured plans, research insights, implementation solutions, and quality-reviewed outputs.**

---

## 📌 Overview

**AutoTaskerAI** is a multi-agent artificial intelligence system designed to solve user-provided tasks through a collaborative sequence of specialized AI agents.

Instead of asking a single AI model to perform an entire task at once, AutoTaskerAI divides the task into multiple stages:

**User Task → Planner → Researcher → Coder → Reviewer → Final Output**

The system is powered by the **Google Gemini API** and provides both a command-line interface and an interactive **Streamlit web interface**.

The project demonstrates practical concepts such as:

* Multi-Agent AI Architecture
* LLM Orchestration
* Prompt Engineering
* Task Decomposition
* AI-Assisted Research
* Code Generation
* Automated Evaluation
* Confidence & Quality Scoring
* Streamlit UI Development

---

## ✨ Features

* 🧠 **Planner Agent** — Breaks complex tasks into clear, logical steps.
* 🔍 **Researcher Agent** — Identifies relevant concepts, algorithms, tools, and approaches.
* 💻 **Coder Agent** — Converts research into implementation-level solutions or code.
* 🧪 **Reviewer Agent** — Evaluates the generated solution.
* 📊 **AI Evaluation Scores** — Generates Quality, Confidence, and Readiness scores.
* 🤖 **Google Gemini Powered** — Uses Gemini as the underlying LLM.
* 🎨 **Interactive Streamlit UI** — Provides a visual interface for running tasks.
* 🧩 **Modular Architecture** — Each agent is separated into its own Python module.
* 🔐 **Environment-Based API Key** — API credentials are loaded using `.env`.
* ⚡ **Dynamic Task Handling** — The system can process different types of user tasks.

---

# 🏗️ System Architecture

```text
                         ┌──────────────────┐
                         │    User Task     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  🧠 Planner      │
                         │ Task Decomposition│
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ 🔍 Researcher    │
                         │ Research & Tools │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ 💻 Coder        │
                         │ Implementation   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ 🧪 Reviewer      │
                         │ Evaluation       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  📊 Final Output │
                         │ Scores + Review  │
                         └──────────────────┘
```

---

# 🧠 Agents

## 1. 🧠 Planner Agent

The Planner is the first stage of the system.

It receives the user's task and converts it into a structured, numbered execution plan.

### Responsibilities

* Understand the user's objective
* Decompose the task
* Create logical execution steps
* Provide a structured plan for downstream agents

---

## 2. 🔍 Researcher Agent

The Researcher receives the Planner's output and identifies the important concepts, algorithms, tools, and approaches required to complete the task.

### Responsibilities

* Analyze the execution plan
* Identify relevant concepts
* Suggest algorithms
* Suggest tools and technologies
* Provide technical guidance to the Coder

---

## 3. 💻 Coder Agent

The Coder uses the Researcher's output to generate implementation-level details or code.

### Responsibilities

* Convert research into an implementation
* Generate readable code
* Provide technical solutions
* Follow the requirements identified by previous agents

---

## 4. 🧪 Reviewer Agent

The Reviewer acts as the quality-control stage of the pipeline.

It evaluates the generated solution and produces three numerical metrics:

* **Quality Score**
* **Confidence Score**
* **Readiness Score**

It also identifies strengths, weaknesses, and provides a final review.

### Responsibilities

* Evaluate the generated solution
* Identify strengths
* Identify weaknesses
* Calculate evaluation scores
* Determine solution readiness

---

# 🔄 How It Works

### Step 1 — User Input

The user enters a task into the application.

Example:

```text
Build a sentiment analysis system for product reviews.
```

---

### Step 2 — Planning

The Planner analyzes the task and creates a step-by-step plan.

```text
1. Understand the problem
2. Collect and preprocess data
3. Select an appropriate ML approach
4. Train the model
5. Evaluate the model
6. Generate the final implementation
```

---

### Step 3 — Research

The Researcher analyzes the generated plan and identifies:

* Algorithms
* Libraries
* Tools
* Technical approaches
* Implementation considerations

---

### Step 4 — Coding

The Coder converts the research into implementation-level details or code.

---

### Step 5 — Review

The Reviewer analyzes the generated solution and returns:

```text
QUALITY_SCORE: 90
CONFIDENCE_SCORE: 88
READINESS_SCORE: 75
```

Along with:

* Strengths
* Weaknesses
* Final review

---

### Step 6 — Final Output

The system presents the complete workflow and evaluation to the user.

---

# 🖥️ User Interface

AutoTaskerAI includes a Streamlit-based web interface.

The interface provides:

* Task input area
* Run button
* Planner output
* Researcher output
* Generated solution
* Reviewer evaluation
* Quality indicators
* Dark-themed UI

The Streamlit application configures the page as **AutoTaskerAI** and displays the four agents as separate stages.

---

# 📂 Project Structure

```text
AutoTaskerAI/
│
├── app.py
│
├── main.py
│
├── planner.py
├── researcher.py
├── coder.py
├── reviewer.py
│
├── gemini_client.py
├── memory.py
│
├── requirements.txt
├── .env
└── README.md
```

### File Description

| File               | Purpose                      |
| ------------------ | ---------------------------- |
| `app.py`           | Streamlit web interface      |
| `main.py`          | Command-line execution       |
| `planner.py`       | Planner Agent                |
| `researcher.py`    | Researcher Agent             |
| `coder.py`         | Coder Agent                  |
| `reviewer.py`      | Reviewer Agent               |
| `gemini_client.py` | Gemini API integration       |
| `memory.py`        | Shared memory implementation |
| `requirements.txt` | Python dependencies          |
| `.env`             | Environment variables        |
| `README.md`        | Project documentation        |

---

# 🔗 Agent Workflow in Code

The command-line application executes the agents sequentially:

```text
User Task
   ↓
Planner
   ↓
Researcher
   ↓
Coder
   ↓
Reviewer
   ↓
Scores + Detailed Review
```

The main execution flow passes the Planner output to the Researcher, then the Researcher output to the Coder, and finally the generated solution to the Reviewer.

---

# 🤖 Gemini Integration

The project uses Google's `google-genai` library to communicate with Gemini.

The Gemini client loads the API key from an environment variable:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

The project currently uses:

```text
models/gemini-flash-latest
```

The shared Gemini client exposes a `gemini_call()` function that sends prompts to the model and returns the generated response.

---

# 🔐 Environment Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### ⚠️ Important

Never commit your `.env` file or API key to GitHub.

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/AutoTaskerAI.git
cd AutoTaskerAI
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Gemini API

Create `.env`:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

# 🚀 Running the Project

## Streamlit Web Application

Run:

```bash
streamlit run app.py
```

Then open the Streamlit URL shown in your terminal.

---

## Command-Line Version

You can also run the system from the terminal:

```bash
python main.py
```

The CLI version asks for a task and runs it through all four agents.

---

# 📊 Evaluation System

The Reviewer generates three metrics:

| Metric           | Description                                               |
| ---------------- | --------------------------------------------------------- |
| Quality Score    | Overall quality of the generated solution                 |
| Confidence Score | Reviewer's confidence in the solution                     |
| Readiness Score  | Assessment of how ready the solution is for practical use |

The scores are returned on a **0–100 scale**.

---

# 🧠 Shared Memory

The project also contains a `SharedMemory` class that provides a simple key-value storage mechanism.

It supports:

```python
save(key, value)
```

and

```python
get(key)
```

This provides a foundation for passing or storing information between components of the multi-agent system.

---

# 🛠️ Tech Stack

### Programming Language

* Python

### AI / LLM

* Google Gemini
* `google-genai`

### Frontend

* Streamlit
* HTML
* CSS

### Configuration

* Python-dotenv

### Architecture

* Multi-Agent AI
* Modular Agent Design
* Prompt-Based Agent Orchestration

---

# 🎯 Project Goals

The primary goals of AutoTaskerAI are to:

1. Demonstrate practical multi-agent AI architecture.
2. Divide complex tasks into specialized stages.
3. Use LLMs for planning, research, coding, and evaluation.
4. Create a modular architecture that can be extended with additional agents.
5. Provide a user-friendly interface for interacting with the system.
6. Introduce automated evaluation of AI-generated solutions.

---

# 🔮 Future Improvements

Potential future extensions include:

* 🔁 Agent feedback loops
* 🧠 Persistent long-term memory
* 🔎 Real web-search capabilities for the Researcher
* 🛠️ Tool/API calling
* 🧪 Automatic code execution and testing
* 🔄 Reviewer → Coder iterative correction
* 📚 RAG-based knowledge retrieval
* 💾 Database-backed memory
* 👥 Additional specialized agents
* 🔐 Authentication and user management
* 📈 Agent performance analytics
* ⚡ Parallel agent execution

A future architecture could look like:

```text
                         User
                          │
                          ▼
                       Planner
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
         Researcher                Analyst
              │                       │
              └───────────┬───────────┘
                          ▼
                        Coder
                          │
                          ▼
                       Tester
                          │
                          ▼
                       Reviewer
                          │
                    ┌─────┴─────┐
                    │           │
                 PASS          FAIL
                    │           │
                    ▼           ▼
               Final Output   Coder
                              ↺
```

---

# 📚 Learning Outcomes

This project provides practical experience with:

* Large Language Models
* AI Agents
* Prompt Engineering
* Agent Orchestration
* Python Modular Programming
* API Integration
* Environment Variables
* Streamlit Development
* Automated Evaluation
* Software Architecture
* AI System Design

---

# 👨‍💻 Project Status

**Status:** 🚧 Active Development

AutoTaskerAI currently supports a sequential four-agent workflow:

```text
Planner → Researcher → Coder → Reviewer
```

The architecture is designed so additional agents and tools can be integrated in future versions.

---

# 📄 License

This project is intended for educational and development purposes.

You may modify and extend the project according to your requirements.

---

# ⭐ Acknowledgements

* Google Gemini for the underlying generative AI capabilities
* Streamlit for the interactive application framework
* Python open-source ecosystem

---

## 🤖 AutoTaskerAI

**Plan. Research. Build. Review.**

> Turning a single AI prompt into a collaborative multi-agent workflow.
