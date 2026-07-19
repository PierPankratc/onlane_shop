from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def product_list(request, slug = None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    current_category = None
    if slug:
        current_category = get_object_or_404(Category, slug = Category.slug)
        current_product = get_object_or_404(category=current_category)

    return render(request, 
                  'products/app/list.html', 
                  {'category': current_category,
                    'categories': categories,
                    'products': products})

def product_details(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug, available=True)
    related_products = Product.objects.filter(available=True, category=product.category).exclude(id=id)[:4]
    return render(request, 
                  'products/app/product_details.html'
                  {'product': product,
                    'related_products': related_products})

