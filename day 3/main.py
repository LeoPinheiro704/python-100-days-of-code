
# print('Welcome to the rollercoaster!')
# height = int(input('What is your height in cm? '))
# bill = 0

# if height >= 120:
#   print('you can ride the rollercoaster!')
#   age = int(input('What is your age? '))
#   if age < 12:
#     bill = 5
#     print('Child tickets are $5.')
#   elif age <= 18:
#     bill = 7
#     print('Youth tickets are $7.')
#   elif age >= 45 and age <= 55:
#     print('You have free tickets!')
#   else:
#     bill = 12
#     print('Adult tickets are $12.')

#   wants_photos = input("Do you want a photo taken? Y or N. ")
#   if wants_photos == 'Y':
#     bill += 3
  
#   print(f'Your final bill is ${bill}')
# else:
#   print('you cannot ride the rollercoaster!')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print('Welcome to Treasure Island. Your mission is to find the treasure.')
direction = input('left or right? ').lower()
if direction == 'left':
  action = input('swim or wait? ').lower()
  if action == 'wait':
    door_color = input('which door? Blue, red or yellow? ').lower()
    if door_color == 'blue':
      print('Eaten by beasts. Game Over.')
    elif door_color == 'red':
      print('Burned by fire. Game Over.')
    elif door_color == 'yellow':
      print('You Win!')
    else:
      print('Game Over.')
  else:
    print('Attacked by trout. Game Over.')
else: 
  print('Fall into a hole. Game Over.')