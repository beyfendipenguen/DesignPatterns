from abc import ABC, abstractmethod


class Order(ABC):

    def __init__(self, account):
        self.account = account

    def place_order(self,amount):
        if not self.validate_order():
            raise PermissionError("validate order error")
        self.process_payment(amount)
        self.complete_order()

    @abstractmethod
    def validate_order(self):
        pass

    def process_payment(self,amount):
        if not self.account:
            raise ValueError("Account can not be None")
        self.account.process_payment(amount)

    @abstractmethod
    def complete_order(self):
        pass
