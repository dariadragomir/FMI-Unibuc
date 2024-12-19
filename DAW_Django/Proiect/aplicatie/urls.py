from django.urls import path
import aplicatie.views as views
from django.contrib import admin
from django.urls import path, include
from .forms import InstrumentForm

urlpatterns = [
    # Adaugă aici rutele specifice aplicației tale
    path("", views.index, name="index"),
    path('filter-instruments/', views.filter_instruments, name='filter_instruments'),
    #path('admin/', admin.site.urls),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.success_view, name='success'),
    path('adauga-instrument/', views.adauga_instrument, name='adauga_instrument'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('custom_login/', views.custom_login_view, name='custom_login'),
]
