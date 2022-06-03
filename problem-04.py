class ReceiptItem:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def get_total(self):
        return self.quantity * self.price


class Receipt:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_subtotal(self):
        sum = 0
        for item in self.items:
            sum += item.get_total()
        return sum

    def get_total(self):
        return self.get_subtotal() * (1 + self.tax_rate)


receipt = Receipt(0.3)
receipt.get_total(),
receipt.add_item(ReceiptItem(2, 6))
receipt.get_total(),
receipt.add_item(ReceiptItem(2, 5))
