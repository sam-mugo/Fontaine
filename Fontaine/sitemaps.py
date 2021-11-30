from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from main_blog.models import Category, Posts

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    
class PostSitemap(Sitemap):
    def items(self):
        return Posts.objects.filter(status=Posts.ACTIVE)
    
    def lastmod(self, obj):
        return obj.created_at