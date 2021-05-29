from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import winsound


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
all_drinks = menu.get_items()

coffee_machine_sound = r"day-016\Espresso-Machine-Jet-Out-Hot-Water-into-Metal-Cup.wav"
cash_register_sound = r"day-016\Cash Register (Kaching) - Sound Effect.wav"
process_complete_sound = r"day-016\Elevator Bell Ring Sound.wav"

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice in all_drinks:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                winsound.PlaySound(cash_register_sound, winsound.SND_FILENAME)
                winsound.PlaySound(coffee_machine_sound, winsound.SND_FILENAME)
                coffee_maker.make_coffee(drink)
                winsound.PlaySound(process_complete_sound, winsound.SND_FILENAME)

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        is_on = False
