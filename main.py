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
    """Returns 'make coffee' if there are enough resources or return corresponding message
    in case that there is no enough resource of a type"""
    if resources['water'] >= water_needed:
        if resources['coffee'] >= coffee_needed:
            if resources['milk'] >= milk_needed:
                return 'make coffee'
            else:
                return 'Sorry there is not enough milk.'
        else:
            return 'Sorry there is not enough coffee.'
    else:
        return 'Sorry there is not enough water.'


def get_ingredient_needed(type_of_coffee, ingredient):
    """Returns the amount of ingredient needed to prepare the type of coffee entered."""
    return MENU[type_of_coffee]['ingredients'][ingredient]


user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()
coffee_message = ''

if user_input == 'off':
    print('Machine turning off...')
elif user_input == 'report':
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')
elif user_input == 'espresso':
    espresso_water_needed = get_ingredient_needed('espresso', 'water')
    espresso_coffee_needed = get_ingredient_needed('espresso', 'coffee')
    coffee_message = check_resources(espresso_water_needed, 0, espresso_coffee_needed)
elif user_input == 'latte':
    latte_water_needed = get_ingredient_needed('latte', 'water')
    latte_coffee_needed = get_ingredient_needed('latte', 'coffee')
    latte_milk_needed = get_ingredient_needed('latte', 'milk')
    coffee_message = check_resources(latte_water_needed, latte_milk_needed, latte_coffee_needed)
elif user_input == 'cappuccino':
    cappuccino_water_needed = get_ingredient_needed('cappuccino', 'water')
    cappuccino_coffee_needed = get_ingredient_needed('cappuccino', 'coffee')
    cappuccino_milk_needed = get_ingredient_needed('cappuccino', 'milk')
    coffee_message = check_resources(cappuccino_water_needed, cappuccino_milk_needed, cappuccino_coffee_needed)

print(coffee_message)
