#!/usr/bin/env python3

class CashRegister:
    '''Simulates a cash register for an e-commerce site.'''

    def __init__(self, discount=0):
        # discount is a percentage off the total (e.g. 20 == 20% off)
        self.discount = discount
        # running total of all items currently in the register
        self.total = 0
        # flat list of item names, expanded by quantity
        self.items = []
        # history of each add_item call, used to void the last transaction
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # discount must be a whole number between 0 and 100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, title, price, quantity=1):
        '''Adds an item (or multiple) to the register and updates the total.'''
        self.total += price * quantity

        # add the item name to the items list once per unit purchased
        for _ in range(quantity):
            self.items.append(title)

        # record this transaction so it can be voided later
        self.previous_transactions.append({
            "item": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        '''Applies the register's discount percentage to the total.'''
        if self.discount:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${self._format_price(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        '''Removes the most recent add_item transaction from the register.'''
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()

        # remove that transaction's contribution to the total
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        # remove the corresponding items from the items list
        for _ in range(last_transaction["quantity"]):
            if self.items:
                self.items.pop()

    @staticmethod
    def _format_price(amount):
        '''Formats a price without a trailing .0 for whole-dollar amounts.'''
        if amount == int(amount):
            return str(int(amount))
        return str(round(amount, 2))