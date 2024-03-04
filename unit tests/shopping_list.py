from shopping_item import ShoppingItem


class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item_name):
        item = ShoppingItem(item_name)
        self.items.append(item)

    def mark_item_as_purchased(self, item_index):
        if 0 <= item_index < len(self.items):
            if not self.items[item_index].check_if_purchased():
                self.items[item_index].mark_as_purchased()
            else:
                raise Exception("Item Already Purchased")
        else:
            raise IndexError("Invalid item index")

    def display_list(self):
        print(f"Shopping List: {self.name}")
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item}")
        print()

    def get_items(self):
        return self.items

