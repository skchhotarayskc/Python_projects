MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 300,
    "coffee":100
}

def is_resourse_sufficient(order_ingrediets):
    '''Returns True when orders can be made, False when ingredients are insufficient'''
    for item in order_ingrediets:
        if order_ingrediets[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    '''Returns the total calculated from coin inserted'''
    print("Please Insert coins. : ")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    '''Returns True when payment is accepted, False when money is insufficient.'''
    if money_received < drink_cost:
        print("Sorry that's not enough money , Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True

def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resourse_sufficient(drink['ingredients']):
            if is_transaction_successful(process_coin(), drink['cost']):
                make_coffee(choice, drink["ingredients"])