from spatialdata.models import Limits
from django.shortcuts import render
from .models import Category
# Create your views here.

def index(request):
    context = {}
    
    distritos = Limits.objects.values('distrito', 'distrito_title').distinct().order_by('distrito')
    
    context = {
        'distritos': distritos,
    }
    
    return render(request, 'index.html', context=context)

def search(request):
    context = {}

    categorias = Category.objects.all()

    context = {
        'categorias': categorias,
    }

    return render(request, 'pages/search.html', context=context)