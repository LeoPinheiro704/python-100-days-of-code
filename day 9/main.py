from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

end_bid = False
bid_list = []

print(logo)
print("Welcome to the secret auction program.")

def get_winner(bids):
  winner_bid = 0
  for bid in bids:
    if winner_bid < bid["value_bid"]:
      winner_bid = bid["value_bid"]
      winner_name = bid["name"]
  print(f"The winner is {winner_name} with a bid of ${winner_bid}.")

while not end_bid:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  bid_list.append({
    "name": name,
    "value_bid": bid
  })
  clear()
  if other_bidders == 'no':
    get_winner(bid_list)
    end_bid = True


