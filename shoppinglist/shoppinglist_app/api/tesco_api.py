import requests
import json

from django.conf import settings


class TescoAPI:
    """
    Make calls to the Tesco API.
    """

    def get_request(self, item: str) -> None:
        """
        Make a request to Tesco for an item.
        """

        headers = {"Ocp-Apim-Subscription-Key": settings.TESCO_API_KEY}

        params = {
            "query": item,
            "offset": 0,
            "limit": 10,
        }

        url = "https://dev.tescolabs.com/grocery/products/"

        response = requests.get(url, headers=headers, params=params)

        return response

    def get_item_price(self, item: str) -> float:
        """
        Get the item price from Tesco item price.
        """

        response = self.get_request(item)

        # Get the first item price in the list from Tesco at the moment
        item_price = response.json()["uk"]["ghs"]["products"]["results"][0]["price"]

        return item_price
