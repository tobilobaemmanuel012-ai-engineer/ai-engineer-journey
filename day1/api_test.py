import requests

task_number = input("Enter a task number (1-10): ")

url = f"https://jsonplaceholder.typicode.com/todos/{task_number}"

response = requests.get(url)

data = response.json()

print("Task:", data["title"])

if data["completed"]:
    print("Status: Completed")
else:
    print("Status: Not completed")