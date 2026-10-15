
print("WELCOME TO TOBI'S AI STUDY ASSISTANT")
print("--------------------------------------")

print("1. Explain a topic")
print("2. Generate a quiz")
print("3. Summarize a topic")

choice = input("Choose an option (1-3): ")
topic = input("Enter the topic you want to study: ")

if choice == "1":
    print(f"\nLet's learn about {topic}!")
    print(f"{topic} is the topic we will study today.")

elif choice == "2":
    print(f"\nLet's create a quiz about {topic}!")
    print(f"Question 1: What do you know about {topic}?")

elif choice == "3":
    print(f"\nLet's summarize {topic}!")
    print(f"Write down the three most important facts about {topic}.")

else:
    print("Invalid choice. Please select 1, 2, or 3.")

print("\nThank you for studying with Tobi's AI Assistant!")
