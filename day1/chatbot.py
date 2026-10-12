print("Welcome to Tobi's AI Chatbot!")

name = input("What is your name? ")

print("Hello " + name + "!")

question = input("What do you want to ask me? ")

if "money" in question.lower():
    print("Keep learning AI Engineering. Your skills can create opportunities!")

elif "api" in question.lower():
    print("An API allows different software programs to communicate with each other.")

elif "hello" in question.lower():
    print("Hello! Nice to meet you.")

else:
    print("I don't know that yet, but I am still learning!")

print("Thank you for chatting with me, " + name + "!")