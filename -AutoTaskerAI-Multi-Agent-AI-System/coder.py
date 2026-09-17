from gemini_client import gemini_call

def coder_agent(research: str) -> str:
    prompt = f"""
You are an expert software engineer.
Using the research below, write implementation-level details or code.

Research:
{research}
"""
    return gemini_call(prompt)
