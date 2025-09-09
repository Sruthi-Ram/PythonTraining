import math

n = int(input("Enter first number (N): "))
m = int(input("Enter second number (M): "))

product = n * m

if math.isqrt(product) ** 2 == product:
    print("yes")
else:
    print("no")
