from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
end_coffee_machine = False


while not end_coffee_machine:
  order = input(f"What would you like? ({menu.get_items()}) ").lower()
  if order == "report":
    coffee_maker.report()
    money_machine.report()
  elif order == "off":
    end_coffee_machine = True
  elif not (menu.find_drink(order) == None):
    menu_item = menu.find_drink(order)
    if coffee_maker.is_resource_sufficient(menu_item):
      if money_machine.make_payment(menu_item.cost):
        coffee_maker.make_coffee(menu_item)
