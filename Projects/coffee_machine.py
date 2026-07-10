# Coffee machine
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 80,
    },
    "cappuccino": {
        "ingredients": {
            "water": 80,
            "coffee": 70,
            "milk": 100,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 80,
            "coffee": 70,
            "milk": 100,
        },
        "cost": 120,
    },
}

resources = {
    "water": 500,
    "coffee": 200,
    "milk": 400,
}

money = 0


def check_resources(drink):
    for item, needed in menu[drink]["ingredients"].items():
        if resources[item] < needed:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_payment(drink):
    cost = menu[drink]["cost"]
    print(f"The cost of {drink} is {cost}.")
    paid = int(input("Insert coins: "))
    if paid >= cost:
        print(f"Here is your {drink} ☕")
        return paid - cost
    else:
        print("Not enough money. Refund issued.")
        return 0


while True:
    choice = input("Enter what do you want (espresso/cappuccino/latte) or 'off' to exit: ").lower()

    if choice == "off":
        print("Machine turned off.")
        break

    if choice not in menu:
        print("Invalid drink choice.")
        continue

    if check_resources(choice):
        change = process_payment(choice)
        if change > 0:
            print(f"Change returned: {change}")

        for item, needed in menu[choice]["ingredients"].items():
            resources[item] -= needed

        money += menu[choice]["cost"]
        print(f"Money in machine: {money}")
