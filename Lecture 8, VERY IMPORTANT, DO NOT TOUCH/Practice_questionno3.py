class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("Nintendo switch 2", 499)
odr2 = Order("PS5", 800)

print(odr2 < odr1)
