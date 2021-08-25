class Register():
    """
    Register the name and quantity when a drink selected.
    """
    def __init__(self,drink,quantity):
        self.drink = drink
        self.quantity = quantity    

    def get_item_total(self):
        item_total = self.drink.price * self.quantity
        return round(item_total)