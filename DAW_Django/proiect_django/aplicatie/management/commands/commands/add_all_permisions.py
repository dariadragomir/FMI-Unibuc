from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from aplicatie.models import CustomUser

class Command(BaseCommand):
    help = 'Atribuie toate permisiunile utilizatorului dariadragomir'

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.get(username='dariadragomir')
        user.is_staff = True
        user.is_superuser = True
        permissions = Permission.objects.all()
        user.user_permissions.set(permissions)
        user.save()
        self.stdout.write(self.style.SUCCESS('Toate permisiunile au fost atribuite utilizatorului dariadragomir'))