from gemini_client import generate


def answer_question(question: str) -> str:

    if not question.strip():
        return "Please enter a question."

    prompt = f"""
You are EduGenie, a friendly AI learning assistant.

Answer the student's question clearly and correctly.

Rules:
- Use simple language.
- Give a clear answer.
- Give an example when useful.
- For calculations, show the important steps.
- Do not invent information.

Student Question:

{question}
"""

    try:
        return generate(prompt)

    except Exception as e:
        return f"AI Error: {e}"