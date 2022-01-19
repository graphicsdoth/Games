MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Todo 2. - Check if the resources are sufficient for a given drink
def check_resources(type1, water, milk, coffee):
    if MENU[type1]["ingredients"]["water"] <= water and MENU[type1]["ingredients"]["milk"] <= milk and \
            MENU[type1]["ingredients"]["coffee"] <= coffee:
        return 1
    else:
        if MENU[type1]["ingredients"]["water"] > water:
            return "water"
        elif MENU[type1]["ingredients"]["milk"] > milk:
            return "milk"
        else:
            return "coffee"


def print_cost(type1):
    return MENU[type1]["cost"]


def update_resources(type1, water, milk, coffee, money):
    water = water - MENU[type1]["ingredients"]["water"]
    milk = milk - MENU[type1]["ingredients"]["milk"]
    coffee = coffee - MENU[type1]["ingredients"]["coffee"]
    moneyf = money + MENU[type1]["cost"]
    return water, milk, coffee, moneyf


def cal_change(type1, quarter, dime, nickel, penny):
    cents = (quarter * 25) + (dime * 10) + (nickel * 5) + penny
    final = round(5555 / 100, 2)
    cost = MENU[type1]["cost"]
    change = round((final - cost), 2)
    if final >= cost:
        return change
    else:
        return 0


# ToDo 1.print report of coffee machine resources left in the machine and money accumulated so far
def print_report(water, milk, coffee, money):
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
again = 1
while again == 1:
    # ToDo 3 - Ask the user what would you like (espresso/latte/cappuccino)
    u_choice = input("What would you like? (espresso/latte/cappuccino):")
    if u_choice == "off":
        again = 0
    elif u_choice == "report":
        print_report(water, milk, coffee, money)
    else:
        # ToDo 4 - Ask the user to insert the coins - Quarters/dimes/nickles/pennies
        # Reference : Quarter - 25 cents ; Dimes 10 cents ; Nickel 5 cents ; Pennies 1 cents
        print(f"To order {u_choice}, given $", print_cost(u_choice), ".If moree money is given then the change will be returned.")
        print("Please Insert the coins")
        quarter = int(input("How many Quarters? "))
        dime = int(input("How many Dimes? "))
        nickel = int(input("How many Nickel? "))
        penny = int(input("How many Pennies? "))
        c = cal_change(u_choice, quarter, dime, nickel, penny)
        if c >= 0:
            if check_resources(u_choice, water, milk, coffee) == 1:
                print(f"Report before purchasing {u_choice}")
                print_report(water, milk, coffee, money)
                water1, milk1, coffee1, money1 = update_resources(u_choice, water, milk, coffee, money)
                # ToDo 5 - Here is the change. Here is coffee name. Enjoy!
                print(f"Here is the change {c}. Here is {u_choice}. Enjoy!")
                water = water1
                milk = milk1
                coffee = coffee1
                money = money1
                print(f"Report after purchasing {u_choice}")
                print_report(water, milk, coffee, money)
            else:
                resource = check_resources(u_choice, water, milk, coffee)
                print(f"Sorry, there is not enough {resource}.")
        else:
            print("Sorry, that's not enough money. Money Refunded.")

# ToDo 6 - What would you like (ask again and again)
