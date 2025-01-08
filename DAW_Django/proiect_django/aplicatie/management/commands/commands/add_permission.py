from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from aplicatie.models import CustomUser

class Command(BaseCommand):
    help = 'Adaugă permisiunea add_produs utilizatorului dariadragomir'

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.get(username='dariadragomir')
        permission = Permission.objects.get(codename='add_produs')
        user.user_permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('Permisiunea add_produs a fost adăugată utilizatorului dariadragomir'))