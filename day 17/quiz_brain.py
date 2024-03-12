class QuizBrain:
  
  
  def __init__(self, q_list):
    self.q_number = 0
    self.list = q_list
    self.len_quiz = len(self.list)
    self.score = 0


  def still_has_question(self):
    return self.q_number < self.len_quiz


  def next_question(self):
    current_question = self.list[self.q_number]
    self.q_number += 1
    user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ").lower()
    self.check_answer(user_answer, current_question.answer)


  def check_answer(self, user_answer, correct_answer):
    if user_answer == correct_answer.lower():
      self.score += 1
      print("You got it right!")
    else:
      print("You are wrong!")
    print(f"The correct answer was: {correct_answer}")
    print(f"Your current score is: {self.score}/{self.q_number}.")
    print("\n")

  def final_score(self):
    print("You've completed the quiz")
    print(f"Your final score was: {self.score}/{self.q_number}")