# 🤖 AutoTaskerAI – Pure Gemini Multi-Agent AI System

AutoTaskerAI is an **advanced multi-agent AI system** inspired by AutoGPT-style architectures.
It uses **multiple specialized AI agents** (Planner, Researcher, Coder, Reviewer) that collaborate to solve **any user-given task end-to-end**.

This project demonstrates **agent orchestration, reasoning, evaluation, and UI design**, making it highly suitable for **AI Engineer, ML Engineer, and Research roles**.

---

## 🚀 Features

✅ Multi-Agent Architecture
✅ Pure Gemini API (No OpenAI dependency)
✅ Dynamic Task Handling (different outputs for different tasks)
✅ Agent Confidence & Quality Scoring
✅ Simple & Beginner-Friendly Code Generation
✅ Attractive, Animated Streamlit UI
✅ Scalable & Extensible Design

---

## 🧠 Agent Architecture

| Agent         | Responsibility                                   |
| ------------- | ------------------------------------------------ |
| 🧠 Planner    | Breaks the task into clear, logical steps        |
| 🔍 Researcher | Finds algorithms, best practices, and approaches |
| 💻 Coder      | Generates simple, readable implementation code   |
| 🧪 Reviewer   | Evaluates confidence, quality, and readiness     |

Each agent works **independently** but shares context through prompts and shared memory.

---

## 🏗️ Project Structure

```
AutoTaskerAI/
│
├── app.py                  # Streamlit UI
├── core/
│   ├── gemini_client.py    # Gemini API wrapper
│   └── memory.py           # Shared memory system
│
├── agents/
│   ├── planner.py          # Planner agent
│   ├── researcher.py       # Research agent
│   ├── coder.py            # Code generation agent
│   └── reviewer.py         # Evaluation agent
│
├── requirements.txt
├── .env
└── README.md
```

---

## 🔑 How It Works (Simple Explanation)

1. **User enters a task**

   > Example: *“Build a sentiment analysis system for product reviews”*

2. **Planner Agent**

   * Understands the task
   * Creates a step-by-step execution plan

3. **Researcher Agent**

   * Analyzes the plan
   * Suggests algorithms, tools, and approaches

4. **Coder Agent**

   * Converts research into **simple, readable code**
   * Supports multiple programming languages

5. **Reviewer Agent**

   * Evaluates the final solution
   * Gives:

     * Confidence score
     * Quality score
     * Readiness score

---

## 🎯 Example Output

**Planner Output**

```
1. Understand the problem
2. Preprocess the data
3. Select sentiment analysis approach
4. Implement solution
5. Evaluate results
```

**Coder Output (Python)**

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["Good product", "Bad quality"]
labels = [1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

print(model.predict(vectorizer.transform(["Very good product"])))
```

**Reviewer Scores**

* Confidence: 88%
* Quality: 90%
* Readiness: 75%

---

## 🖥️ UI Highlights

* Full-width dynamic layout
* Hover-animated agent cards
* Expandable sections per agent
* Clean dark theme
* Beginner-friendly visual flow

Built using **Streamlit + custom CSS**.

---

## ⚙️ Installation

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4️⃣ Run app

```bash
streamlit run app.py
```

---

## 📦 Tech Stack

* Python
* Gemini API (google-genai)
* Streamlit
* Modular Agent Design
* Prompt Engineering

---

## 🧠 Why Recruiters Love This Project

✔ Shows **future-ready AI system design**
✔ Demonstrates **multi-agent reasoning**
✔ Includes **evaluation & scoring metrics**
✔ Clean UI + strong backend logic
✔ Very few freshers build systems like this

---
