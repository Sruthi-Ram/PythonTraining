def add(a, b):
    print("Add:", a + b)

def sub(a, b):
    print("Subtract:", a - b)

def mul(a, b):
    print("Multiply:", a * b)

def div(a, b):
    if b != 0:
        print("Divide:", a / b)
    else:
        print("Divide: Error (division by zero)")

num1 = 10
num2 = 5

add(num1, num2)     
sub(num1, num2)     
mul(num1, num2)     
div(num1, num2)    
