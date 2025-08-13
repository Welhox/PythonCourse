from warnings import catch_warnings

# TODO test the todo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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
    "money": 0,
}

def report():
    print(f"Water: {resources["water"]}ml\nMilk: "
          f"{resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]:.2f}")

def checkResources(key):
    coffee = MENU[key]["ingredients"]
    if resources["water"] < coffee["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < coffee["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if resources["coffee"] < coffee["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True

def takePayment(key):
    try:
        total = 0
        inserted = 0.25 * int(input("Insert quarters: "))
        total += inserted
        inserted = 0.1 * int(input("Insert dimes: "))
        total += inserted
        inserted = 0.05 * int(input("Insert nickel: "))
        total += inserted
        inserted = 0.01 * int(input("Insert pennies: "))
        total += inserted
        if total < MENU[key]["cost"]:
            print(f"Sorry that's not enough money. ${total:.2f} refunded")
            return False
        else:
            resources["money"] += MENU[key]["cost"]
            total -= MENU[key]["cost"]
            if total != 0:
                print(f"Here is ${total:.2f} in change")
            return True
    except Exception as e:
        print("invalid input")
        return False

machineOn = True
commands = ["espresso", "latte", "cappuccino", "off", "report"]

def useResources(key):
    coffee = MENU[key]["ingredients"]
    resources["water"] -= coffee["water"]
    resources["milk"] -= coffee["milk"]
    resources["coffee"] -= coffee["coffee"]
    print(f"Here is your {key}, Enjoy!")

while machineOn:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice not in commands:
        print("invalid input")
        continue
    if choice == "off":
        break
    if choice == "report":
        report()
    else:
        if checkResources(choice):
            if takePayment(choice):
                useResources(choice)
            else:
                continue
        else:
            continue
