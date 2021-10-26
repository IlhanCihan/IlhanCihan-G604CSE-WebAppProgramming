class Product:
    def __init__(self, name=None, description=None, price=None):
        self.name = name
        self.description = description
        self.price = price

    def edit(self, name=None, description=None, price=None):
        if name is not None:
            self.name = name
        if description is not None and description.strip() != "":
            self.description = description
        if price is not None and price > 0:
            self.price = price
