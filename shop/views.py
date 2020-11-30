from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order

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
    if request.method == "POST":
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        phone = form.get('phone')
        desc = form.get('desc')
        con = Contact(name=name, email=email, phone=phone, desc=desc)
        con.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def product_view(request, pid):
    product = Product.objects.filter(id=pid)
    related = Product.objects.filter(prod_category=product[0].prod_category)
    return render(request, 'shop/product_view.html', {'items': {'product': product[0], 'related': related}})


def search(request):
    if request.method == "POST":
        prods = []
        searched_string = request.POST.get('search')
        s = searched_string.lower()
        products = Product.objects.all()
        for i in products:
            if s in i.prod_name.lower() or s in i.prod_desc.lower() or s in i.prod_category.lower() or \
                    s in i.prod_sub_category.lower():
                prods.append(i)
        if prods.__len__() != 0:
            return render(request, 'shop/search.html', {'prods': prods, 's': searched_string})
        else:
            return render(request, 'shop/search_not_found.html', {'s': s})


def checkout(request):
    products = Product.objects.all()
    param = {'products': products}
    if request.method == "POST":
        form = request.POST
        item_json = form.get('items')
        name = form.get('fname') + " " + form.get('lname')
        email = form.get('email')
        phone = form.get('ph')
        address = form.get('address')
        city = form.get('city')
        state = form.get('state')
        zip_code = form.get('zipcode')
        order = Order(item_json=item_json, name=name, email=email, phone=phone, address=address,
                      city=city, state=state, zip_code=zip_code)
        order.save()
        thank = True
        return render(request, 'shop/checkout.html', {'products': products, 'id': order.order_id, 'thank': thank})
    return render(request, 'shop/checkout.html', param)
