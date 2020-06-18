from django.db import models
from django.contrib.auth.models import User


class Recipes(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class LikedRecipes(models.Model):
    title = models.CharField(max_length = 100 )
    description = models.TextField()

class ShoppingList(models.Model):
    ingredients = models.TextField()
