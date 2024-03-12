#Data types

# num_char = len(input("what is yout name?"))
# print("your name has " + str(num_char) + " characters.")

# print(round(2.66666, 2))
# print(8 // 6)

# score = 0
# print(f"your score is {score}")

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill = (total + ((total * tip) / 100 )) / people
final_amount = "{:.2f}".format(round(bill, 2))
print(f"Each person should pay: ${final_amount}")

