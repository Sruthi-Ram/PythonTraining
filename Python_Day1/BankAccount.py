balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposit", amount, "→ Balance:", balance)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdraw", amount, "→ Balance:", balance)
    else:
        print("Withdraw", amount, "→ Insufficient funds! Balance:", balance)


dep = float(input("Enter amount to deposit: "))
deposit(dep)

wd1 = float(input("Enter amount to withdraw: "))
withdraw(wd1)

wd2 = float(input("Enter another amount to withdraw: "))
withdraw(wd2)
