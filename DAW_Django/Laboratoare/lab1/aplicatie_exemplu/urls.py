from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pag1", views.pag1, name="f"),
    path("pag2", views.pag2, name="g"),
    path("mesaj", views.mesaj, name="mesaj"),
    path("data", views.data, name="data"),
    path("nr_accesari", views.nr_accesari, name="nr_accesari"),
    path("suma", views.suma, name="suma"),
    path("text", views.text, name="text"),
    path("nr_parametri", views.nr_parametri, name="nr_parametri"),
    path("operatie", views.operatie, name="operatie"),
    path("tabel", views.tabel, name="tabel"),
    path("lista", views.lista, name="lista"),
    path("elev", views.elev, name="elev"),
]
