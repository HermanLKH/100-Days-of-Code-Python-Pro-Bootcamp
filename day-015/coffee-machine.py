# TODO DONE 1. prompt user to decide what to do next
# TODO DONE 2. admin actions - report, off
# TODO DONE 3. customer actions - 4 drinks
# TODO DONE 4. check resources sufficient to make a drink
# TODO DONE 5. prompt user to insert coins
# TODO DONE 6. check monetary value of coins is enough to purchase the drink
# TODO DONE 7. deduct resources, add money and calculate changes
# TODO DONE 8. print success message and changes returned
# TODO DONE 9. loop over the whole process

import winsound

coffee_machine_sound = "day-015\Espresso-Machine-Jet-Out-Hot-Water-into-Metal-Cup.wav"
cash_register_sound = "day-015\Cash Register (Kaching) - Sound Effect.wav"
process_complete_sound = "day-015\Elevator Bell Ring Sound.wav"

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 800,
    "milk": 400,
    "coffee": 200,
    "money": 0
}


def is_resources_sufficient(drink_ingredients):
    # check if resources is sufficient
    for ingredient in drink_ingredients:
        if not resources[ingredient] >= drink_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    # input coins and calculate received money
    money_received = int(input("How many quarters? ")) * 0.25
    money_received += int(input("How many dimes? ")) * 0.10
    money_received += int(input("How many nickles? ")) * 0.05
    money_received += int(input("How many pennies? ")) * 0.01
    return money_received


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        # deduction of money, addition of money and calculate changes
        money_received -= drink_cost
        resources["money"] += drink_cost
        customer_money_as_str = "{0:.2f}".format(money_received)
        print(f"Here is ${customer_money_as_str} in change.")
        winsound.PlaySound(cash_register_sound, winsound.SND_FILENAME)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]

    winsound.PlaySound(coffee_machine_sound, winsound.SND_FILENAME)
    winsound.PlaySound(process_complete_sound, winsound.SND_FILENAME)

    print(f"Here is your {drink} ☕. Enjoy!")


def coffee_machine():
    is_on = True
    drinks = list(MENU.keys())

    while is_on:
        # user input
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        # customer order drinks
        if choice in drinks:
            drink = MENU[choice]
            drink_name = choice
            drink_ingredients = drink["ingredients"]
            # process coins
            if is_resources_sufficient(drink_ingredients):
                money_received = process_coins()
                # calculate drink cost
                drink_cost = drink["cost"]
                # check money if is enough
                if is_transaction_successful(money_received, drink_cost):
                    make_coffee(drink_name, drink_ingredients)

        # make resource report
        elif choice == "report":
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${resources["money"]}')
        # turn off machine
        elif choice == "off":
            is_on = False
        # error
        else:
            print("Input Error - Please key in correct instruction")


coffee_machine()
