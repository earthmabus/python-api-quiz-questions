from quiz_brain import QuizBrain
from ui import UI

# create a QuizBrain and load in questions
quiz = QuizBrain()
quiz.load_questions_from_opentdb()

# display the UI to allow the user to play
quiz_ui = UI(quiz)
quiz_ui.loop()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
