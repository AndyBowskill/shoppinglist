from django.test import TestCase

from shoppinglist_app.api.tesco_api import TescoAPI


class TescoAPIClientTests(TestCase):
    def test_get_item_price_when_tesco_found_item(self):
        """
        Test get item price when the item is found in Tesco.
        """

        tesco = TescoAPI()
        price = tesco.get_item_price("tofu")

        self.assertEquals(price, 2.00)
