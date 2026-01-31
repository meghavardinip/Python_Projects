import art
def artin():
    print(art.logo())
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero!"
    return n1 / n2


# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def operation_to_be_performed():
    print("Choose the operation to be performed from the given list:")
    for op in operations.keys():
        print(op)
    choice = input("Your choice: ")
    return choice
def perform_operation(choice, n1, n2):
    if choice in operations:
        return operations[choice](n1, n2)
    else:
        return "Invalid operation!"
def calculator():
    print(art.logo)
    n1 = float(input("Enter the first number: "))
    choice=operation_to_be_performed()
    n2 = float(input("Enter the second number: "))
    result = perform_operation(choice, n1, n2)
    print(f"{n1}{choice}{n2}={result}")
    continue_or_not = input("If you want to continue working with the previous result, type 'yes', otherwise type 'no': ")
    if continue_or_not.lower() == "yes":
        n3 = result
        choice = operation_to_be_performed()
        result = perform_operation(choice, n3, n2)
        print(f"New Result: {result}")
    elif continue_or_not.lower() == "no":
        new_game()
    else:
        print("Invalid input")
    return None
def new_game():
    decision=input("Do want to use calculator? type if y/n:")
    if decision=="y":
        calculator()
    else:
        print("Thanks for using the calculator!")
        return
    return None
new_game()
