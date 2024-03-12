from replit import clear
from art import logo
import random


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def get_score(hand):
  return sum(hand)

def blackjack_hand(hand):
  score = get_score(hand)
  if score == 21:
    return True
  else:
    return False

def have_ace(hand):
  for card in hand:
    index = 0
    if card == 11:
      return True
    index += 1
  return False

def change_ace(hand):
  index = 0
  for card in hand:
    if card == 11:
      hand[index] = 1
    index += 1
  return hand

print(logo)
print('Welcome to BlackJack game.')

end_game = False
user_cards = []
computer_cards = []
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
user_score = get_score(user_cards)
computer_score = get_score(computer_cards)

print(f"Your hand:  {user_cards}")
print(f"Computer card: {computer_cards[0]}")

if computer_score == 21:
  print("Computer wins!")
  end_game = True
elif user_score == 21:
  print("You wins!")
  end_game = True
else:
  while not end_game:
    if user_score > 21:
      if have_ace(user_cards):
        user_cards = change_ace(user_cards)
        user_score = get_score(user_cards)
      else:
        print("You Lose!")
        end_game = True
    else:
      another_card = input("Do you want another card? Type 'y' to card or 'no' to compare hands\n").lower()
      if another_card == 'y':
        user_cards.append(deal_card())
        user_score = get_score(user_cards)
        print(f"Your hand:  {user_cards}")
      else:
        while computer_score < 17:
          computer_cards.append(deal_card())
          computer_score = get_score(computer_cards)
        print(f"Your hand:  {user_cards}")
        print(f"Your score: {user_score}")
        print(f"Computer hands:  {computer_cards}")
        print(f"Computer score: {computer_score}")
        if computer_score > 21:
          print("You wins!")
          end_game = True
        else:
          if user_score == computer_score:
            print("You Draw!")
            end_game = True
          elif user_score > computer_score:
            print("You win!")
            end_game = True
          else:
            print("You Lose!")
            end_game = True
