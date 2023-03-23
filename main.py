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
    "money": 0
}


def check_resources(water_needed, milk_needed, coffee_needed):
    """Returns an object with key 'make-coffee' that returns True or False
    depending on if are enough resources. In addition, if there are not enough
    returns an error message"""
    if resources['water'] >= water_needed:
        if resources['coffee'] >= coffee_needed:
            if resources['milk'] >= milk_needed:
                return {'make_coffee': True}
            else:
                return {
                    'make_coffee': False,
                    'message': 'Sorry there is not enough milk.\n'
                }
        else:
            return {
                'make_coffee': False,
                'message': 'Sorry there is not enough coffee.\n'
            }
    else:
        return {
            'make_coffee': False,
            'message': 'Sorry there is not enough water.\n'
        }


def get_ingredient_needed(type_of_coffee, ingredient):
    """Returns the amount of ingredient needed to prepare the type of coffee entered."""
    return MENU[type_of_coffee]['ingredients'][ingredient]


def calculate_money(inserted_quarters, inserted_dimes, inserted_nickles, inserted_pennies):
    inserted_quarters *= 0.25
    inserted_dimes *= 0.1
    inserted_nickles *= 0.05
    inserted_pennies *= 0.01
    return inserted_quarters + inserted_dimes + inserted_nickles + inserted_pennies


machine_on = True

while machine_on:
    water_required = 0
    coffee_required = 0
    milk_required = 0
    make_coffee = False
    error_message = ''
    coffee_cost = 0
    coffee_to_prepare = ''

    user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_input == 'espresso':
        water_required = get_ingredient_needed('espresso', 'water')
        coffee_required = get_ingredient_needed('espresso', 'coffee')
        check_resources_output = check_resources(water_required, milk_required, coffee_required)
        if check_resources_output['make_coffee']:
            make_coffee = check_resources_output['make_coffee']
            coffee_cost = MENU['espresso']['cost']
            coffee_to_prepare = 'espresso'
        else:
            error_message = check_resources_output['message']

    elif user_input == 'latte':
        water_required = get_ingredient_needed('latte', 'water')
        coffee_required = get_ingredient_needed('latte', 'coffee')
        milk_required = get_ingredient_needed('latte', 'milk')
        check_resources_output = check_resources(water_required, milk_required, coffee_required)
        if check_resources_output['make_coffee']:
            make_coffee = check_resources_output['make_coffee']
            coffee_cost = MENU['latte']['cost']
            coffee_to_prepare = 'latte'
        else:
            error_message = check_resources_output['message']

    elif user_input == 'cappuccino':
        water_required = get_ingredient_needed('cappuccino', 'water')
        coffee_required = get_ingredient_needed('cappuccino', 'coffee')
        milk_required = get_ingredient_needed('cappuccino', 'milk')
        check_resources_output = check_resources(water_required, milk_required, coffee_required)
        if check_resources_output['make_coffee']:
            make_coffee = check_resources_output['make_coffee']
            coffee_cost = MENU['latte']['cost']
            coffee_to_prepare = 'cappuccino'
        else:
            error_message = check_resources_output['message']

    elif user_input == 'off':
        print('Machine turning off...')
        machine_on = False

    elif user_input == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')

    else:
        print('Wrong Input.')

    if make_coffee:
        print(f'Your coffee will cost: ${coffee_cost}. Please insert coins:')
        quarters = float(input('quarters: '))
        dimes = float(input('dimes: '))
        nickles = float(input('nickles: '))
        pennies = float(input('pennies: '))
        money_inserted = calculate_money(quarters, dimes, nickles, pennies)
        print(f'You inserted: ${"{:.2f}".format(money_inserted)}')

        if money_inserted < coffee_cost:
            print('Sorry that\'s not enough money. Money refunded.\n')
        else:
            resources['money'] += coffee_cost
            if money_inserted > coffee_cost:
                change = "{:.2f}".format(round((money_inserted - coffee_cost), 2))
                print(f'Here is ${change} dollars in change.')
            resources['water'] -= water_required
            resources['coffee'] -= coffee_required
            resources['milk'] -= milk_required
            print(f'Here is your {coffee_to_prepare}. Enjoy!\n')
    else:
        print(error_message)
