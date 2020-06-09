from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='search-home'),
    path('results/', views.results, name='search-results'),
    path('subsite/', views.subsite, name='search-subsite'),
    path('liked_recipes/', views.liked_recipes, name='search-likedrecipes'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)