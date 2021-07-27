from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Products
from products.models import Category
from products.forms import ProductsForm
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def main_page_view(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    print(products)
    for i in products:
        print('id:', i.id)
        print('title:', i.title)
        print('price:', i.price)
        print()
    data = {
        'title': 'Главная страница',
        'product_list': products,
        'category_list': categories
    }
    return render(request, 'index.html', context=data)


def product_item_view(request, product_id):
    product = Products.objects.get(id=product_id)
    product_list = Products.objects.all()
    data = {
        'product': product,
        'title': product.title,
        'product_list': product_list
    }
    return render(request, 'item.html', context=data)


def category_item_view(request, category_id):
    products_list = Products.objects.filter(category__id=category_id)
    category_list = Category.objects.all()

    data = {
        'category_list': category_list,
        'product_list': products_list

    }
    return render(request, 'category.html', context=data)


@login_required(login_url='/login/')
def add_product(request):
    if request.method == "GET":
        data = {
            'form': ProductsForm()
        }
        return render(request, 'add.html', context=data)
    elif request.method == "POST":
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/login/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    data = {
        'form': LoginForm
    }
    return render(request, 'login.html', context=data)