from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from project.models import Service
from .forms import RegisterForm
from .models import Account, PublicContacts


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


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


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


def user_delete_view(request, username):
    obj = get_object_or_404(Account, username=username)
    if request.method == "POST":
        obj.delete()
        return redirect('needsbox:index')
    context = {
        "object": obj
    }
    return render(request, 'user_delete.html', context)
