# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the BankAccount with an optional initial balance, default is 0."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a certain amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw a certain amount from the account if funds are sufficient."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current balance: ${self.__account_balance:.2f}")

