import httpretty

from django.test import TestCase

from shoppinglist_app.api.tesco_api import TescoAPI


class TescoAPIClientTests(TestCase):
    @httpretty.activate
    def test_get_request_is_successful(self):

        httpretty.register_uri(
            method=httpretty.GET,
            uri="https://dev.tescolabs.com/grocery/products/",
            status=200,
        )

        tesco = TescoAPI()
        response = tesco.get_request("tofu")

        self.assertEqual(response.status_code, 200)
