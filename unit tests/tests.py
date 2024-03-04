import unittest
from shopping_list_app import ShoppingListApp


class TestShoppingListApp(unittest.TestCase):
    def setUp(self):
        self.app = ShoppingListApp()

    def test_create_shopping_list(self):
        self.app.create_shopping_list("Groceries")
        self.assertTrue("Groceries" in self.app.shopping_lists)

    def test_add_item_to_list(self):
        self.app.create_shopping_list("Groceries")
        self.app.add_item_to_list("Groceries", "Apples")
        items = self.app.shopping_lists["Groceries"].get_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].get_name(), "Apples")

    def test_mark_item_as_purchased(self):
        self.app.create_shopping_list("Groceries")
        self.app.add_item_to_list("Groceries", "Apples")
        self.app.mark_item_as_purchased("Groceries", "Apples")
        items = self.app.shopping_lists["Groceries"].get_items()
        self.assertTrue(items[0].check_if_purchased())

    def test_fail_mark_item_as_purchased(self):
        # This test case will fail because we're trying to mark an item as purchased
        # which doesn't exist in the list
        self.app.create_shopping_list("Groceries")
        self.app.add_item_to_list("Groceries", "Apples")
        with self.assertRaises(IndexError):
            self.app.mark_item_as_purchased("Groceries", "Bananas")


if __name__ == '__main__':
    unittest.main()
