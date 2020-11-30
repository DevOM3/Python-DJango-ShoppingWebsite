from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("product_view/<int:pid>", views.product_view, name="product_view"),
    path("search/", views.search, name="search"),
    path("checkout/", views.checkout, name="checkout"),
    path("categories/", views.categories, name="categories")
]
