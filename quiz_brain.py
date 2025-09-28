from question_model import Question

import html
import requests

class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = None
        self.current_question = None

    def load_questions_from_opentdb(self):
        parameters = {}
        parameters['amount'] = 3
        parameters['type'] = "boolean"
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()

        # convert question_data into a format that works for our QuizBrain
        question_bank = []
        for question in response.json()['results']:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)

        self.question_list = question_bank

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = html.unescape(self.current_question.text)
        return self.current_question

    def check_answer(self, user_answer):
        retval = False
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True

        return retval
