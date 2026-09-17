from gemini_client import gemini_call

def researcher_agent(plan: str) -> str:
    prompt = f"""
You are a senior AI researcher.
Based on this plan, gather key concepts, algorithms, and tools needed.

Plan:
{plan}
"""
    return gemini_call(prompt)
