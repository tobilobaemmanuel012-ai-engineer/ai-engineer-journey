print("AI PROMPT ROLES")
print("----------------")

role = input("What role should the AI act as? ")
question = input("What should the AI answer? ")

system_prompt = f"You are a {role}. Give clear and helpful answers."

user_prompt = question

print("\nSYSTEM PROMPT:")
print(system_prompt)

print("\nUSER PROMPT:")
print(user_prompt)