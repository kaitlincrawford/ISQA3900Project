from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from cart.forms import CartAddProductForm
from .models import Category, Product

now = timezone.now()


def home(request):
    return render(request, 'shop/home.html',
                  {'shop': home})


def aboutus(request):
    return render(request, 'shop/aboutus.html',
                  {'shop': aboutus})


def registration(request):
    return render(request, 'registration/registration.html',
                  {'shop': registration})


@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
