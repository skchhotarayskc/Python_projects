calc_logo = ['''
 _____________________
|  _________________  |
| | Pycalc       0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''']

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    print(calc_logo[0])
    print("Welcome to pycalculator!")

    num1 = float(input("Whats the first number? : "))

    for symbol in operations:
        print(symbol)

    previous_ans = num1

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation from the line above : ")
        num2 = float(input("Whats the next number? : "))

        calculation_function = operations[operation_symbol]
        answer = round(calculation_function(previous_ans, num2), 2)

        print(f"{previous_ans} {operation_symbol} {num2} = {answer}")
        previous_ans = answer

        yes_or_no = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation, or 'exit' to exit : ")

        if yes_or_no == 'y':
            for symbol in operations:
                print(symbol)
        elif yes_or_no == 'n':
            should_continue = False
            calculator()
        elif yes_or_no == 'exit':
            exit()

calculator()