n = input()
digits = [int(d) for d in n]
s = sum(digits)
p = 1
for d in digits:
    p *= d
print(s == p)
