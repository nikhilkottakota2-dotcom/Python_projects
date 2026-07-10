
def print_calculator():
    calculator = """
    _____________________
   |  _________________  |
   | | Python Calc    0| |
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
    """
    print(calculator)

print_calculator()

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

print("Enter the first number:")
a = int(input())
print("Enter the operation:")
print(operations.keys())
operation_input = input("Enter the symbol of the operation")
print("Enter the second number:")
b = int(input())
for operation_symbol in operations:
    if operation_symbol == operation_input:
        result = operations[operation_input](a,b)
        print(result)
        yesorno = input("Print is you have another number (y/n)")
        while yesorno == "y":
            b = int(input("Enter the another number:"))
            result = operations[operation_symbol](result,b)
            print(result)
            yesorno = input("Print is there any other number (y/n)")
        break;
    else:
        print("There is no opertion for the entered operator in the system")
