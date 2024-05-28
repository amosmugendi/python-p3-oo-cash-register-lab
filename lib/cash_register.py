#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.prices = []
        self.last_transaction_amount = 0
        self.total = 0
        self.discount = discount

    def add_item(self, item, price, quantity=1):
        transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(item)
            self.prices.append(price)
        self.total += transaction_amount
        self.last_transaction_amount = transaction_amount

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Formatting to print without decimal places if the total is a whole number
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction_amount != 0:
            for _ in range(self.prices.count(self.last_transaction_amount // len(self.items))):
                self.items.pop()
                self.prices.pop()
            self.total -= self.last_transaction_amount
            self.last_transaction_amount = 0

# Examples
register = CashRegister()
register.add_item("Wheelbarrow", 200, 3)
register.add_item("Rake", 120)

print(register.total)  # Output should be 720

register.apply_discount()
print(register.total)  # Output should be 720 (no discount applied as default discount is 0)

register_with_discount = CashRegister(20)
register_with_discount.add_item("Wheelbarrow", 200, 3)
register_with_discount.add_item("Rake", 120)
register_with_discount.apply_discount()

print(register_with_discount.total)  # Output should be 576 (720 * 0.8)

register_with_discount.void_last_transaction()
print(register_with_discount.total)  # Output should be 360 (576 - 216)
