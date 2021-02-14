from django.shortcuts import render
from .forms import RegisterForm
from django.views import generic
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Account
from project.models import Service

# Create your views here.

# Generic view para criar um novo utilizador
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('needsbox:index')
    
    # Se o utilizador for criado com sucesso envia-se um email de agradecimento pelo registo
    def form_valid(self, form):
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

def profile(request, slug):
    
    user = Account.objects.get(username=slug)
    
    print(user)
    
    services = Service.objects.filter(user=user)
    context = {
        'user': user,
        'services': services,
    }
    return render(request, 'profile.html', context=context)

class AccountDetailView(generic.DetailView):
    model = Account
    slug_field = "username"