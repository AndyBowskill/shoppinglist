from django.test import TestCase
from django.urls import reverse

from shoppinglist_app.views import home, delete

from shoppinglist_app.models import ShoppingList


def create_shopping_list_item():
    return ShoppingList.objects.create(item="Oranges.")


class ShoppingListViewsTests(TestCase):
    def test_home_no_shopping_list_items(self):
        """
        Test home page works successfully when the shopping list is empty.
        """

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shopping list is empty.")

    def test_home_shopping_list_is_populated(self):
        """
        Test home page works successfully when the shopping list is populated.
        """

        create_shopping_list_item()

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oranges.")

    def test_delete_shopping_list_item_is_deleted(self):
        """
        Test that the delete view deletes the valid shopping list item.
        """

        shopping_list_item = create_shopping_list_item()

        response = self.client.post(
            reverse("delete", args=(shopping_list_item.id,)), follow=True
        )
        self.assertEqual(response.status_code, 200)
