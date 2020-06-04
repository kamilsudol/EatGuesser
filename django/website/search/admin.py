from django.contrib import admin
from .models import Recipes, LikedRecipes

admin.site.register(Recipes)
admin.site.register(LikedRecipes)
# admin.site.register(Profile)