class Product:
    nProducts = 0

    @property
    def getPrice(self):
        return self._price

    @classmethod
    def getId(cls):
        Product.nProducts += 1

    def __init__(self, name, price):
        self.getId()
        self._id = Product.nProducts
        self._name = name
        self._price = price
    def __str__(self):
        return f"ID [{self._id}], Name [{self._name}], Price [{self._price}]"

if __name__ == "__main__":
    Keyboard = Product("Keyboard", 12.99)
    Mouse = Product("Mouse", 16.99)
    print(Keyboard)
    print(Mouse)

