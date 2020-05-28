from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
=======

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
>>>>>>> 7a3f3b372e6c30bfb5be3feb2c735d3de519caf8

    def __str__(self):
        return f'{self.user.username} Profile'