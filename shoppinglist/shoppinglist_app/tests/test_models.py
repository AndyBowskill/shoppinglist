from django.test import TestCase

from shoppinglist_app.models import ShoppingList


class ShoppingListModelTests(TestCase):
    """
    Tests for the shopping list model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Setup the test database one time
        """
        cls.shoppinglist_item = ShoppingList.objects.create(item="Apples.", price=1.69)

    def test_item_max_length(self):
        """
        Test the shopping list item text max length.
        """

        max_length = self.shoppinglist_item._meta.get_field("item").max_length
        self.assertEquals(max_length, 100)

    def test_price_default(self):
        """
        Test the shopping list item price default
        """

        default_price = self.shoppinglist_item._meta.get_field("price").default
        self.assertEquals(default_price, 0)

    def test_price_max_digits(self):
        """
        Test the shopping list item price max digits
        """

        max_digits = self.shoppinglist_item._meta.get_field("price").max_digits
        self.assertEquals(max_digits, 5)

    def test_price_decimal_places(self):
        """
        Test the shopping list item price decimal places
        """

        decimal_places = self.shoppinglist_item._meta.get_field("price").decimal_places
        self.assertEquals(decimal_places, 2)
