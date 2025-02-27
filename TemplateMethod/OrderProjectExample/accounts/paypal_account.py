from accounts.account import Account


class PaypalAccount(Account):

    def __init__(self, balance):
        self.balance = balance
