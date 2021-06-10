import requests
import json


class TescoAPI:
    """
    Class to make calls to the Tesco API.
    """

    response = ""

    def __init__(self):
        self.APIKey = "fb3bbf71931c4ad8b75c6a0688ef7d88"

    def get_request(self, item):
        """
        Make a request to Tesco API for an item.
        """

        headers = {"Ocp-Apim-Subscription-Key": self.APIKey}

        params = {
            "query": item,
            "offset": 0,
            "limit": 10,
        }

        url = "https://dev.tescolabs.com/grocery/products/"

        self.response = requests.get(url, headers=headers, params=params)

    def get_item_price(self, item):
        """
        Get the item price from Tesco item price.
        """

        self.get_request(item)

        # Get the first item price in the list from Tesco at the moment
        item_price = self.response.json()["uk"]["ghs"]["products"]["results"][0][
            "price"
        ]

        return item_price
