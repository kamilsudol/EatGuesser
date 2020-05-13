from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('results/', views.results, name='search-results'),
    path('subsite/', views.subsite, name='search-subsite'),
]