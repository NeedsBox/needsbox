from spatialdata.models import Limits
from django.shortcuts import render
from .models import Category, Service
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
    services = Service.objects.all()
    services_count = services.count()

    context = {
        'categorias': categorias,
        'services': services,
        'total_services': services_count,
    }

    return render(request, 'pages/search.html', context=context)