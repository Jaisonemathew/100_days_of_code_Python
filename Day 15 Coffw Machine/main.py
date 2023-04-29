from data import MENU, resources

profit=0


def calculate(user):
    penny = float(input("How many pennies do you have:"))
    quarters = float(input("How many quarters:"))
    nickles = float(input("How many nickles:"))
    dimes = float(input("How many dimes:"))
    value = (0.01 * penny) + (0.05 * nickles) + (0.10 * dimes) + (0.25 * quarters)
    if value < MENU[user]["cost"]:
        return 0
    else:
        balance = value - MENU[user]["cost"]
        round_balance=round(balance, 2)
        print(f"Here is your balance ${round_balance}")
        global profit
        profit = profit + MENU[user]["cost"]


def coffee(user):
    if user == "espresso":
        if (resources["water"] - 50) <= 0 or (resources["coffee"] - 18) <= 0:
            print("You have not enough resources in machine")
            return 0
        else:
            check = calculate(user)
            if check == 0:
                print("Oops it's not enough Money refunded!!")
                return 0
            else:
                resources["water"] = resources["water"] - 50
                resources["coffee"] = resources["coffee"] - 18
                print("Enjoy☕ your Espresso ")

    elif user == "latte":
        if (resources["water"] - 200) <= 0 or (resources["coffee"] - 24) <= 0 or (resources["milk"] - 150) < 0:
            print("You have not enough resources in machine")
            return
        else:
            check = calculate(user)
            if check == 0:
                print("Oops it's not enough Money refunded!!")
                return 0
            else:
                resources["water"] = resources["water"] - 200
                resources["coffee"] = resources["coffee"] - 24
                resources["milk"] = resources["milk"] - 150
                print("Enjoy your Latte🍵 ")

    elif user == "cappuccino":
        if (resources["water"] - 250) <= 0 or (resources["coffee"] - 24) <= 0 or (resources["milk"] - 100) <= 0:
            print("You have not enough resources in machine")
            return
        else:
            check = calculate(user)
            if check == 0:
                print("Oops it's not enough Money refunded!!")
                return 0
            else:
                resources["water"] = resources["water"] - 250
                resources["coffee"] = resources["coffee"] - 24
                resources["milk"] = resources["milk"] - 100
                print("Enjoy your Cappuccino🍵 ")


def machine():
    user = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user == "report":
        print(resources)
        print(f"Profit: {profit}")
        machine()
    elif user == "off":
        return
    elif user == "espresso" or user == "latte" or user == "cappuccino":
        coffee(user)
        machine()


machine()
