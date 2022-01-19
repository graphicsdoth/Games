from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cntd = 1
c= CoffeeMaker()
mon = MoneyMachine()
me = Menu()
while(cntd==1):
    options = me.get_items()
    user_choice = input(f"What would you like? {options}:")
    if user_choice == "off":
        cntd=0
        break
    elif user_choice == "report":
        c.report()
        mon.report()
    else:
        drink = me.find_drink(user_choice)
        if c.is_resource_sufficient(drink) and mon.make_payment(drink.cost) :
                c.make_coffee(drink)








