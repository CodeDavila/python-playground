# Define the MENU dictionary containing drink options, their ingredients, and cost
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

# Define the resources available in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Check if there are enough resources to make a drink
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Process the coins inserted by the user and return the total value
def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.\n")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Check if the payment is sufficient for the selected drink
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is ${change} in change.")
        return True
    else:
        print("\nSorry that's not enough money. Money refunded.")
        return False

# Make the selected drink by updating resources and serving it to the user
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\nHere is your {drink_name} ☕. Enjoy!")

# Display the menu options for the user to choose from
def display_menu():
    print("\nWelcome to the coffee shop! Here's our menu:")
    for drink_name, drink_details in MENU.items():
        cost = drink_details["cost"]
        print(f"{drink_name.capitalize()}: ${cost}")
    print("\nIf you want to close the program, please write 'off'.\n")

# Initialize profit variable to keep track of earnings
profit = 0
# Variable to control the main loop of the program
is_on = True

# Main loop of the program
while is_on:
    display_menu()
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Check if the user wants to turn off the machine
    if choice == "off":
        is_on = False
    # Check if the user wants to display a report of available resources
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        # If the user chose a drink, check if it's available and sufficient resources
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            # Check if the payment is sufficient
            if is_transaction_successful(payment, drink["cost"]):
                # If payment is successful, make the drink
                make_coffee(choice, drink["ingredients"])


