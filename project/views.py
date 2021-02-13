from django.db.models.lookups import IContains, IsNull
from spatialdata.models import Limits
from django.shortcuts import render
from .models import Category, Service
from django.views.generic import ListView
from django.db.models import Q, query
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

    
    
    try:
        distrito = request.GET["distrito"]
    except:
        distrito = ""
    
    try:
        concelho = request.GET["concelho"]
    except:
        concelho = ""
    
   # 
    #if request.GET["distrito"] == None:
     #   request.GET["distrito"] == "none"
   # if request.GET["concelho"] == None:
       # request.GET["concelho"] == "none"
        
    #print(request.GET["search"])
    ##print(request.GET["concelho"])
    
    concelho_polygon = Limits.objects.filter(nome=concelho).values("geom",)
    distrito_polygon = Limits.objects.filter(distrito=distrito).count()
    print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOLA" + str(concelho_polygon))
    #location = Concelho.objects.filter(geom__intersects=context['post'].location).values('nome', 'distrito_title')
    
    services = Service.objects.filter(
        Q(title__icontains=request.GET["search"]) | Q(user__username__icontains=request.GET["search"])
    ).filter(location__intersects=concelho_polygon)
    
    categorias = Category.objects.all()
    #services = Service.objects.all()
    services_count = services.count()

    context = {
        'categorias': categorias,
        'services': services,
        'total_services': services_count,
    }

    return render(request, 'pages/search.html', context=context)