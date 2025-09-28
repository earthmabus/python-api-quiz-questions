from question_model import Question
from quiz_brain import QuizBrain
from ui import UI
import requests

def get_questions_from_opentdb():
    parameters = {}
    parameters['amount'] = 10
    parameters['type'] = "boolean"
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    questions = response.json()['results']
    return questions

question_data = get_questions_from_opentdb()

# convert question_data into a format that works for our QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create a QuizBrain to hold all the quiz questions
quiz = QuizBrain(question_bank)

quiz_ui = UI()
quiz_ui.loop()

#while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
