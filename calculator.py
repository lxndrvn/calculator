def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    try:
        num1 = int(input("Enter a number (or a letter to exit): "))
    except:
        print("That is not a number!")
        break

    operator = input("Enter an operator: ")

    if operator == "+":
        func = add
    elif operator == "-":
        func = subtract
    elif operator == "*":
        func = multiply
    elif operator == "/":
        func = divide
    else:
        print("Invalid operator!")
        break
        
    try:
        num2 = int(input("Enter another number: "))
    except:
        print("That is not a number!")
        break

    result=func(num1, num2)
    print ("Result:", result)
