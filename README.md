# Quizzler - Python UI Quiz Game

Quizzler is a simple interactive True/False quiz game built with Python and Tkinter, powered by questions fetched from the Open Trivia Database API. The game features a graphical interface with real-time score tracking, visual feedback, and modular design following object-oriented programming principles.

##Features

+ Fetches 10 random True/False trivia questions from the Open Trivia DB API.
+ Graphical UI built with Tkinter for an engaging user experience.
+ Dynamic score tracking displayed in the interface.
+ Visual feedback: canvas turns green/red depending on the correctness of your answer.
+ Disables buttons and shows a message when the quiz ends.
+ Organized into multiple modules for clarity and scalability:
<br> + data.py → API handling
<br>question_model.py → Question class
<br>quiz_brain.py → Quiz logic (score, next question, answer check)
<br>ui.py → Tkinter interface
<br>main.py → Entry point
