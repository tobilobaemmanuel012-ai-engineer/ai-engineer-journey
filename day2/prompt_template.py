print("PROMPT TEMPLATE BUILDER")
print("-----------------------")

role = input("AI role: ")
audience = input("Who is the answer for? ")
topic = input("Topic: ")

prompt = f"""
You are an expert {role}.

Explain {topic} to {audience}.

Rules:
- Use simple language.
- Give clear examples.
- Avoid unnecessary technical words.
- Organize the answer with headings.
- End with a short question to test understanding.
- Explain the topic using one real-life example.
"""

print("\nGENERATED PROMPT")
print("----------------")
print(prompt)