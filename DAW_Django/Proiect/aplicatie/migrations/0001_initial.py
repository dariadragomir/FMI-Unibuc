# Generated by Django 5.1.1 on 2024-12-18 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50, unique=True)),
                ('tara_origine', models.CharField(blank=True, max_length=50, null=True)),
                ('data_infiintare', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50, unique=True)),
                ('descriere', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_client', models.CharField(max_length=100)),
                ('data_comanda', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50, unique=True)),
                ('descriere', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50, unique=True)),
                ('descriere', models.TextField(blank=True, null=True)),
                ('pret', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('stoc', models.IntegerField(blank=True, default=0)),
                ('data_adaugare', models.DateTimeField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicatie.brand')),
                ('categorie', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='aplicatie.categorie')),
                ('materiale', models.ManyToManyField(blank=True, related_name='instrumente', to='aplicatie.material')),
            ],
        ),
        migrations.CreateModel(
            name='ComandaInstrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantitate', models.IntegerField()),
                ('comanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicatie.comanda')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicatie.instrument')),
            ],
        ),
        migrations.AddField(
            model_name='comanda',
            name='instrumente',
            field=models.ManyToManyField(through='aplicatie.ComandaInstrument', to='aplicatie.instrument'),
        ),
        migrations.CreateModel(
            name='Accesoriu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50, unique=True)),
                ('descriere', models.TextField(blank=True, null=True)),
                ('pret', models.DecimalField(decimal_places=2, max_digits=8)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicatie.instrument')),
            ],
        ),
    ]