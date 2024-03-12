from art import logo, vs
from game_data import data
import random
from replit import clear

selected_accounts = []

def get_description(account):
  """Returns formatted text about the account"""
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description}, from {country} followers {account['follower_count']} "

def account_options(accounts):
  """Prints the options for choosing the two comparison accounts"""
  print(f"Compare A: {get_description(accounts[0])}")
  print(vs)
  print(f"Against B: {get_description(accounts[1])}")
  return input("Who has more followers? Type 'A' or 'B': ").lower()


def end_accounts():
  global selected_accounts
  if len(data) == len(selected_accounts):
    return True
  else:
    return False

def change_position(accounts):
  """Change the order of accounts in the list and check if the next account has not already appeared in the previous choices"""
  accounts[0] = accounts[1]
  global selected_accounts
  repeated = True
  while repeated:
    account = random.choice(data)
    if account not in selected_accounts:
      selected_accounts.append(account)
      accounts[1] = account
      repeated = False
  return accounts

def check_won(guess, accounts):
  """Check the chosen option and return if the account choice was correct"""
  if guess == 'a':
    return accounts[0]['follower_count'] > accounts[1]['follower_count']
  else:
    return accounts[1]['follower_count'] > accounts[0]['follower_count']

def play_game():
  score = 0
  end_game = False
  accounts = []
  for _ in range(2):
    account = random.choice(data)
    accounts.append(account)
    selected_accounts.append(account)
  while not end_game:
    clear()
    print(logo)
    if score > 0:
      print(f"You right. Your current score is {score}")
    guess = account_options(accounts)
    if check_won(guess, accounts):
      score += 1
      if end_accounts():
        print(f"You win. Your score is {score}.")
        end_game = True
      else:
        accounts = change_position(accounts)
    else:
      print(f"You lose. Final score is {score}.")
      end_game = True


play_game()

