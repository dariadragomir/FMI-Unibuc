from django.urls import path
import aplicatie.views as views
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap

from aplicatie.sitemaps import InstrumentSitemap, PromotieSitemap, StaticViewSitemap

sitemaps = {
    'instruments': InstrumentSitemap,
    'promotii': PromotieSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path("", views.index, name='index'),
    path('filter_instruments/', views.filter_instruments, name='filter_instruments'),
    #path('admin/', admin.site.urls),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.success_view, name='success'),
    path('adauga-instrument/', views.adauga_instrument, name='adauga_instrument'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('confirma_mail/<str:cod>/', views.confirma_mail, name='confirma_mail'),
    path('custom_login/', views.custom_login_view, name='custom_login'),
    path('promotii/', views.adauga_promotie, name='adauga_promotie'),
    path('adauga-promotie/', views.adauga_promotie, name='adauga_promotie'),
    path('some_view/', views.some_view, name='some_view'),
    path('oferta/', views.oferta_view, name='oferta'),
    path('aloca_permisiune_oferta/', views.aloca_permisiune_oferta, name='aloca_permisiune_oferta'),
    path('instrument/<int:id>/', views.instrument_detail, name='instrument_detail'),
    path('instrumente/', views.instrument_list, name='instrument_list'),
    path('promotie/<int:id>/', views.promotie_detail, name='promotie_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increment/<int:item_id>/', views.increment_cart_item, name='increment_cart_item'),
    path('cart/decrement/<int:item_id>/', views.decrement_cart_item, name='decrement_cart_item'),
    path('procesare-comanda/', views.place_order, name='procesare_comanda'),

]