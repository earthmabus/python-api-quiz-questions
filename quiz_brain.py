from question_model import Question

import html
import requests

NUM_QUESTIONS_TO_LOAD = 5

class QuizBrain:

    def __init__(self):
        self.reset()

    def reset(self):
        self.question_number = 0
        self.score = 0
        self.question_list = None
        self.current_question = None
        self.question_list = []

    def load_questions_from_opentdb(self):
        parameters = {'amount': NUM_QUESTIONS_TO_LOAD, 'type': "boolean"}
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()

        # convert each question json from the api into a Question object
        self.question_list = []
        for question in response.json()['results']:
            new_question = Question(question["question"], question["correct_answer"])
            self.question_list.append(new_question)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = f"Q{self.question_number}: {html.unescape(self.current_question.text)}"
        return self.current_question

    def check_answer(self, user_answer):
        retval = False
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True

        return retval
