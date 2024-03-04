class ShoppingItem:
    def __init__(self, name):
        self.name = name
        self.purchased = False

    def mark_as_purchased(self):
        self.purchased = True

    def check_if_purchased(self):
        return self.purchased

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name} {'(Purchased)' if self.purchased else ''}"