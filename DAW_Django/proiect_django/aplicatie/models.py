from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Categorie(models.Model):
    nume = models.CharField(max_length=50, unique=True)
    descriere = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nume

class Brand(models.Model):
    nume = models.CharField(max_length=50, unique=True)
    tara_origine = models.CharField(max_length=50, blank=True, null=True)
    data_infiintare = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nume

class Material(models.Model):
    nume = models.CharField(max_length=50, unique=True)
    descriere = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nume

class Instrument(models.Model):
    nume = models.CharField(max_length=50, unique=True)
    descriere = models.TextField(blank=True, null=True)
    pret = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    stoc = models.IntegerField(default=0, blank=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    materiale = models.ManyToManyField('Material', related_name='instrumente', blank=True)
    data_adaugare = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nume
    

class Accesoriu(models.Model):
    nume = models.CharField(max_length=50, unique=True)
    descriere = models.TextField(blank=True, null=True)
    pret = models.DecimalField(max_digits=8, decimal_places=2)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    def __str__(self):
        return self.nume

class Comanda(models.Model):
    nume_client = models.CharField(max_length=100)
    data_comanda = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    instrumente = models.ManyToManyField('Instrument', through='ComandaInstrument')

    def __str__(self):
        return f"Comanda {self.id} - {self.nume_client}"

class ComandaInstrument(models.Model):
    comanda = models.ForeignKey('Comanda', on_delete=models.CASCADE)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    cantitate = models.IntegerField()

    def __str__(self):
        return f"{self.cantitate}x {self.instrument.nume} in comanda {self.comanda.id}"

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    cod = models.CharField(max_length=100, blank=True, null=True)
    email_confirmat = models.BooleanField(default=False)
    blocat = models.BooleanField(default=False) 

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

    def save(self, *args, **kwargs):
        if not self.cod:
            self.cod = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
def create_offer_permission():
    content_type = ContentType.objects.get_for_model(CustomUser)
    permission, created = Permission.objects.get_or_create(
        codename='vizualizeaza_oferta',
        name='Can view offer',
        content_type=content_type,
    )

class Vizualizare(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    data_vizualizare = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_vizualizare']
        db_table = 'aplicatie_vizualizari'

class Promotie(models.Model):
    nume = models.CharField(max_length=255)
    data_creare = models.DateTimeField(auto_now_add=True)
    data_expirare = models.DateTimeField()
    subiect = models.CharField(max_length=255)
    mesaj = models.TextField()
    categorii = models.ManyToManyField(Categorie)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    cod_promotie = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nume

from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.instrument.name}"
    
from django.utils.timezone import now

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(default=now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    instrument = models.ForeignKey(Instrument, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.instrument.nume} (Order {self.order.id})"