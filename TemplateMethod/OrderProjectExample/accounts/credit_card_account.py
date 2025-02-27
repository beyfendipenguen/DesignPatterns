from accounts.account import Account

class CreditCardAccount(Account):

    def __init__(self, balance):
        self.balance = balance