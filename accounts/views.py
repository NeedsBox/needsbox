from django.shortcuts import render
from .forms import RegisterForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

# Generic view para criar um novo utilizador
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('needsbox:index')
    
    # Se o utilizador for criado com sucesso envio um email de agradecimento pelo registo
    def form_valid(self, form):
        """message = "Hello {name}, welcome to my Unsplash-Clone made in Django!\n\n Any questions contact me at unsplash@scutelniciuc.xyz\n\nBest regards,\nAlexandru".format(
            name=form.cleaned_data.get('name'),)
        send_mail(
            subject="THANKS FOR REGISTERING",
            message=message,
            from_email='unsplash@scutelniciuc.xyz',
            recipient_list=[form.cleaned_data.get('email')],
        )"""
        return super().form_valid(form)