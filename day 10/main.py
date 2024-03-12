#Calculator
from art import logo
from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  clear()
  print(logo)
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  end_operation = False

  while not end_operation:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calc = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {calc}")

    continue_operation = input(f"Type 'y' to continue calculation with {calc}, or type 'n' to start a new calculation.: ").lower()
    if continue_operation != 'y':
      end_operation = True
      calculator()
    else:
      num1 = calc

calculator()