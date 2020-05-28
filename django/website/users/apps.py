from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
<<<<<<< HEAD
        import users.signals
=======
        import users.signals
        
>>>>>>> 7a3f3b372e6c30bfb5be3feb2c735d3de519caf8
