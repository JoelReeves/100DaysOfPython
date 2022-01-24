from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_is_on = True

while coffee_machine_is_on:
    menu_choice = input("What would you like? (espresso -$1.50) | (latte - $2.50) | (cappuccino -$3.00): ").lower().strip()

    if menu_choice == "off":
        print("Turning coffee machine off. Have a nice day!")
        coffee_machine_is_on = False
    elif menu_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(menu_choice)
        if drink is None:
            print("Please select a valid drink from the menu.")
        elif not coffee_maker.is_resource_sufficient(drink):
            continue
        else:
            payment_success = money_machine.make_payment(drink.cost)
            if not payment_success:
                continue
            else:
                coffee_maker.make_coffee(drink)
