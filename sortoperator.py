from operator import attrgetter, methodcaller, itemgetter

class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount
        
