from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def categories_view(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'category/categories_list.html', context=context)


def products_for_categories(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'category': category
    }

    return render(request, 'product/products_list.html', context=context)


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }

    return render(request, 'product/detail.html', context=context)