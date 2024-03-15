import jmespath

"""
    Library extraction with jmespath
"""


class Extraction:

    def __init__(self, jsonData):
        self.jsonData = jsonData

    def getCategories(self):
        return self.getFirstAttribute("[].products[].category")

    def getProducts(self):
        return self.getFirstAttribute("[].products[].name")

    def getMethodPayments(self):
        return self.getFirstAttribute("[].payments[].type")

    def getWaiters(self):
        return self.getFirstAttribute("[].waiter")

    def getCashiers(self):
        return self.getFirstAttribute("[].cashier")

    def getZones(self):
        return self.getFirstAttribute("[].zone")

    def getDiningTable(self):
        return self.getFirstAttribute("[].table")

    def getDiners(self):
        return self.getFirstAttribute("[].diners")

    def getFirstAttribute(self, string_query):
        result = jmespath.search(string_query, self.jsonData)
        result = set(result)
        result = sorted(result, key=None, reverse=False)
        return result
