import django
import os
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proiect.settings')
django.setup()

from aplicatie.models import CustomUser, Instrument

def delete_unconfirmed_users():
    unconfirmed_users = CustomUser.objects.filter(email_confirmat=False, date_joined__lt=timezone.now() - timedelta(minutes=2))
    count = unconfirmed_users.count()
    unconfirmed_users.delete()
    print(f"{count} unconfirmed users deleted.")

def send_newsletter():
    users = CustomUser.objects.filter(date_joined__lt=timezone.now() - timedelta(minutes=60))
    for user in users:
        send_mail(
            'Weekly Newsletter',
            'Here is the weekly newsletter.',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
    print(f"Newsletter sent to {users.count()} users.")

def custom_task_1():
    # actualizez stocurile produselor
    instruments = Instrument.objects.all()
    for instrument in instruments:
        instrument.stoc = instrument.stoc + 1 
        instrument.save()
    print("Stocurile produselor au fost actualizate.")

def custom_task_2():
    # trimit unui raport zilnic catre administratori
    admins = CustomUser.objects.filter(is_staff=True)
    for admin in admins:
        send_mail(
            'Raport zilnic',
            'Acesta este raportul zilnic al activităților de pe site.',
            settings.DEFAULT_FROM_EMAIL,
            [admin.email],
            fail_silently=False,
        )
    print("Raportul zilnic a fost trimis administratorilor.")