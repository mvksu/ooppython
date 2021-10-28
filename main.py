import random

class Cart:
    def __init__(self):
        self.total = 0
        self.items = []
        self.client = ''
        self.seller = ''
        self.number = ''
        self.invoicedate = ''
        self.selldate = ''
        self.payday = ''
        self.invoice = {
            'items': [],
            'total': 0
        }
    def add_item(self, name, price, quantity):
        order = Order(name, price, quantity)
        self.invoice['items'].append(order)
        print(self.invoice['items'])
    def generateNumber(self):
        print(random.randint(1000, 9999))




class Order:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.priceperunit = price
        self.totalnettoprice = price * quantity
        self.tax = 0.23
        self.totalbruttoprice = self.totalnettoprice + self.totalnettoprice * 0.23
    def getPrice(self):
        return self.totalbruttoprice


class Client:
    def __init__(self, name, address, nip):
        self.name = name
        self.address = address
        self.nip = nip

class Seller:
    def __init__(self, name, address, nip, banknumber):
        self.name = name
        self.address = address
        self.nip = nip
        self.banknumber = banknumber




c = Cart()
c.add_item('marchewa', 10, 5)
c.add_item('ziemniakia', 5, 5)
c.generateNumber()