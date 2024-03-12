from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random


question_bank = []
for q in question_data:
  question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

quiz.final_score()