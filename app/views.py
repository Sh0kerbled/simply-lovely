from django.shortcuts import render
from .models import Categories, Products

def main_page(request):
    context = {
        'categories': Categories.objects.all(),
        'products': Products.objects.all(),
    }
    return render(request, 'index.html', context)