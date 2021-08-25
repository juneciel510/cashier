class Order:
    def __init__(self, selected_drinks, discount, payment_method):
        self.selected_drinks = selected_drinks
        self.discount = discount
        self.payment_method = payment_method
        self.status=False

    def get_order_total(self):
        order_total=0
        for item in self.selected_drinks:
            order_total += item.get_item_total()
        order_total=order_total*self.discount
        return round(order_total)

    #set the status to be True if it is paid
    def set_status_paid(self):
        self.status=True