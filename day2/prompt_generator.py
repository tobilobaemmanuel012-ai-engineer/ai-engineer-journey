print("PROMPT GENERATOR")
print("----------------")

topic = input("Enter a topic: ")
audience = input("Who are you learning this for? ")

prompt = f"Explain {topic} in very simple English, as if you are teaching {audience}."

print()
print("Generated Prompt:")
print(prompt)