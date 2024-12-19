from django.contrib import admin
from aplicatie.models import Categorie, Brand, Material, Instrument, Accesoriu, Comanda, ComandaInstrument
import os
from django.conf import settings

# Ensure DJANGO_SETTINGS_MODULE is set correctly (do not call settings.configure)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proiect_django.settings')

# Personalizarea titlurilor și header-ului din panoul admin
admin.site.site_header = "Administrare Magazin Instrumente Muzicale"
admin.site.site_title = "Panou Admin Magazin"
admin.site.index_title = "Administrare Modele"

# Interfață admin pentru Categorie
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere')  # Afișare câmpuri
    search_fields = ('nume',)  # Căutare după nume

# Interfață admin pentru Brand
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tara_origine', 'data_infiintare')
    search_fields = ('nume',)
    list_filter = ('tara_origine',)  # Filtru lateral după țara de origine

# Interfață admin pentru Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere')
    search_fields = ('nume',)

# Interfață admin pentru Instrument
@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('nume', 'categorie', 'brand', 'pret', 'stoc', 'data_adaugare')
    search_fields = ('nume', 'descriere') 
    list_filter = ('categorie', 'brand', 'pret', 'stoc', 'data_adaugare') 
    
    def get_search_results(self, request, queryset, search_term):
        if search_term:
            try:
                price_range = search_term.split('-')
                if len(price_range) == 2:
                    min_price, max_price = float(price_range[0]), float(price_range[1])
                    queryset = queryset.filter(pret__gte=min_price, pret__lte=max_price)
            except ValueError:
                pass
        return queryset

    list_per_page = 5  

    fieldsets = (
        ("Informații de bază", {'fields': ('nume', 'descriere', 'categorie', 'brand')}),
        ("Detalii suplimentare", {'fields': ('pret', 'stoc', 'materiale', 'data_adaugare')}),
    )


# Interfață admin pentru Accesoriu
@admin.register(Accesoriu)
class AccesoriuAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere', 'pret', 'instrument')
    search_fields = ('nume',)

# Interfață admin pentru Comanda
@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    list_display = ('nume_client', 'data_comanda', 'total')
    search_fields = ('nume_client',)
    list_filter = ('data_comanda',)  # Filtru lateral după data comenzii

# Interfață admin pentru ComandaInstrument
@admin.register(ComandaInstrument)
class ComandaInstrumentAdmin(admin.ModelAdmin):
    list_display = ('comanda', 'instrument', 'cantitate')
    search_fields = ('comanda__nume_client', 'instrument__nume')  # Căutare în relațiile între modele
