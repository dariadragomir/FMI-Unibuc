from django.contrib import admin
from aplicatie.models import Categorie, Brand, Material, Instrument, Accesoriu, Comanda, ComandaInstrument, CustomUser, Vizualizare, Promotie
import os
from django.conf import settings

# Ensure DJANGO_SETTINGS_MODULE is set correctly (do not call settings.configure)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proiect_django.settings')

admin.site.site_header = "Administrare Magazin Instrumente Muzicale"
admin.site.site_title = "Panou Admin Magazin"
admin.site.index_title = "Administrare Modele"

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere') 
    search_fields = ('nume',) 

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tara_origine', 'data_infiintare')
    search_fields = ('nume',)
    list_filter = ('tara_origine',)  

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere')
    search_fields = ('nume',)
from django.contrib import admin
from .models import Instrument, Vizualizare, Promotie, Brand, Categorie

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('nume', 'categorie', 'brand', 'pret', 'stoc', 'data_adaugare')
    search_fields = ('nume', 'descriere') 
    list_filter = ('categorie', 'brand', 'pret', 'stoc', 'data_adaugare') 
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            try:
                price_range = search_term.split('-')
                if len(price_range) == 2:
                    min_price, max_price = float(price_range[0]), float(price_range[1])
                    queryset = queryset.filter(pret__gte=min_price, pret__lte=max_price)
            except ValueError:
                pass
        return queryset, use_distinct

admin.site.register(Vizualizare)
admin.site.register(Promotie)

@admin.register(Accesoriu)
class AccesoriuAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere', 'pret', 'instrument')
    search_fields = ('nume',)

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    list_display = ('nume_client', 'data_comanda', 'total')
    search_fields = ('nume_client',)
    list_filter = ('data_comanda',)  

@admin.register(ComandaInstrument)
class ComandaInstrumentAdmin(admin.ModelAdmin):
    list_display = ('comanda', 'instrument', 'cantitate')
    search_fields = ('comanda__nume_client', 'instrument__nume') 

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'email_confirmat', 'cod')
    search_fields = ('username', 'email', 'first_name', 'last_name')


#admin.site.register(InstrumentAdmin)
