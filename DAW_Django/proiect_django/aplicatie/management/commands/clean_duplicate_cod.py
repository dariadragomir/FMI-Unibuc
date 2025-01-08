from django.core.management.base import BaseCommand
from aplicatie.models import CustomUser

class Command(BaseCommand):
    help = 'Curăță valorile duplicate din câmpul cod'

    def handle(self, *args, **kwargs):
        users = CustomUser.objects.all()
        for user in users:
            user.cod = str(user.id)
            user.save()
        self.stdout.write(self.style.SUCCESS('Valorile duplicate din câmpul cod au fost curățate.'))