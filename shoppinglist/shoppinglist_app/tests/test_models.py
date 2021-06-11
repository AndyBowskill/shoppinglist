from django.test import TestCase

from shoppinglist_app.models import ShoppingList


def create_shopping_list_item():
    return ShoppingList.objects.create(item="Apples.", price=1.69)


class ShoppingListModelTests(TestCase):
    def test_item_max_length(self):
        """
        Test the shopping list item text max length.
        """

        shoppinglist = create_shopping_list_item()
        max_length = shoppinglist._meta.get_field("item").max_length
        self.assertEquals(max_length, 100)

    def test_price_default(self):
        """
        Test the shopping list item price default
        """

        shoppinglist = create_shopping_list_item()
        default_price = shoppinglist._meta.get_field("price").default
        self.assertEquals(default_price, 0)

    def test_price_max_digits(self):
        """
        Test the shopping list item price max digits
        """

        shoppinglist = create_shopping_list_item()
        max_digits = shoppinglist._meta.get_field("price").max_digits
        self.assertEquals(max_digits, 5)

    def test_price_decimal_places(self):
        """
        Test the shopping list item price decimal places
        """

        shoppinglist = create_shopping_list_item()
        decimal_places = shoppinglist._meta.get_field("price").decimal_places
        self.assertEquals(decimal_places, 2)
