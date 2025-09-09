
n = int(input("Enter number of elements: "))

numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

min_val = min(numbers)
max_val = max(numbers)

min_index = numbers.index(min_val) + 1
max_index = numbers.index(max_val) + 1

print(min_index, max_index)
