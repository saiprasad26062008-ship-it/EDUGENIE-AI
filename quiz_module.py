import json
import re

from gemini_client import generate


def extract_json(text):

    text = text.strip()

    text = re.sub(
        r"^```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^```\s*",
        "",
        text
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    start = text.find("[")
    end = text.rfind("]")

    if start == -1 or end == -1:
        raise ValueError("Quiz JSON not found.")

    return json.loads(
        text[start:end + 1]
    )


def generate_quiz(topic: str):

    if not topic.strip():
        return []

    prompt = f"""
Create a quiz about:

{topic}

Return ONLY valid JSON.

Create exactly 3 questions.

Each question must have:
- question
- exactly 4 options
- exactly 1 correct answer
- explanation

Use this format:

[
  {{
    "question": "Question",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": 0,
    "explanation": "Why this answer is correct"
  }}
]

The answer number must be:

0 = first option
1 = second option
2 = third option
3 = fourth option
"""

    try:

        result = extract_json(
            generate(prompt)
        )

        return result[:3]

    except Exception as e:

        return [
            {
                "question": "Quiz generation failed.",
                "options": [
                    "Try again",
                    "Check API key",
                    "Check internet",
                    "None"
                ],
                "answer": 0,
                "explanation": str(e)
            }
        ]