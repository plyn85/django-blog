from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
# import signals file here
    def ready(self):
        import users.signals


