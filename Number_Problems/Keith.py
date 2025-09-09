n = int(input())
digits = [int(d) for d in str(n)]
seq = digits[:]
while sum(seq[-len(digits):]) < n:
    seq.append(sum(seq[-len(digits):]))
print(sum(seq[-len(digits):]) == n)
