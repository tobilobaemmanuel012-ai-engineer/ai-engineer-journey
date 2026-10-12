
def ask_ai(question):
    topic = question.lower()

    if "artificial intelligence" in topic or topic == "ai":
        return "Artificial Intelligence (AI) is the ability of computers to perform tasks that normally require human intelligence."

    elif "python" in topic:
        return "Python is a programming language used to build software, automate tasks, and create AI applications."

    elif "api" in topic:
        return "An API is a way for two software applications to communicate with each other."

    elif "llm" in topic:
        return "LLM means Large Language Model. It is an AI model trained on large amounts of text to understand and generate language."

    else:
        return "I do not have a prepared explanation for that topic yet. Try AI, Python, API, or LLM."


print("================================")
print("       STUDY ASSISTANT")
print("================================")

question = input("What topic do you want to learn today? ")

answer = ask_ai(question)

print("\nYour explanation:")
print(answer)