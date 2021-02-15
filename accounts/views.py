from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views import generic
from django.shortcuts import render

from .forms import RegisterForm
from .models import Account, PublicContacts
from project.models import Service


# Create your views here.

# Generic view para criar um novo utilizador
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('needsbox:index')

    # Se o utilizador for criado com sucesso envio um email de agradecimento pelo registo
    def form_valid(self, form):
        message = "Hello {name}, welcome to my Unsplash-Clone made in Django!\n\n Any questions contact me at unsplash@scutelniciuc.xyz\n\nBest regards,\nAlexandru".format(
            name=form.cleaned_data.get('name'), )
        html_message = render_to_string('email.html', {'nome': form.cleaned_data.get('name')})
        plain_message = strip_tags(html_message)
        send_mail(
            subject="THANKS FOR REGISTERING",
            message=plain_message,
            html_message=html_message,
            from_email='system@scutelniciuc.xyz',
            recipient_list=[form.cleaned_data.get('email')],
        )
        return super().form_valid(form)

class AccountDetailView(generic.DetailView):
    model = Account
    slug_field = "username"

def profile(request, username):
    context = {}
    
    
    try:
        user = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return render(request, 'pages/404-error.html', context=context)
    
    if user.get_type() != 'PRO':
        return render(request, 'pages/404-error.html', context=context)
    
    services = Service.objects.filter(user=user)
    
    try:
        public_contacts = PublicContacts.objects.get(user=user)
    except PublicContacts.DoesNotExist:
        public_contacts = 0
    review_count = 0
    service_count = 0
    
    for service in services:
        service_count += 1
        review_count += service.get_reviews_count()
    
    context = {
        'user': user,
        'services': services,
        'review_count': review_count,
        'service_count': service_count,
        'contacts': public_contacts,
    }
    
    return render(request, 'profile.html', context=context)