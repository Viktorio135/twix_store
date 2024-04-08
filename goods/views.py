from django.shortcuts import render
from django.core.paginator import Paginator

from goods.models import Categories, Product


def shop(request, slug):

    page = int(request.GET.get('page', 1))
    
    categories = Categories.objects.all()
    if slug != 'all': 
        products = Product.objects.filter(category__slug=slug)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 6)
    current_page = paginator.page(page)

    context = {
        'categories': categories,
        'products': current_page
    }
    return render(request, 'goods/shop.html', context=context)
