print("TOBI'S MINI AI ASSISTANT")
print("------------------------")

role = input("What should the AI act as? ")
question = input("Ask your question: ")

system_prompt = f"""
You are a helpful {role}.
Give simple, clear, and accurate answers.
"""

user_prompt = question

print("\n--- AI INSTRUCTIONS ---")
print(system_prompt)

print("--- USER QUESTION ---")
print(user_prompt)

print("\n--- AI ASSISTANT ---")
print("Your AI assistant is ready to answer!")