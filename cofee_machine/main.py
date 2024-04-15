from assets import MENU, resources
profit = 0
is_on = True

def is_resource_sufficient(order_ingredients):
    is_enough = True

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False

    return is_enough


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    total += int(input("How many dimes?: ")) * 0.1

    return total


def is_transaction_succesful(money_received, drink_cot):
    if money_received >= drink_cot:
        global profit
        profit += drink_cot
        change = round(money_received - drink_cot, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry tha's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


while is_on:
    choice = input("What would you like to order? (express, latte, cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice =="report":
        for item in resources:
            print(f"{item}: {resources[item]}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()

            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee()
    