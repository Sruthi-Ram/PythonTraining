import math

def is_peterson(n):
    return n == sum(math.factorial(int(d)) for d in str(n))

n = 145
print(is_peterson(n))
