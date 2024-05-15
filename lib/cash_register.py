#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0.0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        self.items.extend([title] * quantity)
        
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")
            
    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        # Removing the last transaction items from the list
        for _ in range(self.items.count(self.last_transaction_amount)):
            self.items.remove(self.last_transaction_amount)
        self.last_transaction_amount = 0.0

# Example usage:
if __name__ == '__main__':
    register = CashRegister(20)
    register.add_item("book", 12.99, 2)
    register.add_item("pen", 0.99)
    print(f"Total before discount: ${register.total}")
    register.apply_discount()
    print(f"Total after discount: ${register.total}")
    register.void_last_transaction()
    print(f"Total after voiding last transaction: ${register.total}")
    print(f"Items in register: {register.items}")
