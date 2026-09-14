# Cash Register Lab

A `CashRegister` class that models the core behavior of a cash register for an e-commerce checkout flow: adding items, applying a discount, and voiding the most recent transaction.

## Description

This project was built as part of an Object-Oriented Programming exercise focused on class design, properties, and instance state management in Python. The `CashRegister` class tracks a running total, the items currently rung up, and a history of transactions so the last one can be undone.

## Features

- **Add items** — `add_item(title, price, quantity=1)` adds an item (or multiple units of it) to the register, updating the running total and the list of items.
- **Apply a discount** — `apply_discount()` reduces the total by the register's discount percentage (set at initialization). If no discount was set, it prints an error message instead.
- **Void the last transaction** — `void_last_transaction()` reverses the most recent `add_item` call, correctly adjusting the total whether it was a single item or a bulk quantity.
- **Discount validation** — the `discount` property ensures the value is a whole number between 0 and 100 inclusive; invalid values print `"Not valid discount"`.

## Installation

Clone the repo and install dependencies with Pipenv:

```bash
git clone https://github.com/<your-username>/oop-p2-cash-register-lab.git
cd oop-p2-cash-register-lab
pipenv install
pipenv shell
```

## Usage

```python
from cash_register import CashRegister

register = CashRegister(20)  # 20% discount
register.add_item("macbook air", 1000)
register.apply_discount()
# After the discount, the total comes to $800.
```

## Running Tests

```bash
pytest
```

All 14 tests should pass:

![Image of passing test suite](/images/Test.png)

## Author

Cornē Nagel

## License

See `LICENSE.md`.
