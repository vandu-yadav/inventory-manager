class Product:
    def __init__(self, id, name, category, qty, price):
        self.id = id
        self.name = name
        self.category = category
        self.qty = qty
        self.price = price
    
    def update_product_name(self,new_name):
        self.name = new_name

    def update_category_name(self,new_name):
        self.category = new_name

    def update_qty(self,qty):
        self.qty = qty

    def update_price(self,price):
        self.price = price
    
    def adjust_qty(self,n):
        new_q = self.qty+n
        if new_q < 0:
            raise ValueError('Qty is becoming negative post adjustment')
        self.qty = new_q
