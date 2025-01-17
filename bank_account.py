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


def view_bank_account():
    balance = 0
    history = []

    while True:
        print('1. Deposit')
        print('2. Purchase')
        print('3. Purchase history')
        print('4. Exit')

        choice = input('Choose an option: ')
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance, history = purchase(balance, history)
        elif choice == '3':
            purchase_history(history)
        elif choice == '4':
            break
        else:
            print('Invalid option')


if __name__ == '__main__':
    view_bank_account()
