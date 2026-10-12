print("ADVANCED PROMPT BUILDER")
print("-----------------------")

topic = input("Enter a topic: ")
learner = input("Who are you teaching? ")
examples = input("How many examples should be included? ")

prompt = f"""
Explain {topic} to {learner}.

Use very simple English.
Give {examples} examples.
Use bullet points.
Keep the explanation clear and easy to understand.
End with one question to test understanding.
"""

print("\nGenerated Advanced Prompt:")
print(prompt)