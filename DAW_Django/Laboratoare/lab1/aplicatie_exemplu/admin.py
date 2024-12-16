from django.contrib import admin
import sys
sys.path.append('/Users/dariadragomir/Facultate/AN2/SEM1/Django/Lab1')
from aplicatie_exemplu.models import Festival, Locatie, Partener, Concert, Scena, TipBilet, Bilet, Client, Repertoriu, Piesa, Artist
import os
import django
admin.site.site_header = "Panou de Administrare Site"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Bine ai venit în panoul de administrare"


class FestivalAdmin(admin.ModelAdmin):
    list_display = ('cod_festival', 'denumire', 'eveniment_muzical')
    list_filter = ('eveniment_muzical',)
    search_fields = ('denumire', 'eveniment_muzical')  
    ordering = ('denumire',) 

class LocatieAdmin(admin.ModelAdmin):
    list_display = ('cod_locatie', 'oras')
    list_filter = ('oras',)  
    search_fields = ('oras',) 

class PartenerAdmin(admin.ModelAdmin):
    list_display = ('cod_partener', 'nume')
    list_filter = ('nume',) 
    search_fields = ('nume',) 

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('cod_concert', 'festival', 'locatie', 'partener')
    list_filter = ('festival', 'locatie', 'partener')  
    search_fields = ('cod_concert',)
    ordering = ('festival',) 

class ScenaAdmin(admin.ModelAdmin):
    list_display = ('concert', 'nume')
    search_fields = ('nume',) 

class TipBiletAdmin(admin.ModelAdmin):
    list_display = ('cod_bilet', 'tip')
    list_filter = ('tip',) 
    search_fields = ('tip',) 

class BiletAdmin(admin.ModelAdmin):
    list_display = ('cod_bilet', 'concert')
    search_fields = ('cod_bilet',)  

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nume', 'cod_bilet')
    search_fields = ('nume',) 

class RepertoriuAdmin(admin.ModelAdmin):
    list_display = ('concert',)
    search_fields = ('concert',) 

class PiesaAdmin(admin.ModelAdmin):
    list_display = ('nume', 'cod_repertoriu')
    search_fields = ('nume',) 

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('nume', 'cod_piesa')
    search_fields = ('nume',) 

# Înregistrăm modelele cu Admin-ul
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Locatie, LocatieAdmin)
admin.site.register(Partener, PartenerAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Scena, ScenaAdmin)
admin.site.register(TipBilet, TipBiletAdmin)
admin.site.register(Bilet, BiletAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Repertoriu, RepertoriuAdmin)
admin.site.register(Piesa, PiesaAdmin)
admin.site.register(Artist, ArtistAdmin)
