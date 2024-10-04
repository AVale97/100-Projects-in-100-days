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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0  # Machine starts at 0

# Checking if there are enough resources


def check_resources(order):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Processes inserted coins and returns the total amount."""
    try:
        print("Please insert coins.")
        quarters = int(input("How many quarters will you insert? "))
        dimes = int(input("How many dimes will you insert? "))
        nickels = int(input("How many nickels will you insert? "))
        pennies = int(input("How many pennies will you insert? "))
    except ValueError:
        print("Invalid coin amount. Please enter integers only.")
        return None  # Returns None if input is invalid

    total_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_inserted


def make_coffee(order):
    """Deduct ingredients from resources and serve the coffee."""
    ingredients = MENU[order]["ingredients"]
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    if "milk" in ingredients:
        resources["milk"] -= ingredients["milk"]
    print(f"Here is your {order}. Enjoy!")

while True:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()

    if order == "off":
        print("Turning off the coffee machine. Goodbye!")
        break

    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        continue

    # Check if the drink exists in the menu
    if order not in MENU:
        print("Sorry, we don't serve that drink.")
        continue

    # Check if there are enough resources
    if not check_resources(order):
        continue

    # Process coins
    total_inserted = process_coins()
    if total_inserted is None:  # Invalid coin input
        continue


    # Checking transaction success
    if total_inserted < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        money += MENU[order]["cost"]
        change = total_inserted - MENU[order]["cost"]
        if change > 0:
            print(f"Here is {change:.2f} dollars in change")


    # Make coffee
        make_coffee(order)  # Now this is called after a successful transaction


