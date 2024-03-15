# import models.product as Product
from models.product import Product
from models.payments import Payment

print("LLEGO SALES")


class Sales:
    def __init__(self, id, date_closed, date_opened, total, zone, waiter, cashier, table, diners, products, payments):
        self.id = id
        self.date_opened = date_opened
        self.date_closed = date_closed
        self.total = total
        self.zone = zone
        self.zone = zone
        self.waiter = waiter
        self.cashier = cashier
        self.diners = diners
        self.table = table
        self.products = [Product(p['category'], p['price'], p['name'], p['quantity'])
                         for p in products]
        self.payments = [Payment(p['amount'], p['type'])
                         for p in payments]
