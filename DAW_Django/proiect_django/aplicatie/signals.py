from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Produs

@receiver(post_migrate)
def create_custom_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(Produs)
    Permission.objects.get_or_create(
        codename='vizualizeaza_oferta',
        name='Poate vizualiza oferta',
        content_type=content_type,
    )
    
from django.apps import AppConfig

class AplicatieConfig(AppConfig):
    name = 'aplicatie'

    def ready(self):
        import aplicatie.signals