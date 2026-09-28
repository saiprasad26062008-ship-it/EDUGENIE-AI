from gemini_client import generate


def summarize_text(text: str) -> str:

    if not text.strip():
        return "Please paste some content."

    prompt = f"""
You are EduGenie, a study assistant.

Summarize the following content for exam preparation.

Rules:
- Keep all important information.
- Remove unnecessary repetition.
- Use short bullet points.
- Make it easy to study.
- Do not add unrelated information.

Content:

{text}
"""

    try:
        return generate(prompt)

    except Exception as e:
        return f"AI Error: {e}"