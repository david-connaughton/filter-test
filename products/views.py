from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator


# def products(request):
#     if request.method == "POST":
#         tag = request.POST.get('tag')
#         search = Product.objects.filter(tag=tag)
#         return render(request, 'products/products.html', {'products': search})
#     else: 
#         productdisp = Product.objects.all()
#         return render(request, 'products/products.html', {'products': productdisp})


# def products(request):
#     products = Product.objects.all()
#     query = None

#     if 'q' in request.GET:
#         query = request.GET['q']
#         if not query:
#             messages.error(request, "You didn't enter any search criteria!")
#             return redirect(reverse('products'))
#         queries = Q(tag__icontains=query)
#         products = products.filter(queries)

#     context = {
#         'products': products,
#         'search_term': query,
#     }

#     return render(request, 'products/products.html', context)


def products(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(tag__icontains=query)
        ).distinct()
    paginator = Paginator(products, 6)  # 6 posts per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
