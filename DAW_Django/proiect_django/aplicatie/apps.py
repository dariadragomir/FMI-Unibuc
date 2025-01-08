from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_offer_permission(sender, **kwargs):
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import CustomUser

    content_type = ContentType.objects.get_for_model(CustomUser)
    Permission.objects.get_or_create(
        codename='vizualizeaza_oferta',
        name='Can view offer',
        content_type=content_type,
    )

class AplicatieConfig(AppConfig):
    name = 'aplicatie'

    def ready(self):
        post_migrate.connect(create_offer_permission, sender=self)