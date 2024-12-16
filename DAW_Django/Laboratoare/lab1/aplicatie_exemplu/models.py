from django.db import models
from django.contrib.auth.models import AbstractUser

import sys
sys.path.append('/Users/dariadragomir/Facultate/AN2/SEM1/Django/Lab1/')

class Festival(models.Model):
    cod_festival = models.CharField(max_length=50)
    denumire = models.CharField(max_length=100)
    eveniment_muzical = models.CharField(max_length=100)

    def __str__(self):
        return self.denumire

class Locatie(models.Model):
    cod_locatie = models.CharField(max_length=50)
    oras = models.CharField(max_length=50)

    def __str__(self):
        return self.oras

class Partener(models.Model):
    cod_partener = models.CharField(max_length=50)
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume
class Concert(models.Model):
    partener = models.ForeignKey(Partener, on_delete=models.CASCADE)
    locatie = models.ForeignKey(Locatie, on_delete=models.CASCADE)
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    cod_concert = models.CharField(max_length=50)

    def __str__(self):
        return self.cod_concert

class Scena(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    nume = models.CharField(max_length=50)

    def __str__(self):
        return self.nume

class TipBilet(models.Model):
    cod_bilet = models.CharField(max_length=50)
    tip = models.CharField(max_length=50)

    def __str__(self):
        return self.tip

class Bilet(models.Model):
    cod_bilet = models.ForeignKey(TipBilet, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

class Client(models.Model):
    cod_bilet = models.ForeignKey(Bilet, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class Repertoriu(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

class Piesa(models.Model):
    cod_repertoriu = models.ForeignKey(Repertoriu, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class Artist(models.Model):
    cod_piesa = models.ForeignKey(Piesa, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)

    def __str__(self):
        return self.nume

class CustomUser(AbstractUser):
    telefon = models.CharField(max_length=15, blank=True)

