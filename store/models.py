class Product:
    def __init__(self, name: str,  brand: str, model: str, category=None,  color=None, memory: int = 0, price: int = 0):
        self.name = name
        self.color = color
        self.memory = memory
        self.brand = brand
        self.model = model
        self.price = price
        self.category = category

class Category:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name
