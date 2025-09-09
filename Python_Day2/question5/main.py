from banking import accounts, transactions

acc_num = input("Enter account number: ")
name = input("Enter account holder name: ")
initial = float(input("Enter initial deposit: "))
accounts.create_account(acc_num, name, initial)

action = input("Choose action (deposit/withdraw/transfer): ").strip().lower()

if action == "deposit":
    amt = float(input("Enter amount to deposit: "))
    transactions.deposit(acc_num, amt)
elif action == "withdraw":
    amt = float(input("Enter amount to withdraw: "))
    transactions.withdraw(acc_num, amt)
elif action == "transfer":
    to_acc = input("Enter recipient account number: ")
    amt = float(input("Enter amount to transfer: "))
    accounts.create_account(to_acc, "Recipient", 0)
    transactions.transfer(acc_num, to_acc, amt)

print("Updated balance:", accounts.get_balance(acc_num))
