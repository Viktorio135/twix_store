from django.shortcuts import render

from goods.models import Product


def index(request):

    products = Product.objects.all()

    context = {
        'products': products[:3],
    }

    return render(request, "main/index.html", context=context)

