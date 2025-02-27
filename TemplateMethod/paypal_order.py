from TemplateMethod.order import Order
from TemplateMethod.models import PaypalAccount


class PaypalOrder(Order):

    def __init__(self,paypal_account):
        self.account = paypal_account

    def validate_order(self):
        return True


    def complete_order(self):
        print("order is completed")
