from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('subsite/', views.subsite, name='search-subsite'),
]