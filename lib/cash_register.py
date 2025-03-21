#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0  # Track last transaction for voiding

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item_name] * quantity)
        self.last_transaction = price * quantity  # Store last transaction amount

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Format total to remove decimal if it's a whole number
            total_display = f"{int(self.total)}" if self.total.is_integer() else f"{self.total:.2f}"
            print(f"After the discount, the total comes to ${total_display}.")  # Ensure period at end
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction

