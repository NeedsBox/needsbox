from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView

from spatialdata.models import Limits
from .models import Category, Service, Advertisement
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AddServiceForm, AddAdvertisementForm, UpdateAdvertisementForm
from .forms import UpdateServiceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import random


# Create your views here.


def index(request):
    context = {}

    distritos = Limits.objects.values('distrito', 'distrito_title').distinct().order_by('distrito')

    services = list(Service.objects.all())

    # change 3 to how many random items you want
    random_services = random.sample(services, 4)
    # if you want only a single random item
    # random_item = random.choice(items)

    context = {
        'distritos': distritos,
        'random_services': random_services,
    }

    return render(request, 'index.html', context=context)


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

    categorias = Category.objects.all()
    services_count = services.count()

    context = {
        'categorias': categorias,
        'services': services,
        'total_services': services_count,
    }

    return render(request, 'pages/search.html', context=context)

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
    success_url = reverse_lazy('needsbox:index')
    login_url = reverse_lazy('accounts:login')


class AdvertisementDelete(LoginRequiredMixin, DeleteView):
    model = Advertisement
    success_url = reverse_lazy('needsbox:index')
    login_url = reverse_lazy('accounts:login')

class ServiceDetail(DetailView):
    model = Service
