# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: R{amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrawn: R{amount:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False
    def display_balance(self):
        print(f"Current Balance: R{self.__account_balance:.2f}")
