from __future__ import annotations
"""
Quiz App

- Function that makes API calls to fetch quiz question
https://opentdb.com/api_config.php 

- Function that converts a response to a list of questions 
- function that allows user to pick an answer / validates it?
- score counter
- Loop that runs through the questions (mainloop)
- API link https://opentdb.com/api.php?amount=50&category=19&difficulty=medium&type=multiple


-- You can validate this with Pydantic
Example response
    {
      "type": "multiple",
      "difficulty": "medium",
      "category": "Sports",
      "question": "Who was the British professional wrestler Shirley Crabtree better known as?",
      "correct_answer": "Big Daddy",
      "incorrect_answers": [
        "Giant Haystacks",
        "Kendo Nagasaki",
        "Masambula"
      ]
    },
"""

import requests
import random
from dataclasses import dataclass


@dataclass
class Question:
    question: str
    incorrect_answers: list[str]
    correct_answer: str

    @classmethod
    def from_dict(cls, data: dict[str, str | list[str]]) -> Question:
        return cls(
            question=data["question"],
            incorrect_answers=data["incorrect_answers"],
            correct_answer=data["correct_answer"]
        )

    def verify_answer(self, answer: str) -> bool:
        """return if answer is the correct one"""
        return answer.lower() == self.correct_answer.lower()

    @property
    def answers(self):
        all_answers = [self.correct_answer, *self.incorrect_answers]
        random.shuffle(all_answers)
        return all_answers


class Quiz:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.score = 0

    @classmethod
    def load_quiz(cls) -> Quiz:
        params = {
            "category": 11,
            "difficulty": "easy",
            "type": "multiple",
            "amount": 10
        }
        response = requests.get("https://opentdb.com/api.php", params=params).json()
        return Quiz([Question.from_dict(item) for item in response["results"]])

    def run(self) -> None:
        for q in self.questions:
            self.display(q)
        print(f"Congratulations, you finished the quiz, final score: {self.score}/10")

    def display(self, q: Question):
        print(q.question)
        for answer in q.answers:
            print(answer)

        answer = input("Please select answer:")

        if q.verify_answer(answer):
            self.score += 1 
            print(f"\nCorrect! current score {self.score}\n")
        else:
            print("\nIncorrect answer\n")

quiz = Quiz.load_quiz()
quiz.run()
