accounts_data = {}

def create_account(account_number, name, initial_balance=0):
    accounts_data[account_number] = {'name': name, 'balance': initial_balance}

def get_balance(account_number):
    return accounts_data.get(account_number, {}).get('balance', None)

def update_balance(account_number, new_balance):
    if account_number in accounts_data:
        accounts_data[account_number]['balance'] = new_balance
