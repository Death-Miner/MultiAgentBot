import streamlit as st
import time

from planner import planner_agent
from researcher import researcher_agent
from coder import coder_agent
from reviewer import reviewer_agent

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AutoTaskerAI",
    page_icon="🤖",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

.main-title {
    font-size: 44px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #a78bfa);
    -webkit-background-clip: text;
    color: transparent;
    text-align: center;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #94a3b8;
    margin-bottom: 30px;
}

.agent-card {
    background: #020617;
    border: 1px solid #1e293b;
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 35px;
    box-shadow: 0 0 25px rgba(56,189,248,0.25);
    animation: fadeIn 0.6s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}

.agent-title {
    font-size: 26px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 10px;
}

.agent-sub {
    font-size: 15px;
    color: #94a3b8;
    margin-bottom: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="main-title">🤖 AutoTaskerAI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Pure Gemini Powered Multi-Agent System</div>', unsafe_allow_html=True)
st.markdown("---")

# ---------- INPUT ----------
task = st.text_area(
    "💡 Enter your task",
    placeholder="Example: Build a student chatbot",
    height=120
)

run = st.button("🚀 Run Multi-Agent System")

# ---------- EXECUTION ----------
if run and task.strip():

    # 🧠 PLANNER
    with st.spinner("🧠 Planner thinking..."):
        time.sleep(1)
        plan = planner_agent(task)

    st.markdown(f"""
    <div class="agent-card">
        <div class="agent-title">🧠 Planner</div>
        <div class="agent-sub">Full task planning & execution strategy</div>
        {plan}
    </div>
    """, unsafe_allow_html=True)

    # 🔍 RESEARCHER
    with st.spinner("🔍 Researcher analyzing..."):
        time.sleep(1)
        research = researcher_agent(plan)

    st.markdown(f"""
    <div class="agent-card">
        <div class="agent-title">🔍 Researcher</div>
        <div class="agent-sub">Algorithms, tools & best practices</div>
        {research}
    </div>
    """, unsafe_allow_html=True)

    # 💻 CODER
    with st.spinner("💻 Coder building solution..."):
        time.sleep(1)
        solution = coder_agent(research)

    st.markdown("""
    <div class="agent-card">
        <div class="agent-title">💻 Coder</div>
        <div class="agent-sub">Clean, beginner-friendly implementation</div>
    </div>
    """, unsafe_allow_html=True)

    st.code(solution, language="python")

    # 🧪 REVIEWER
    with st.spinner("🧪 Reviewer reviewing..."):
        time.sleep(1)
        review = reviewer_agent(solution)

    st.markdown(f"""
    <div class="agent-card">
        <div class="agent-title">🧪 Reviewer</div>
        <div class="agent-sub">Confidence, quality & readiness scoring</div>
        {review}
    </div>
    """, unsafe_allow_html=True)

    st.success("✅ Task completed successfully!")

elif run:
    st.warning("⚠️ Please enter a task first.")
