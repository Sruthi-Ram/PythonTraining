from banking import accounts

def deposit(account_number, amount):
    balance = accounts.get_balance(account_number)
    if balance is not None:
        accounts.update_balance(account_number, balance + amount)

def withdraw(account_number, amount):
    balance = accounts.get_balance(account_number)
    if balance is not None and balance >= amount:
        accounts.update_balance(account_number, balance - amount)

def transfer(from_account, to_account, amount):
    from_balance = accounts.get_balance(from_account)
    to_balance = accounts.get_balance(to_account)
    if from_balance is not None and to_balance is not None and from_balance >= amount:
        accounts.update_balance(from_account, from_balance - amount)
        accounts.update_balance(to_account, to_balance + amount)
