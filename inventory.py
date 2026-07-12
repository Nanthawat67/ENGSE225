class Inventory:

    def __init__(self):
        self.products = {}

    def add_product(self, name, price, stock):
        self.products[name] = {
            "price": price,
            "stock": stock
        }

    def update_product(self, name, stock):
        if name in self.products:
            self.products[name]["stock"] = stock
            return True
        return False

    def remove_stock(self, name, amount):
        if name in self.products:
            if self.products[name]["stock"] >= amount:
                self.products[name]["stock"] -= amount
                return True
        return False

    def total_value(self):
        total = 0
        for product in self.products.values():
            total += product["price"] * product["stock"]

        return total
