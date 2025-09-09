def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
rev = int(str(n)[::-1])
print(is_prime(n) and is_prime(rev) and n != rev)
