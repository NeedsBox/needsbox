import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.models import Account
from spatialdata.models import Limits
from .forms import AddServiceForm, AddAdvertisementForm, UpdateAdvertisementForm
from .forms import UpdateServiceForm
from .models import Category, Service, Advertisement
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    context = {}

    distritos = Limits.objects.values('distrito', 'distrito_title').distinct().order_by('distrito')

    services = list(Service.objects.all())
    services_count = Service.objects.all().count()
    ad_count = Advertisement.objects.all().count()

    users = Account.objects.all().count()

    by_location = []
    for x in services:
        limits = Limits.objects.filter(geom__intersects=x.location).values('nome', 'distrito_title')
        if limits[0]['distrito_title'] == "Aveiro":
            by_location.append(x)

    random_services = random.sample(by_location, 4)
    recent_services = Service.objects.all().order_by('-created_at')[:4]
    best_services = []

    for service in services:
        best_services.append(service.get_average_review_for_index())

    best_services_r = []
    best_services = sorted(best_services, key=lambda i: i['average'], reverse=True)
    best_services = best_services[:4]
    for b_service in best_services:
        best_services_r.append(b_service['service'])

    context = {
        'distritos': distritos,
        'random_services': random_services,
        'recent_services': recent_services,
        'best_services': best_services_r,
        'users': users,
        'services_count': services_count,
        'ad_count': ad_count,
    }

    return render(request, 'index.html', context=context)




    # class ServiceCreate(CreateView):
    model = Service
    form_class = AddServiceForm


# View para criar um Post
class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    form_class = AddServiceForm
    success_url = reverse_lazy('needsbox:index')
    login_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ServiceUpdate(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = UpdateServiceForm
    template_name = 'project/service_update_form.html'

    success_url = reverse_lazy('needsbox:index')
    login_url = reverse_lazy('accounts:login')


class ServiceDelete(LoginRequiredMixin, DeleteView):
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('needsbox:index')


class AdvertisementCreate(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AddAdvertisementForm
    success_url = reverse_lazy('needsbox:index')
    login_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdvertisementUpdate(LoginRequiredMixin, UpdateView):
    model = Advertisement
    form_class = UpdateAdvertisementForm
    template_name = 'project/advertisement_update_form.html'
    success_url = reverse_lazy('needsbox:index')
    login_url = reverse_lazy('accounts:login')


class AdvertisementDelete(LoginRequiredMixin, DeleteView):
    model = Advertisement
    success_url = reverse_lazy('needsbox:index')
    login_url = reverse_lazy('accounts:login')


class ServiceDetail(DetailView):
    model = Service


def about(request):
    return render(request, 'pages/about.html')

def search_ad(request):
    context = {}

    #concelho_polygon = Limits.objects.filter(nome=concelho).values("geom", )
    #distrito_polygon = Limits.objects.filter(distrito=distrito).count()

    """if concelho != "none":
        ads = Advertisement.objects.filter(
            Q(title__icontains=request.GET["search"]) | Q(user__username__icontains=request.GET["search"])
        ).filter(location__intersects=concelho_polygon)
    else:
    
    try:
        ads = Advertisement.objects.filter(
            Q(title__icontains=request.GET["search"]) | Q(user__username__icontains=request.GET["search"])
        )
    except:
        ads = Advertisement.objects.all()"""
    
    distritos = Limits.objects.values('distrito', 'distrito_title').distinct().order_by('distrito')
    
    try:
        distrito = request.GET["distrito"]
    except:
        distrito = "none"

    try:
        concelho = request.GET["concelho"]
    except:
        concelho = "none"

    try:
        concelho_polygon = Limits.objects.filter(nome=concelho).values("geom", )
        distrito_polygon = Limits.objects.filter(distrito=distrito).count()

        if concelho != "none":
            ads = Advertisement.objects.filter(
                Q(title__icontains=request.GET["search"]) | Q(user__username__icontains=request.GET["search"])
            ).filter(location__intersects=concelho_polygon)
        else:
            ads = Advertisement.objects.filter(
                Q(title__icontains=request.GET["search"]) | Q(user__username__icontains=request.GET["search"])
            )
    except:
        ads = Advertisement.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(ads, 5)

    categorias = Category.objects.all()
    ads_count = ads.count()
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'categorias': categorias,
        'services': users,
        'total_services': ads_count,
        'users': users,
        'distritos': distritos,
    }

    return render(request, 'pages/search-ad.html', context=context)

def search(request):
    context = {}

    try:
        distrito = request.GET["distrito"]
    except:
        distrito = "none"

    try:
        concelho = request.GET["concelho"]
    except:
        concelho = "none"

    try:
        concelho_polygon = Limits.objects.filter(nome=concelho).values("geom", )
        distrito_polygon = Limits.objects.filter(distrito=distrito).count()

        if concelho != "none":
            services = Service.objects.filter(
                Q(title__icontains=request.GET["search"]) | Q(user__username__icontains=request.GET["search"])
            ).filter(location__intersects=concelho_polygon)
        else:
            services = Service.objects.filter(
                Q(title__icontains=request.GET["search"]) | Q(user__username__icontains=request.GET["search"])
            )
    except:
        services = Service.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(services, 9)

    categorias = Category.objects.all()
    services_count = services.count()
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'categorias': categorias,
        'services': users,
        'total_services': services_count,
        'users': users,
    }

    return render(request, 'pages/search.html', context=context)
