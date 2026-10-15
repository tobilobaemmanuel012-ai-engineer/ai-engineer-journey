
from flask import Flask, render_template, request

app = Flask(__name__)


def explain_topic(topic):
    explanations = {
        "geology": (
            "Geology is the scientific study of the Earth, "
            "including its rocks, minerals, structure, and history.\n\n"
            "Key facts:\n"
            "1. Geologists study rocks and minerals.\n"
            "2. Geology helps us understand earthquakes and volcanoes.\n"
            "3. It supports oil, gas, and mineral exploration.\n\n"
            "Example: A geologist may study rocks to identify "
            "an area that could contain gold."
        ),
        "python": (
            "Python is a programming language used to give "
            "instructions to computers.\n\n"
            "Key facts:\n"
            "1. Python has readable syntax.\n"
            "2. It is used in automation, web development, and AI.\n"
            "3. Python programs use variables, loops, and functions.\n\n"
            "Example: print('Hello, Tobi!') displays a message."
        ),
        "artificial intelligence": (
            "Artificial Intelligence (AI) is a field of computing "
            "that develops systems capable of tasks such as "
            "recognizing patterns and generating language.\n\n"
            "Key facts:\n"
            "1. AI systems can learn patterns from data.\n"
            "2. Different AI systems perform different tasks.\n"
            "3. AI outputs should be checked for accuracy.\n\n"
            "Example: An AI study tool can help explain a topic."
        ),
    }

    return explanations.get(
        topic.lower(),
        f"Study topic: {topic}\n\n"
        "Start by defining the topic, identifying three key facts, "
        "finding a practical example, and reviewing what you learned."
    )


def create_quiz(topic):
    quizzes = {
        "geology": [
            {
                "question": "What does geology study?",
                "options": [
                    "The Earth and its materials",
                    "The human brain",
                    "The solar system only",
                    "Computer programming"
                ],
                "answer": 0
            },
            {
                "question": "Which of these is a rock?",
                "options": [
                    "Oxygen",
                    "Granite",
                    "Electricity",
                    "Plastic"
                ],
                "answer": 1
            },
            {
                "question": "Which professional studies rocks?",
                "options": [
                    "Geologist",
                    "Dentist",
                    "Accountant",
                    "Chef"
                ],
                "answer": 0
            }
        ],
        "python": [
            {
                "question": "What is Python?",
                "options": [
                    "A programming language",
                    "A web browser",
                    "A keyboard",
                    "An operating system only"
                ],
                "answer": 0
            },
            {
                "question": "Which command displays a message in Python?",
                "options": [
                    "show()",
                    "display_text()",
                    "print()",
                    "message()"
                ],
                "answer": 2
            },
            {
                "question": "Which symbol starts a comment in Python?",
                "options": [
                    "//",
                    "#",
                    "<!--",
                    "**"
                ],
                "answer": 1
            }
        ]
    }

    return quizzes.get(topic.lower())


def create_summary(topic):
    summaries = {
        "geology": (
            "REVISION NOTES: GEOLOGY\n\n"
            "Definition:\n"
            "Geology is the scientific study of the Earth, "
            "its rocks, minerals, structure, and history.\n\n"
            "Three Key Points:\n"
            "1. Rocks are made of one or more minerals.\n"
            "2. The three major rock types are igneous, "
            "sedimentary, and metamorphic.\n"
            "3. Geology supports mineral exploration, "
            "engineering, and oil and gas exploration.\n\n"
            "Practical Example:\n"
            "A geologist examines rock samples to identify "
            "minerals and understand how the rocks formed.\n\n"
            "Quick Review:\n"
            "Can you name the three major rock types?"
        ),
        "python": (
            "REVISION NOTES: PYTHON\n\n"
            "Definition:\n"
            "Python is a programming language used to build "
            "software, automate tasks, and develop AI applications.\n\n"
            "Three Key Points:\n"
            "1. Variables store values.\n"
            "2. Loops repeat instructions.\n"
            "3. Functions organise reusable blocks of code.\n\n"
            "Practical Example:\n"
            "The command print('Hello, Tobi!') displays a message.\n\n"
            "Quick Review:\n"
            "What is the difference between a variable and a function?"
        ),
        "artificial intelligence": (
            "REVISION NOTES: ARTIFICIAL INTELLIGENCE\n\n"
            "Definition:\n"
            "Artificial Intelligence (AI) is a field of computing "
            "that develops systems capable of tasks such as "
            "recognising patterns and generating language.\n\n"
            "Three Key Points:\n"
            "1. Machine learning can identify patterns in data.\n"
            "2. AI is used in education, healthcare, and engineering.\n"
            "3. AI outputs can contain errors and need verification.\n\n"
            "Practical Example:\n"
            "A study assistant can help learners practise questions "
            "and review educational material.\n\n"
            "Quick Review:\n"
            "Why should users verify information produced by AI?"
        )
    }

    return summaries.get(
        topic.strip().lower(),
        f"REVISION NOTES: {topic}\n\n"
        "1. Definition: Write a clear definition of the topic.\n"
        "2. Key Points: Identify three important facts.\n"
        "3. Example: Describe a practical application.\n"
        "4. Review: Write three questions to test your understanding."
    )


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    topic = ""
    action = "explain"
    questions = None

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        action = request.form.get("action", "explain")

        if not topic:
            result = "Please enter a topic first."

        elif len(topic) > 150:
            result = "Please keep your topic under 150 characters."

        elif action == "explain":
            result = explain_topic(topic)

        elif action == "quiz":
            questions = create_quiz(topic)

            if questions is None:
                result = (
                    f"No interactive quiz is available for {topic} yet.\n\n"
                    "Try Geology or Python for now."
                )

        elif action == "summarize":
            result = create_summary(topic)

        else:
            result = "Please select a valid study mode."

    return render_template(
        "index.html",
        result=result,
        topic=topic,
        action=action,
        questions=questions
    )


if __name__ == "__main__":
    app.run(debug=False)
