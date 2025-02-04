class Bill:

    def __init__(self):
        self.amount = 0
        self.purchase_history = []

    def add(self, amount):
        """
        Adds amount to balance.
        """
        self.amount += amount
        return self.amount
    
    def can_buy(self, amount):
        """
        Checks if amount can be deducted from balance.
        """
        return self.amount >= amount
        
    def buy(self, amount, item):
        """
        Deducts amount from balance and adds item to purchase history.
        """
        pass

        if self.can_buy(amount):
            # Deduct amount from balance
            self.amount -= amount
            self.purchase_history.append((item, amount))
        else:
            # TODO: Raise an exception
            raise Exception('Insufficient funds')
            print('Insufficient funds')




if __name__ == '__main__':
    leo_bill = Bill()
    print(leo_bill.amount)
    leo_bill.add(100)
    leo_bill.add(90)
    print(leo_bill.amount)

    kate_bill = Bill()
    print(kate_bill.amount)
    kate_bill.add(200)
    print(kate_bill.amount)