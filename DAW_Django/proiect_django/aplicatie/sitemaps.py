from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Instrument, Promotie

class InstrumentSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Instrument.objects.all()

    def location(self, obj):
        return reverse('instrument_detail', args=[obj.id])

class PromotieSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Promotie.objects.all()

    def location(self, obj):
        return reverse('promotie_detail', args=[obj.id])

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['index', 'contact', 'register', 'login']

    def location(self, item):
        return reverse(item)