from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class HomeSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5
    def items(self):
        return ['home', 'about', 'contact', 'services', 'privacy']
    def location(self, obj):
        return reverse(obj)
