# quiz.py

import random


class Quiz:
    def __init__(self, subject):
        self.subject = subject
        self.questions = []
        self.score = 0

    def add_question(self, question, options, correct_answer):
        """Adds a new question to the quiz."""
        self.questions.append({
            "question": question,
            "options": options,
            "correct": correct_answer
        })

    def shuffle_questions(self):
        """Randomizes the order of questions."""
        random.shuffle(self.questions)

    def take_quiz(self):
        """Starts the quiz and records the score."""
        self.shuffle_questions()
        self.score = 0

        for i, q in enumerate(self.questions, start=1):
            print(f"Q{i}: {q['question']}")
            if isinstance(q["options"], list):  # Multiple-choice question
                random.shuffle(q["options"])
                for j, option in enumerate(q["options"], start=1):
                    print(f"{j}. {option}")
                answer = input("Enter the number of your answer: ")
                if q["options"][int(answer) - 1] == q["correct"]:
                    self.score += 1
            else:  # Fill-in-the-blank or True/False
                answer = input("Your answer: ")
                if answer.lower() == q["correct"].lower():
                    self.score += 1

        print(f"Quiz Complete! Your final score: {self.score}/{len(self.questions)}")

    def get_score(self):
        """Returns the final score."""
        return self.score
