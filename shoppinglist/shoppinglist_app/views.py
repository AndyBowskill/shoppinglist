from django.shortcuts import render, redirect

from .models import ShoppingList
from .forms import ShoppingListForm


def home(request):
    
    if request.method == "POST":

        form = ShoppingListForm(request.POST)

        if form.is_valid():
            form.save()
            items = ShoppingList.objects.all
            return render(request, "home.html", {"items": items})

    else:
        items = ShoppingList.objects.all
        return render(request, "home.html", {"items": items})


def delete(request, item_id):

    item = ShoppingList.objects.get(pk=item_id)
    item.delete()

    return redirect("home")
