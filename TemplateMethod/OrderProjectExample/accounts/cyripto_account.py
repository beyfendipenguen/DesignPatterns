from accounts.account import Account


class CryptoAccount(Account):

    def __init__(self, balance):
        self.balance = balance
