item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

total = item1 + item2 + item3

if total > 100:
    discount = total * 0.10
    final_total = total - discount
else:
    discount = 0
    final_total = total

print("Cart Total:", total)
print("Discount Applied:", discount)
print("Final Total:", final_total)
