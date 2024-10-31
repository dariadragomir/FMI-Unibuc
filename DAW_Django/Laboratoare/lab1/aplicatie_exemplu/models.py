from django.db import models

# Create your models here.
from django.db import models
import uuid

class Organizator(models.Model):
    nume = models.CharField(max_length=100)
    email = models.EmailField()

class Locatie(models.Model):
    adresa = models.CharField(max_length=255)
    oras = models.CharField(max_length=100)
    judet = models.CharField(max_length=100)
    cod_postal = models.CharField(max_length=10)


class Prajitura(models.Model):
    nume = models.CharField(max_length=50, unique=True)
    descriere = models.TextField(blank=True, null=True)
    pret = models.DecimalField(max_digits=8, decimal_places=2)
    gramaj = models.IntegerField()
    tip_produs = models.CharField(max_length=50, default='cofetarie')
    calorii = models.IntegerField()
    categorie = models.CharField(max_length=50, default='comuna')
    pt_diabetici = models.BooleanField(default=False)
    imagine = models.CharField(max_length=300, blank=True, null=True)
    data_adaugare = models.DateTimeField(auto_now_add=True)