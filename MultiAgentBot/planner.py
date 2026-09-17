from gemini_client import gemini_call

def planner_agent(task: str) -> str:
    prompt = f"""
You are an expert AI planner.
Break the following task into clear, numbered steps.

Task:
{task}
"""
    return gemini_call(prompt)
