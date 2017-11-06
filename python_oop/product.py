class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    def displayInfo(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.status
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax):
        deci_tax = float(tax) / 100
        self.price = self.price + (self.price * deci_tax)
        return self
    def return_reason(self, reason):
        reason = ""
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "returned in box":
            self.status = "like new"
        elif reason == "box opend":
            self.status = "used"
            self.price = self.price - (self.price*0.20)
        return self


product1 = Product(2000, 'shoes', '0.5lb', 'Jimmy Choo')
# product1.sell().displayInfo()
product1.return_reason(15).displayInfo()
