import random
from datetime import date


class Cart:
    def __init__(self):
        self.invoice = {
            'items': [],
            'total': 0,
            'client': None,
            'seller': None,
            'number': None,
            'invoiceDate': None,
            'sellDate': None,
            'payDay': None,
        }

    def add_item(self, name, price, quantity):
        order = Order(name, price, quantity)
        self.invoice['items'].append(order)
        self.invoice['total'] += order.getPrice()
        print(self.invoice['items'])

    def get_client(self, name, address, nip):
        self.invoice['client'] = Client(name, address, nip)

    def get_seller(self, name, address, nip, banknumber):
        self.invoice['seller'] = Seller(name, address, nip, banknumber)

    def generate_number(self):
        self.invoice['number'] = random.randint(1000, 9999)

    def get_payday

    def checkout(self):
        self.invoice['invoiceDate'] = date.today()
        print(self.invoice)


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


class Seller(Client):
    def __init__(self, name, address, nip, banknumber):
        super(Seller, self).__init__(name, address, nip)
        self.banknumber = banknumber


c = Cart()

