from credit_card_pay_interface import credit_card_pay_interface
from cash_pay_interface import cash_pay_interface

class Payment:
    def __init__(self,order):
        self.order=order
        self.to_pay()

    def card_checkout(self): 
        """
        if credit_card_pay_interface does not return True,
        raise the AssertionError
        """
        assert credit_card_pay_interface(self.order.get_order_total())
        self.order.set_status_paid()
        print("The amount of the order is " +str(self.order.get_order_total()) +" Kroners, paid with credit card.")

    def cash_checkout(self):  
        """
        if cash_card_pay_interface does not return True,
        raise the AssertionError
        """    
        assert cash_pay_interface(self.order.get_order_total())
        self.order.set_status_paid()
        print("The amount of the order is " +str(self.order.get_order_total()) +" Kroners, paid with cash.")

    def to_pay(self):
        if self.order.payment_method=="credit_card":
            try:
                self.card_checkout()
            except AssertionError:
                print("Error occurs during the payment with credit card.")
            
        elif self.order.payment_method=="cash":   
            try:
                self.cash_checkout()
            except AssertionError:
                print("Error occurs during the payment with cash.")
            
        else:
            print(self.order.payment_method +": is not available.")