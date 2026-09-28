from gemini_client import generate


def get_learning_recommendations(topic: str) -> str:

    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
You are EduGenie, a personalized learning coach.

Create a complete learning path for:

{topic}

Start from beginner level and gradually move to advanced level.

Use these sections:

I. Beginner Level: Building a Foundation

II. Intermediate Level: Working with More Complex Concepts

III. Advanced Level: Mastery

IV. Practice Projects

V. Recommended Resources

VI. Adaptive Learning Tips

For every level include:

- Estimated Time
- Key Topics
- What the student should learn
- What the student should be able to do

Make the plan practical and student friendly.
"""

    try:
        return generate(prompt)

    except Exception as e:
        return f"AI Error: {e}"