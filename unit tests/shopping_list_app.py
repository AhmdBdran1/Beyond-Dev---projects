from shopping_list import ShoppingList


class ShoppingListApp:
    def __init__(self):
        self.shopping_lists = {}

    def create_shopping_list(self, list_name):
        if list_name in self.shopping_lists:
            print("Shopping list with that name already exists.")
        else:
            self.shopping_lists[list_name] = ShoppingList(list_name)
            print(f"Shopping list '{list_name}' created successfully.")

    def add_item_to_list(self, list_name, item_name):
        try:
            self.shopping_lists[list_name].add_item(item_name)
            print(f"Item '{item_name}' added to '{list_name}' successfully.")
        except KeyError:
            print(f"Shopping list '{list_name}' does not exist.")

    def mark_item_as_purchased(self, list_name, item_name):
        try:
            shopping_list = self.shopping_lists[list_name].get_items()
            for idx, item in enumerate(shopping_list):
                if item.name.lower() == item_name.lower():
                    try:
                        self.shopping_lists[list_name].mark_item_as_purchased(idx)
                        print(f"Item '{item_name}' marked as purchased.")
                    except Exception as e:
                        print(f"Error: {e}")
                    return
            print(f"Item '{item_name}' does not exist in Shopping list '{list_name}'")
        except KeyError:
            print(f"Shopping list '{list_name}' does not exist.")

    def display_all_lists(self):
        if not self.shopping_lists:
            print("No shopping lists available.")
        else:
            for shopping_list in self.shopping_lists.values():
                shopping_list.display_list()
