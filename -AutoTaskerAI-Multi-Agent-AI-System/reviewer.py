from gemini_client import gemini_call

def reviewer_agent(solution: str) -> dict:
    prompt = f"""
You are a strict AI reviewer.

Evaluate the following solution and respond in EXACTLY this format:

QUALITY_SCORE: <0-100>
CONFIDENCE_SCORE: <0-100>
READINESS_SCORE: <0-100>

STRENGTHS:
- bullet points

WEAKNESSES:
- bullet points

FINAL_VERDICT:
One short paragraph on whether this solution is production-ready.

Solution:
{solution}
"""

    response = gemini_call(prompt)

    return parse_review(response)


def parse_review(text: str) -> dict:
    result = {
        "quality": 0,
        "confidence": 0,
        "readiness": 0,
        "full_review": text
    }

    for line in text.splitlines():
        if "QUALITY_SCORE" in line:
            result["quality"] = extract_score(line)
        elif "CONFIDENCE_SCORE" in line:
            result["confidence"] = extract_score(line)
        elif "READINESS_SCORE" in line:
            result["readiness"] = extract_score(line)

    return result


def extract_score(line: str) -> int:
    try:
        return int("".join(filter(str.isdigit, line)))
    except:
        return 0
