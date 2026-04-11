
'''
This program simulates a coffee machine that can make espresso, latte, and cappuccino.
It has a limited amount of resources and will only make the drink if it has enough resources.
It has extra features such as reporting the current resources and turning off the machine.
'''

# Function to check if the coffee machine has enough resources for the order
def is_resource_sufficient(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Function to print the ingredient report including money
def ingredient_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}\n")

# Function to calculate the money needed for the order based off coins
def money_needed():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

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
    "money": 0,
}

# Choice of drink for order (or report or off)
order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

# Main loop for the coffee machine
while order != "off":
    if order == "report":
        ingredient_report()

    # Check if the order is a valid drink
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        # Check if the coffee machine has enough resources for the order
        if is_resource_sufficient(order):

            print("\nPlease insert your coins.\n")
            dollars = money_needed()

            # Check if the money inserted is enough for the order
            if dollars >= MENU[order]["cost"]:
                # Deduct the ingredients from the coffee machine
                for i in MENU[order]["ingredients"]:
                    resources[i] -= MENU[order]["ingredients"][i]
                
                # Add the money to the coffee machine
                resources["money"] += MENU[order]["cost"]

                # Calculate the change
                change = dollars - MENU[order]["cost"]
                print(f"\nHere is your {order}. Enjoy!")
                print(f"Here is your change: ${change:.2f}\n")

            else:
                print("Transaction failed. Your money is getting refunded...\n")

    # Get the next order
    order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

# Print that the coffee machine is turning off
print("\nCoffee Machine turning off. . .")

