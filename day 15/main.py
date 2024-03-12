from coffee_data import MENU, resources


end_coffee_machine = False
money = 0


def calculate_coins():
  """Calcula o valor recebido do usuário"""
  print("Please insert coins.")
  total = 0
  total += int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.10
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total


def calculate_change(paid, cost):
  """Calcula o troco, mostra para o usuário o valor e soma ao valor do dinheiro dentro da máquina de café"""
  global money
  if paid > cost:
    change = round(paid - cost, 2)
    money += cost
    print(f"Here is ${change} in change.")
  else:
    money += paid


def report():
  """Mostra para o usuário o reporte de recursos disponíveis"""
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${money}")


def have_resources(order_ingredients, order):
  """Verifica se tem recursos suficientes para realizar o pedido"""
  for ingredient in resources:
    if not (order == 'espresso' and ingredient == 'milk'):
      if resources[ingredient] < order_ingredients[ingredient]:
        print(f"Sorry there is not enough {ingredient}")
        return False
  return True


def reduce_resources(order_ingredients, order):
  """Função para reduzir os recursos da máquina"""
  for ingredient in resources:
      if not (order == 'espresso' and ingredient == 'milk'):
        resources[ingredient] -= order_ingredients[ingredient]


def play_coffee_machine():
  global end_coffee_machine
  order = input("What would you like? (espresso/latte/cappuccino) ").lower()
  if order == "report":
    report()
  elif order in MENU:
    ingredients = MENU[order]["ingredients"]
    cost = MENU[order]["cost"]
    if have_resources(ingredients, order):
      paid = calculate_coins()
      if paid >= cost:
        reduce_resources(ingredients, order)
        calculate_change(paid, cost)
        print(f"Here is your {order} ☕ Enjoy!")
      else:
        print("Sorry that's not enough money. Money refunded.")
  elif order == "off":
    end_coffee_machine = True
  else:    
    print("Don't understand the order. Please, order again.")


while not end_coffee_machine:
  play_coffee_machine()