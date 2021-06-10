from django.test import TestCase

from shoppinglist_app.models import ShoppingList


def create_shopping_list_item():
    return ShoppingList.objects.create(item="Apples.")


class ShoppingListModelTests(TestCase):
    def test_item_max_length(self):
        """
        Test the shopping list item text max length
        """

        shoppinglist = create_shopping_list_item()
        max_length = shoppinglist._meta.get_field("item").max_length
        self.assertEquals(max_length, 100)
