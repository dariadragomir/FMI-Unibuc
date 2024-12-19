from django.db import models as mdl

class Categorie(mdl.Model):
    nume = mdl.CharField(max_length=50, unique=True)
    descriere = mdl.TextField(blank=True, null=True)

    def __str__(self):
        return self.nume

class Brand(mdl.Model):
    nume = mdl.CharField(max_length=50, unique=True)
    tara_origine = mdl.CharField(max_length=50, blank=True, null=True)
    data_infiintare = mdl.DateField(blank=True, null=True)

    def __str__(self):
        return self.nume
class Material(mdl.Model):
    nume = mdl.CharField(max_length=50, unique=True)
    descriere = mdl.TextField(blank=True, null=True)

    def __str__(self):
        return self.nume

class Instrument(mdl.Model):
    nume = mdl.CharField(max_length=50, unique=True)
    descriere = mdl.TextField(blank=True, null=True)
    pret = mdl.DecimalField(max_digits=8, decimal_places=2, blank=True)
    stoc = mdl.IntegerField(default=0, blank=True)
    categorie = mdl.ForeignKey('Categorie', on_delete=mdl.CASCADE, blank=True)
    brand = mdl.ForeignKey('Brand', on_delete=mdl.CASCADE)
    materiale = mdl.ManyToManyField('Material', related_name='instrumente', blank=True)
    data_adaugare = mdl.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.nume

class Accesoriu(mdl.Model):
    nume = mdl.CharField(max_length=50, unique=True)
    descriere = mdl.TextField(blank=True, null=True)
    pret = mdl.DecimalField(max_digits=8, decimal_places=2)
    instrument = mdl.ForeignKey('Instrument', on_delete=mdl.CASCADE)

    def __str__(self):
        return self.nume

class Comanda(mdl.Model):
    nume_client = mdl.CharField(max_length=100)
    data_comanda = mdl.DateTimeField(auto_now_add=True)
    total = mdl.DecimalField(max_digits=10, decimal_places=2)
    instrumente = mdl.ManyToManyField('Instrument', through='ComandaInstrument')

    def __str__(self):
        return f"Comanda {self.id} - {self.nume_client}"

class ComandaInstrument(mdl.Model):
    comanda = mdl.ForeignKey('Comanda', on_delete=mdl.CASCADE)
    instrument = mdl.ForeignKey('Instrument', on_delete=mdl.CASCADE)
    cantitate = mdl.IntegerField()

    def __str__(self):
        return f"{self.cantitate}x {self.instrument.nume} in comanda {self.comanda.id}"

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username