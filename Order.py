from Product import Product

class Order:
    orderNum = 0

    def __init__(self, products):
        Order.orderNum += 1
        self._idOrder = Order.orderNum
        self._products = list(products)

    def addProduct(self, product):
        self._products.append(product)
    
    def totalValue(self):
        total = 0
        for i in self._products:
            total += i.getPrice
        return "{0:.2f}".format(total)

    def __str__(self):
        productsOrder = ""
        for i in self._products:
            if productsOrder == "":
                productsOrder += i.__str__()
            else:
                productsOrder +=  "  |  " + i.__str__()
        return f"OrderID [{self._idOrder}]: \n Products: [{productsOrder}] \n Total Price: {self.totalValue()}"

Keyboard = Product("Keyboard", 12.99)
Mouse = Product("Mouse", 16.99)
Screen = Product("Screen", 129.99)
Mousepad = Product("Mousepad", 8.99)

usualOrder = [Keyboard, Mouse, Screen]
Order1 = Order(usualOrder)
print(Order1)

Order1.addProduct(Mousepad)
print(Order1)