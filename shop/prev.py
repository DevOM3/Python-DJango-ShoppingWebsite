from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    param = {'products': products}
    return render(request, 'shop/index.html', param)


def categories(request):
    all_products = []
    product_cats = Product.objects.values('prod_category', 'id')
    cats = {items['prod_category'] for items in product_cats}
    for cat in cats:
        products = Product.objects.filter(prod_category=cat)
        all_products.append(products)
    param = {'products': all_products}
    return render(request, "shop/categories.html", param)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def product_view(request, pid):
    product = Product.objects.filter(id=pid)
    related = Product.objects.filter(prod_category=product[0].prod_category)
    return render(request, 'shop/product_view.html', {'product': product[0]})


def search(request):
    return render(request, 'shop/search.html')


def checkout(request):
    return HttpResponse("checkout")
