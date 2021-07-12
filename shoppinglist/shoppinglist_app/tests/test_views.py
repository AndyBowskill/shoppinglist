from django.test import TestCase, Client
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

    def test_create_shopping_list_item_is_created(self):
        """
        Test that the 'Add' button creates the valid shopping list item.
        """

        response = self.client.post(reverse("home"), data={"item": "Bananas"})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ShoppingList.objects.count(), 1)

    def test_create_shopping_list_item_is_not_created(self):
        """
        Test that the 'Add' button didn't create the invalid shopping list item.
        """

        response = self.client.post(reverse("home"), data={"item": ""})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ShoppingList.objects.count(), 0)

    def test_delete_shopping_list_item_is_deleted(self):
        """
        Test that the delete view deletes the valid shopping list item.
        """

        shopping_list_item = create_shopping_list_item()

        response = self.client.get(
            reverse("delete", args=(shopping_list_item.id,)), follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ShoppingList.objects.count(), 0)

    def test_shopping_list_item_is_checked(self):
        """
        Test that the check view checked the valid shopping list item.
        """

        shopping_list_item = create_shopping_list_item()

        response = self.client.get(
            reverse("check", args=(shopping_list_item.id,)), follow=True
        )

        self.assertEqual(response.status_code, 200)

        shopping_list_item_after = ShoppingList.objects.get(pk=shopping_list_item.id)

        self.assertEqual(shopping_list_item_after.check, True)
