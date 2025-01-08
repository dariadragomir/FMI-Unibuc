from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from aplicatie.models import CustomUser

class Command(BaseCommand):
    help = 'Atribuie permisiunile de administrare utilizatorului dariadragomir'

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.get(username='dariadragomir')
        user.is_staff = True
        permissions = Permission.objects.filter(content_type__app_label='admin')
        user.user_permissions.set(permissions)
        user.save()
        self.stdout.write(self.style.SUCCESS('Permisiunile de administrare au fost atribuite utilizatorului dariadragomir'))