from django.contrib.auth import views as auth_views
from django.urls import path

from . import views, forms

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
