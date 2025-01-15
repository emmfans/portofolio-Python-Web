from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

print(question_bank)

quiz = Quizbrain(question_bank)
while quiz.checkq():
    quiz.nextq()

print(f"You completed the quiz \nYour final score is :{quiz.score}/{quiz.questionn}")
