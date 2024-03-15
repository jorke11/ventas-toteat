from models.sales import Sales
from datetime import datetime
import math


class ProcessinData():
    def __init__(self, jsonData):
        self.jsonData = jsonData

    def orderData(self, arr, key=1, reverse=True):
        return sorted(arr.items(), key=lambda x: x[key], reverse=reverse)

    def serializeData(self):
        total_sales = 0
        sales_by_product = {}
        total_units_products = 0
        sales_by_category = {}
        sales_by_product_unit = {}
        sales_by_waiter = {}
        sales_by_cashier = {}
        sales_by_zone = {}
        sales_by_table = {}
        sales_by_day = {}
        sales_by_week = {}
        sales_by_month = {}
        total_diners_by_day = {}

        sales = [Sales(p['id'], p['date_closed'], p['date_opened'], p['total'], p['zone'], p['waiter'], p['cashier'], p['table'], p['diners'], p['products'], p['payments'])
                 for p in self.jsonData]
        for sale in sales:
            total_sales += sale.total
            fecha_apertura = datetime.strptime(
                sale.date_opened, '%Y-%m-%d %H:%M:%S')
            closed_date = datetime.strptime(
                sale.date_closed, '%Y-%m-%d %H:%M:%S')
            day = closed_date.date()

            num_week = fecha_apertura.isocalendar()[1]

            if day in total_diners_by_day:
                total_diners_by_day[day] += sale.total
            else:
                total_diners_by_day[day] = sale.total

            if day in sales_by_day:
                sales_by_day[day] += sale.total
            else:
                sales_by_day[day] = sale.total

            if num_week in sales_by_week:
                sales_by_week[num_week] += sale.total
            else:
                sales_by_week[num_week] = sale.total

            if sale.waiter in sales_by_waiter:
                sales_by_waiter[sale.waiter] += sale.total
            else:
                sales_by_waiter[sale.waiter] = sale.total

            if sale.cashier in sales_by_cashier:
                sales_by_cashier[sale.cashier] += sale.total
            else:
                sales_by_cashier[sale.cashier] = sale.total

            if sale.zone in sales_by_zone:
                sales_by_zone[sale.zone] += sale.total
            else:
                sales_by_zone[sale.zone] = sale.total

            if sale.table in sales_by_table:
                sales_by_table[sale.table] += sale.total
            else:
                sales_by_table[sale.table] = sale.total

            for product in sale.products:
                total_sales_product = product.price * product.quantity
                total_units_products += product.quantity

                if product.category in sales_by_category:
                    sales_by_category[product.category] += total_sales_product
                else:
                    sales_by_category[product.category] = total_sales_product

                if product.name in sales_by_product:
                    sales_by_product[product.name] += total_sales_product
                else:
                    sales_by_product[product.name] = total_sales_product

                if product.name in sales_by_product_unit:
                    sales_by_product_unit[product.name] += product.quantity
                else:
                    sales_by_product_unit[product.name] = product.quantity

        sales_by_week = self.orderData(sales_by_week)
        sales_by_category = self.orderData(sales_by_category)
        sales_by_product = self.orderData(sales_by_product)
        sales_by_product_unit = self.orderData(sales_by_product_unit)
        sales_by_waiter = self.orderData(sales_by_waiter)
        sales_by_cashier = self.orderData(sales_by_cashier)
        sales_by_zone = self.orderData(sales_by_zone)
        sales_by_table = self.orderData(sales_by_table)
        sales_by_day = self.orderData(sales_by_day, key=0, reverse=False)
        months = math.ceil(len(sales_by_day)/40)

        return {
            "total_sales": total_sales,
            "months": months,
            "average_by_day": total_sales / len(sales_by_day),
            "sales_by_product": sales_by_product,
            "sales_by_category": sales_by_category,
            "sales_by_product_unit": sales_by_product_unit,
            "sales_by_waiter": sales_by_waiter,
            "sales_by_cashier": sales_by_cashier,
            "sales_by_table": sales_by_table,
            "sales_by_week": sales_by_week,
            "sales_by_day": sales_by_day,
            "total_diners_by_day": total_diners_by_day,
        }
