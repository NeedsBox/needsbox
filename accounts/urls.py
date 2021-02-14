from django.urls import path, include
from . import views, forms
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:slug>', views.profile,  name="profile"),
    path('<str:slug>', views.AccountDetailView.as_view(template_name='profile.html'), name='detail'),
]

