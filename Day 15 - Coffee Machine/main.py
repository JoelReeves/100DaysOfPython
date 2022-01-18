import menu

def turn_off_coffee_machine():
    print("Turning coffee machine off. Have a nice day!")
    exit()

def is_valid_menu_drink(choice):
    return choice == "espresso" or choice == "latte" or choice == "cappuccino"

def print_resources_report():
    water = menu_resources["water"]
    print(f"Water: {water}ml")
    milk = menu_resources["milk"]
    print(f"Milk: {milk}ml")
    coffee = menu_resources["coffee"]
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

def make_coffee(profit):
    if (profit > drink_cost):
        delta = profit - drink_cost
        rounded_delta = round(delta, 2)
        print(f"Here is ${rounded_delta} in change")

    choice_ingredients = drink["ingredients"]
    water_delta = menu_resources["water"] - choice_ingredients.get("water")
    milk_delta = menu_resources["milk"] - choice_ingredients.get("milk", 0)
    coffee_delta = menu_resources["coffee"] - choice_ingredients.get("coffee")

    menu_resources["water"] = water_delta
    menu_resources["milk"] = milk_delta
    menu_resources["coffee"] = coffee_delta

    global money
    money = money + drink_cost

    print(f"Here is your {drink_choice} ☕️. Enjoy!")

def are_resources_enough():
    choice = menu.MENU[drink_choice]
    resources_enough = True
    choice_ingredients = choice["ingredients"]

    water_available = menu_resources["water"]
    water_required = choice_ingredients.get("water")
    milk_available = menu_resources["milk"]
    milk_required = choice_ingredients.get("milk", 0)
    coffee_available = menu_resources["coffee"]
    coffee_required = choice_ingredients.get("coffee")

    if water_available < water_required:
        print("Sorry, not enough water available in the machine")
        print(f"Water required: {water_required}ml, Water available: {water_available}ml")
        resources_enough = False
    elif milk_available < milk_required:
        print("Sorry, there isn't enough milk available in the machine.")
        print(f"Milk required: {milk_required}ml, Milk available: {milk_available}ml")
        resources_enough = False
    elif coffee_available < coffee_required:
        print("Sorry, there isn't enough coffee available in the machine.")
        print(f"Coffee required: {coffee_required}g, Coffee available: {coffee_available}g")
        resources_enough = False

    return resources_enough

def total_coins():
    quarter_total = 0.25 * quarters_amount
    dime_total = 0.10 * dimes_amount
    nickel_total = 0.05 * nickels_amount
    pennies_total = 0.01 * pennies_amount

    total = quarter_total + dime_total + nickel_total + pennies_total
    rounded_total = round(total, 2)
    return rounded_total

quarters = 0.0
dimes = 0.0
nickels = 0.0
pennies = 0.0
money = 0

menu_resources = menu.resources
coffee_machine_is_on = True
drink_choice = ""
drink_ingredients = {}

while coffee_machine_is_on:
    drink_choice = input("What would you like? (espresso ($1.50)/latte/cappuccino): ").lower().strip()

    if drink_choice == "off":
        turn_off_coffee_machine()
    elif drink_choice == "report":
        print_resources_report()
    else:
        if not is_valid_menu_drink(drink_choice):
            print("Please select a valid drink from the menu.")
        elif not are_resources_enough():
            continue
        else:
            drink = menu.MENU[drink_choice]
            drink_cost = drink["cost"]
            drink_ingredients = drink["ingredients"]
            print("Please insert coins.")
            quarters_amount = float(input("How many quarters would you like to insert?: "))
            dimes_amount = float(input("How many dimes would you like to insert?: "))
            nickels_amount = float(input("How many nickels would you like to insert?: "))
            pennies_amount = float(input("How many pennies would you like to insert?: "))

            entered_coins = total_coins()
            if entered_coins < drink_cost:
                print("Sorry, that's not enough money. Money refunded")
                continue
            else:
                make_coffee(entered_coins)
