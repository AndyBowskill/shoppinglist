from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delete/<item_id>", views.delete, name="delete"),
    path("price/<item_id>", views.price, name="price"),
    path("check/<item_id>", views.check, name="check"),
]
