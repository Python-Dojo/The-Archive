# Task

Build a simple multiple-choice quiz application that fetches questions from an external API, asks the user a series of questions, validates their answers, and keeps a running score.

This folder contains a Python prototype from the 2024-10-02 Bristol Python Dojo session. The project is intentionally simple and focused on a small, clear workflow: load questions, display them to the user, accept an answer, and update the score.

## What the program does

The script in `Group-1/main.py` is a quiz engine built around two core classes:

- `Question`: represents one quiz question and its possible answers
- `Quiz`: manages a list of questions and handles the quiz flow

The `Question` dataclass stores:

- the question text
- the incorrect answers
- the correct answer

It also includes a method to verify whether a user's answer is correct:

```python
def verify_answer(self, answer: str) -> bool:
    return answer.lower() == self.correct_answer.lower()
```

The `answers` property then combines the correct answer with the incorrect answers, shuffles them, and returns a randomised answer list for display.

The `Quiz` class has a method called `load_quiz()` that calls the OpenTDB API:

```python
response = requests.get("https://opentdb.com/api.php", params=params).json()
return Quiz([Question.from_dict(item) for item in response["results"]])
```

This fetches a batch of quiz questions, converts each result into a `Question`, and stores them in the quiz.

## Main concept

The main concept is a lightweight quiz loop built around structured question objects and API-based data loading.

The flow is straightforward:

1. fetch a set of questions from the API
2. store them as `Question` objects
3. display one question at a time
4. print the shuffled answers
5. ask the user to choose an answer
6. compare the answer against the correct answer
7. update the score
8. continue until all questions are answered

This pattern is a simple but practical demonstration of how to combine:

- external data fetching
- object-oriented data modelling
- user input handling
- repeated iterative loops
- score tracking

The output is therefore not just a list of question data; it is a working interactive quiz experience.

## The output of the program

When you run the script, the program prints a question, shows all answer options in random order, waits for user input, and then reports whether the answer was correct.

At the end of the quiz, it prints a final result such as:

```python
print(f"Congratulations, you finished the quiz, final score: {self.score}/10")
```

This gives a clean, immediate user-facing result and makes the script a complete interactive toy application rather than just a data-fetching prototype.

## Design choices in the code

The choice to use `dataclasses` is especially important because it gives the code a clear structure:

```python
@dataclass
class Question:
    question: str
    incorrect_answers: list[str]
    correct_answer: str
```

This keeps each question as a small, self-contained object with a predictable interface.

The `from_dict` classmethod also handles the conversion from API JSON into a Python object, which is a very common and useful pattern when working with web APIs.

The `Quiz.display()` method handles the core event loop for each question and keeps the logic in one place. It prints the question, asks for an answer, validates it, and updates the score.

## Summary

This project is a simple quiz application that fetches questions from OpenTDB, converts them into structured objects, and runs an interactive question loop. The code is intentionally small and easy to follow, which makes it a good example of a lightweight data-driven application.

The program's value is in its clarity: it shows how a real-world JSON API can be wrapped in a clean Python model, then turned into a user-facing game loop with a score counter. The script is a practical and well-scoped example of how to build a mini app from external data without a large framework.

It is not a full production quiz system, but it is a complete working prototype for the task: fetch questions, ask them, check answers, and report the final score.
