from django.shortcuts import render, redirect

from .models import ShoppingList
from .forms import ShoppingListForm

from .api.tesco_api import TescoAPI


def home(request):

    if request.method == "POST":

        form = ShoppingListForm(request.POST)

        if form.is_valid():
            form.save()

    items = ShoppingList.objects.all
    return render(request, "home.html", {"items": items})


def delete(request, item_id):

    item = ShoppingList.objects.get(pk=item_id)
    item.delete()

    return redirect("home")


def price(request, item_id):

    item = ShoppingList.objects.get(pk=item_id)

    tesco = TescoAPI()
    price = tesco.get_item_price(item.item)

    item.price = price
    item.save()

    return redirect("home")


def check(request, item_id):

    item = ShoppingList.objects.get(pk=item_id)

    item.check = not item.check
    item.save()

    return redirect("home")
