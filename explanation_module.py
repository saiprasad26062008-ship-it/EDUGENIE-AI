from gemini_client import generate


def explain_topic(topic: str) -> str:

    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
You are EduGenie, an expert teacher.

Explain this topic to a beginner:

Topic:
{topic}

Use this format:

1. Definition
2. Simple Explanation
3. Example
4. Key Points
5. Real-life Application

Use simple English so that a student can easily understand
and study the topic.
"""

    try:
        return generate(prompt)

    except Exception as e:
        return f"AI Error: {e}"