import json


def deposit(balance):
    amount = float(input('Enter the amount to deposit: '))
    balance += amount
    print(f'Account credited with {amount}. Current balance: {balance}')
    return balance


def purchase(balance, history):
    amount = float(input('Enter the purchase amount: '))
    if amount > balance:
        print('Insufficient funds.')
    else:
        item = input('Enter the name of the purchase: ')
        balance -= amount
        history.append((item, amount))
        print(
            f'Purchase {item} for {amount} completed. Current balance: {balance}')
    return balance, history


def purchase_history(history):
    if not history:
        print('Purchase history is empty.')
    else:
        for item, amount in history:
            print(f'{item}: {amount}')
    return


def purchased_log():
    with open('datafiles/account_data.json', 'r') as f:
        purchased = json.load(f)
        # print(purchased)
        # print(json.dumps(purchased, indent=4, ensure_ascii=False))
        for entry in purchased:
            print(f"item: {entry['item']}, amount: {entry['amount']}")
    return


def save_history(history):
    data = [{'item': item, 'amount': amount} for item, amount in history]

    try:
        with open('datafiles/account_data.json', 'r') as f:
            file_content = f.read()
            if file_content:
                existing_data = json.loads(file_content)
            else:
                existing_data = []
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(data)

    with open('datafiles/account_data.json', 'w') as f:
        json.dump(existing_data, f, indent=4)

def load_balance():
    try:
        with open('datafiles/account_balance.json', 'r') as f:
            balance = json.load(f)
    except FileNotFoundError:
        balance = 0
    return balance

def save_balance(balance):
    with open('datafiles/account_balance.json', 'w') as f:
        json.dump(balance, f, indent=4)


def view_bank_account():
    balance = load_balance()
    history = []

    while True:
        print('1. Deposit')
        print('2. Purchase')
        print('3. Current purchases')
        print('4. Purchase history')
        print('5. Current balance')
        print('6. Exit')

        choice = input('Choose an option: ')
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance, history = purchase(balance, history)
        elif choice == '3':
            purchase_history(history)
        elif choice == '4':
            purchased_log()
        elif choice == '5':
            print(f'Current balance: {balance}')
        elif choice == '6':
            save_history(history)
            save_balance(balance)
            break
        else:
            print('Invalid option')


if __name__ == '__main__':
    view_bank_account()
