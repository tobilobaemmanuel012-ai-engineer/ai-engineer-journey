def answer_question(question):

    if "money" in question.lower():
        return "Keep learning AI Engineering. Your skills can create opportunities!"

    elif "api" in question.lower():
        return "An API allows different software programs to communicate."

    elif "python" in question.lower():
        return "Python is a programming language."

    elif "ai" in question.lower():
        return "AI means Artificial Intelligence."

    else:
        return "I don't know that yet, but I'm still learning."


question = input("Ask me a question: ")

answer = answer_question(question)

print("AI:", answer)