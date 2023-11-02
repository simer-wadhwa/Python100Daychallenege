
from extra_files import art

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


operations = {'+':add ,
            '-':sub ,
            '*': mul ,
            '/': div }

def calculator():
    print(art.cal_logo)
    num1 = float(input("What's the number?: "))



    for symbol in operations:
        print(symbol)



    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_fun = operations[operation_symbol]
        answer =calculation_fun(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        result = input(f"Do you want to continue calculating with {answer} then type 'y', or type 'n' to start new calculation ")
        if result.lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()