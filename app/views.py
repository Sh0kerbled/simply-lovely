from django.shortcuts import render
from .models import Categories

def main_page(request):
    context = {
        'title': Categories.objects.all()
    }
    return render(request, 'index.html')