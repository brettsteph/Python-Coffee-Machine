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
    "milk": 200,
    "coffee": 100,
    "water": 300,
}

coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
machine_is_on = True
machine_profit = 0.0


def calculate_coins(coffee, num_quarters, num_dimes, num_nickles, num_pennies):
    q_sum = coins['quarters'] * num_quarters
    d_sum = coins['dimes'] * num_dimes
    n_sum = coins['nickles'] * num_nickles
    p_sum = coins['pennies'] * num_pennies
    return q_sum + d_sum + p_sum + n_sum


def calculate_change(total_coins, coffee_drink):
    return round(total_coins - coffee_drink["cost"], 2)


def update_resources(coffee_drink):
    ingredients = coffee_drink["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def check_resources(coffee_drink):
    check = True
    ingredients = coffee_drink["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}!")
            check = False

    return check


while machine_is_on:
    user_input = (input("What would you like? (espresso/latte/cappuccino): ")).lower()

    if user_input == 'off':
        machine_is_on = False
        print("Machine switched off!")
    elif user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${machine_profit}")
    elif user_input == 'refill':
        resources['milk'] = 200
        resources['coffee'] = 100
        resources['water'] = 300
        print("Coffee machine's resources were replenished. You can make a purchase.")
    else:
        drink = MENU[user_input]
        cost = drink["cost"]
        if check_resources(drink):
            default = 0
            print(f'Please insert coins. ${cost} for a {user_input}.')
            input_quarters = int(input('How many quarters?: ') or default)
            input_dimes = int(input('How many dimes?: ') or default)
            input_nickles = int(input('How many nickles?: ') or default)
            input_pennies = int(input('How many pennies?: ') or default)
            total = calculate_coins(user_input, input_quarters, input_dimes, input_nickles, input_pennies)
            if total < cost:
                print("Sorry that's not enough money. Money refunded.")
            elif total > cost:
                print(f"Here is ${calculate_change(total, drink)} in change.")
                print(f"Here is your {user_input}. Enjoy!")
                update_resources(drink)
                machine_profit += cost
            else:
                print(f"Here is your {user_input}. Enjoy!")
                update_resources(drink)
                machine_profit += cost
