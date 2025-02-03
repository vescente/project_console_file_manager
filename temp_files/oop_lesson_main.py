from oop_bill import Bill

current_bill = Bill()
current_bill.add(1000)
# current_bill.buy(500, 'shoes')

current_bills = {}

current_bill = None


while True:
    print('-' * 50)
    print('1. Add to balance')
    print('2. Purchase')
    print('3. Purchase history')
    print('4. Exit')
    print('5. Open new account')
    print('6. Switch account')

    choice = input('Enter choice: ')
    if choice == '1':
        amount = int(input('Enter amount to add: '))
        current_bill.add(amount)
    elif choice == '2':
        amount = int(input('Enter amount to purchase: '))
        if current_bill.can_buy(amount):
            item = input('Enter item: ')
            current_bill.buy(amount, item)
        else:
            print('Insufficient funds')    
    elif choice == '3':
        print(current_bill.purchase_history)
    elif choice == '4':
        break
    elif choice == '5':
        name = input('Enter account name: ')
        if name in current_bills:
            print('Account already exists')
        else:
            current_bills[name] = Bill()
            print('New account created')
        new_bill = Bill()
    elif choice == '6':
        name = input('Enter account name: ')
        if name in current_bills:
            current_bill = current_bills[name]
        else:
            print('Account does not exist')
