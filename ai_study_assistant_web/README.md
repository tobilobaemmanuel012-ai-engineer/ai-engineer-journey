\# StudyWith TAE's AI



\*\*An Interactive Web-Based Learning Assistant\*\*



\## 1. Project Overview



StudyWith TAE's AI is a web application designed to help students learn, practise, and revise academic topics through a simple and interactive interface.



The application allows users to enter a study topic and choose from three learning modes: Explain, Quiz Me, and Summarize.



\## 2. Project Objectives



\- Make learning easier through clear topic explanations.

\- Help students test their understanding through interactive quizzes.

\- Provide revision notes for study and review.

\- Give students immediate quiz scores and correct-answer feedback.

\- Encourage students to keep learning through supportive messages.



\## 3. Main Features



\### Explain

Provides learning explanations for a selected topic.



\### Quiz Me

Presents questions and answer options, calculates the student's score, and displays feedback with the correct answers.



\### Summarize

Provides revision notes for a selected topic.



\### Input Validation

Requires users to enter a topic before submitting the form.



\### Student Feedback

Displays encouraging messages based on quiz performance.



\## 4. Technologies Used



\- Python

\- Flask

\- HTML5

\- CSS3

\- JavaScript

\- Jinja2 templates



\## 5. Project Structure



```text

StudyWith TAE's - AI/



├── app.py

├── templates/

│   └── index.html

├── static/

│   └── style.css

└── README.md

```



Additional project files may be present.



\## 6. How to Run the Application



1\. Install Python 3 if it is not already installed.

2\. Open a terminal in the project directory.

3\. Install Flask if necessary:



&#x20;  `python -m pip install flask`



4\. Start the application:



&#x20;  `python app.py`



5\. Open the local address displayed in the terminal in your web browser. For example, `http://127.0.0.1:5000`, if that is the address shown.



6\. Enter a topic and select a study mode.



\## 7. Testing



The following tests were completed successfully during development:



\- Explain mode with Geology.

\- Quiz mode with Python.

\- Summarize mode with Geology.

\- Empty-topic validation.

\- Testing with a different topic.



Quiz scoring, correct-answer feedback, and student encouragement were also tested.



\## 8. Current Limitations



The quality and range of explanations, summaries, and quiz questions depend on the application's current implementation. Responses may not always be comprehensive or factually complete.



Live AI model integration and any associated API requirements should be confirmed separately before describing the application as powered by a connected AI model.



\## 9. Future Improvements



\- Integrate an AI model for dynamic explanations and summaries.

\- Generate quizzes for a wider range of subjects.

\- Add student accounts and learning progress tracking.

\- Improve accessibility and mobile responsiveness.

\- Expand the question bank and educational feedback.



\## 10. Conclusion



StudyWith TAE's AI demonstrates how Python, Flask, HTML, CSS, and JavaScript can be combined to build an interactive educational web application. It provides a foundation for developing more advanced AI-assisted learning tools.



