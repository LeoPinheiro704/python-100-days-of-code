#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random

end_game = False

def initialize_variables():
  """Inicializa as variáveis para recomeçar o jogo novamente. """
  global guess, number_list, number_choice, guessed, end_game
  guess = 0
  number_choice = random.randint(1, 100)
  guessed = False
  end_game = False

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == 'easy':
    return 10
  else: 
    return 5

def check_answer(guess, attempts):
  global guessed
  if guess == number_choice:
    guessed = True
    return
  elif guess > number_choice:
    print("Too high.")
  elif guess < number_choice:
    print("Too low.")
  if attempts > 1:
    print("Guess again.")


def game():
  global end_game, guessed
  while not end_game:
    initialize_variables()

    print(logo)
    print("I'm thinking of a number between 1 and 100")
    attempts = set_difficulty()
    while not guessed and not attempts == 0:
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      check_answer(guess, attempts)
      attempts -= 1
    if guessed:
      print(f"You got it! The answer was {number_choice}.")
    elif attempts == 0:
      print("You've run out of guesses, you lose.")
    
    start_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if start_again == 'y':
      clear()
    else:
      end_game = True

game()