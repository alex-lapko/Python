from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = Question(question["text"], question["answer"])
    question_bank.append(question_text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You got {quiz.score}/{len(question_bank)} questions right.")
