

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
}


def run_machine(profit):

    coffee_choice = input("What would you like?(espresso/latte/cappuccino)\n")

    if coffee_choice == "report":
        print(f"{resources['water']} Water\n{resources['milk']} Milk\n{resources['coffee']} Coffee\nProfit: {profit}$\n")

    def enough(water_c, milk_c, coffee_c):

            if water_c <= resources["water"] and milk_c <= resources["milk"] and coffee_c <= resources["coffee"]:
                resources["water"] -= water_c
                resources["milk"] -= milk_c
                resources["coffee"] -= coffee_c
                print("Preparing Coffee Machine...")
                return resources["water"], resources["milk"], resources["coffee"]
            else:
                print("Sorry, machine ran out of resources")
            return False

    def money():
        penny = 0.01 * float(input("How many pennies do you want to insert?\n"))
        nickle = 0.05 * float(input("How many nickles do you want to insert?\n"))
        dime = 0.1 * float(input("How many dimes do you want to insert?\n"))
        quarter = 0.25 * float(input("How many quarters do you want to insert?\n"))

        give = penny + nickle + dime + quarter
        change = round(((MENU[coffee_choice]["cost"] * -1) + give), 2)
        if change > 0:
            print(f"Enough inserted, here is your Change: {change}$ and your {coffee_choice}")
        else:
            print(f"too little here's your money back {give}$")

    if coffee_choice == "espresso":
        result = enough(MENU[coffee_choice]["ingredients"]["water"],
                   MENU[coffee_choice]["ingredients"]["milk"],
                   MENU[coffee_choice]["ingredients"]["coffee"])
        if result != False:
            money()
            profit += MENU[coffee_choice]["cost"]


    elif coffee_choice == "latte":
        result = enough(MENU[coffee_choice]["ingredients"]["water"],
                        MENU[coffee_choice]["ingredients"]["milk"],
                        MENU[coffee_choice]["ingredients"]["coffee"])
        if result != False:
            money()
            profit += MENU[coffee_choice]["cost"]

    elif coffee_choice == "cappuccino":
        result = enough(MENU[coffee_choice]["ingredients"]["water"],
                        MENU[coffee_choice]["ingredients"]["milk"],
                        MENU[coffee_choice]["ingredients"]["coffee"])
        if result != False:
            money()
            profit += MENU[coffee_choice]["cost"]

    return profit

machine = True
gewinn = 0

while machine:
    gewinn = run_machine(gewinn)
