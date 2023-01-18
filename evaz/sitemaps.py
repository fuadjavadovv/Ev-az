from django.contrib import sitemaps
from sale.models import Property
from django.urls import reverse

class StaticSitemap(sitemaps.Sitemap):
    change_freqs = {
        'sale:home': 'weekly',
        'info:contact': 'monthly',
        'sale:property-list': 'daily'
    }
    
    priorities = {
        'sale:home': 0.9,
        'info:contact': 0.8,
        'sale:property-list': 0.6
    }
    
    def items(self):
        return [
            'sale:home',
            'info:contact',
            'sale:property-list',
        ]
        
    def location(self, item):
        return reverse(item)
    
    def priority(self, item):
        return self.priorities.get(item, 0.5)
    
    def changefreq(self, item):
        return self.change_freqs.get(item, 'never')
    
    
class PropertySitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    
    def items(self):
        return Property.objects.all()