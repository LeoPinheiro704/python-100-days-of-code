import random
# import my_module
# print(my_module.pi)

# random_int = random.randint(0, 2)
# print(random_int)
# random_float = random.random() * 5
# print(random_float)
# choice = input('What do you choice? Type 0 for Rock, 1 for paper or 2 for Scissors.')

# states_of_brazil = ["Acre", "Alagoas"]
# print(len(states_of_brazil))

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits[-1])

# texto = 'Teste'
# print(texto[1])

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

jokenpo = [rock, paper, scissors]
user_choice = int(input('What do you choice? Type 0 for Rock, 1 for paper or 2 for Scissors.\n'))
if (user_choice >= 3 or user_choice < 0):
  print('You typed an invalid number, you lose!')
else:
  print(jokenpo[user_choice])
  computer_choice = random.randint(0, 2)
  print(f'Computer chose:\n{jokenpo[computer_choice]}')

  if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print('You win!')
  elif user_choice == computer_choice:
    print('It\'s a draw')
  else:
    print('You lose!')

