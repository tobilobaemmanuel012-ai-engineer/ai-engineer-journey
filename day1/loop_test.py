questions = [
    "What is an API?",
    "What is Python?",
    "What is AI?",
    "I need money"
]

for question in questions:

    if "money" in question.lower():
        print("AI: Keep learning AI Engineering. Your skills can create opportunities!")

    elif "api" in question.lower():
        print("AI: An API allows different software programs to communicate.")

    elif "python" in question.lower():
        print("AI: Python is a programming language.")

    elif "ai" in question.lower():
        print("AI: AI means Artificial Intelligence.")

    else:
        print("AI: I don't know that yet.")
