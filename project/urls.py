from django.urls import path

from . import views

app_name = 'needsbox'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    # path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
