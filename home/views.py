from django.shortcuts import render

from .models import Category, Item
# Create your views here.

def get_home(request):
    category = Category.objects.all()
    return render(request, 'home/home.html', {'category': category})