# jogo da forca
from os import system
import random
from hangman_art import stages, logo
from hangman_words import word_list

word_choice = random.choice(word_list).lower()
display_list =  []
guess_list = []
lives = 6
end_of_game = False

print(logo)

for _ in range(len(word_choice)):
  display_list.append('_')

def print_visual_game(i):
  display = ''
  for char in display_list:
    display += char + ' '
  print(display)
  print(stages[i])

while not end_of_game:
  guess = input('Guess a letter: ').lower()

  system('cls')

  if guess in display_list:
    print(f'You\'ve already guessed {guess}')

  if guess not in word_choice:
    lives -= 1
    print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
    print_visual_game(lives)
    if lives == 0:
      print('You lose.')
      end_of_game = True
  else:
    for position in range(len(word_choice)):
      if guess == word_choice[position]:
        display_list[position] = word_choice[position]
    
    print_visual_game(lives)
    if '_' not in display_list:
      end_of_game = True
      print('You win.')