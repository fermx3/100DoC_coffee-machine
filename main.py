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


def check_resources(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            return False
        else:
            return True


def insert_coins():
    print(f'Your coffee will cost: ${drink["cost"]}. Please insert coins:')
    money_inserted = float(input('quarters: ')) * 0.25
    money_inserted += float(input('dimes: ')) * 0.1
    money_inserted += float(input('nickles: ')) * 0.05
    money_inserted += float(input('pennies: ')) * 0.01
    print(f'You inserted: ${"{:.2f}".format(money_inserted)}')
    return money_inserted


def prepare_coffee(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f'Here is your {drink_name}. ☕ Enjoy!')


machine_on = True

while machine_on:
    user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_input == 'off':
        print('Turning off machine...')
        machine_on = False

    elif user_input == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')

    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        drink = MENU[user_input]
        if check_resources(drink['ingredients']):
            money = insert_coins()
            if money < drink['cost']:
                print('Sorry that\'s not enough money. Money refunded.\n')
            else:
                resources['money'] += drink['cost']
                if money > drink['cost']:
                    change = "{:.2f}".format(round((money - drink['cost']), 2))
                    print(f'Here is ${change} dollars in change.')
            prepare_coffee(user_input, drink['ingredients'])

    else:
        print('Wrong Input.')
