def find_gcd(n, m):
    if n <= 0 or m <= 0:
        return -1
    while m:
        n, m = m, n % m
    return n

N, M = map(int, input().split())
print(find_gcd(N, M))
