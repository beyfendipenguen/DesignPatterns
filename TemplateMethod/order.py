from abc import ABC, abstractmethod


class Order(ABC):

    account = None

    def __init__(self, account):
        self.account = account

    def place_order(self):
        if not self.validate_order():
            raise PermissionError("validate order error")
        self.process_payment()
        self.complate_order()

    @abstractmethod
    def validate_order(self):
        pass

    def process_payment(self):
        if not self.account:
            raise ValueError("Account can not be None")
        self.account.process_payment()

    @abstractmethod
    def complete_order(self):
        pass
