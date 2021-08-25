from drink import Drink
from register import Register
from order import Order
from payment import Payment
from unittest import mock

fanta=Drink("Fanta",20)
hot_chocolate=Drink("hot_chocolate",20)
apple_juice=Drink("apple_juice",20)
selected_drinks=[]
selected_drinks.append(Register(fanta,2))
selected_drinks.append(Register(hot_chocolate,3))
selected_drinks.append(Register(apple_juice,4)) 


@mock.patch("payment.credit_card_pay_interface")
def test0(mock_credit_card_pay_interface):
    mock_credit_card_pay_interface.return_value=True
    print("test #0, when the credit card interface return True:")
    order=Order(selected_drinks,0.5,"credit_card")
    payment=Payment(order)
    print("\n")

@mock.patch("payment.credit_card_pay_interface")
def test1(mock_credit_card_pay_interface):
    mock_credit_card_pay_interface.return_value=False
    print("test #1, when the credit card pay interface return False:")
    order=Order(selected_drinks,0.5,"credit_card")
    payment=Payment(order)
    print("\n")

@mock.patch("payment.cash_pay_interface")
def test2(mock_cash_pay_interface):
    mock_cash_pay_interface.return_value =True
    print("test #2, when cash pay interface return True:")
    order=Order(selected_drinks,1,"cash")
    payment=Payment(order)
    print("\n")

@mock.patch("payment.cash_pay_interface")
def test3(mock_cash_pay_interface):
    mock_cash_pay_interface.return_value =False
    print("test #3, when cash pay interface return True:")
    order=Order(selected_drinks,1,"cash")
    payment=Payment(order)
    print("\n")

def test4():
    print("test #4, when the payment using apple pay:")
    order=Order(selected_drinks,0.5,"apple_pay")
    payment=Payment(order)
    print("\n")
    
test0()
test1()
test2()
test3()
test4()
     