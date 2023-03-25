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

is_on = True

while is_on:
    coffee = input("What would you like? (espresso/latte/cappuccino):" ).lower()

    if coffee == 'off':
        is_on = False
    else:
        if coffee == 'report':
            print(f'Water\t:{resources.get("water")} ')
            print(f'Milk\t:{resources.get("Milk")} ')
            print(f'Water\t:{resources.get("water")} ')
            print(f'Water\t:{resources.get("water")} ')
