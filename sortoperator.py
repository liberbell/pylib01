from operator import attrgetter, methodcaller, itemgetter

class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discountPrice(self):
        return self.price - (self.price * self.discount)
