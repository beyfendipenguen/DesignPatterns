from abc import ABC, abstractmethod


class Account(ABC):
    balance = None

    def process_payment(self, amount):
        if self.get_balance() < amount:
            raise ValueError("Balance cannot be less than the amount.")

        self.balance = self.get_balance() - amount
        return True

    def get_balance(self):
        if self.balance is None:
            raise ValueError("Set balance attribute or override get_balance method.")
        return self.balance
