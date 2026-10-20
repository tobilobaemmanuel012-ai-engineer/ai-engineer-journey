
# DAY 6: STUDY SESSION REPORT

study_sessions = [
    {"topic": "Geology", "mode": "Explain"},
    {"topic": "Python", "mode": "Quiz"},
    {"topic": "Geology", "mode": "Summarize"},
    {"topic": "Artificial Intelligence", "mode": "Explain"},
    {"topic": "Python", "mode": "Explain"},
    {"topic": "Machine Learning", "mode": "Quiz"}
]


def count_sessions(sessions):
    return len(sessions)


def count_by_topic(sessions):
    topic_counts = {}

    for session in sessions:
        topic = session["topic"]

        if topic in topic_counts:
            topic_counts[topic] += 1
        else:
            topic_counts[topic] = 1

    return topic_counts


def show_report(sessions):
    print("STUDYWITH TAE'S AI")
    print("STUDY SESSION REPORT")
    print("-" * 30)

    print("Total sessions:", count_sessions(sessions))
    print("\nSessions by topic:")

    results = count_by_topic(sessions)

    for topic, total in results.items():
        print(f"{topic}: {total}")

    print("\nSessions by mode:")

    mode_counts = {}

    for session in sessions:
        mode = session["mode"]

        if mode in mode_counts:
            mode_counts[mode] += 1
        else:
            mode_counts[mode] = 1

    for mode, total in mode_counts.items():
        print(f"{mode}: {total}")


show_report(study_sessions)
