from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def product_list(request, slug=None):
    categories = Category.objects.all()
    current_category = None
    order = request.GET.get('order', 'asc')
    products = Product.objects.filter(available=True)

    if slug:
        current_category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=current_category)

    if order == 'desc':
        products = products.order_by('-price')
    else:
        order = 'asc'
        products = products.order_by('price')

    return render(request,
                  'app/list.html',
                  {'category': current_category,
                   'categories': categories,
                   'products': products,
                   'current_order': order})


def product_details(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(available=True, category=product.category).exclude(id=id)[:4]
    return render(request,
                  'app/product_details.html',
                  {'product': product,
                   'categories': categories,
                   'related_products': related_products})


def price_sort(request):
    categories = Category.objects.all()
    order = request.GET.get('order', 'asc')
    products = Product.objects.filter(available=True)

    if order == 'desc':
        products = products.order_by('-price')
    else:
        order = 'asc'
        products = products.order_by('price')

    return render(request,
                  'app/sort_products.html',
                  {'products': products,
                   'categories': categories,
                   'current_order': order})


