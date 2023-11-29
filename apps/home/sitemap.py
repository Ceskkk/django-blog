from django.contrib.sitemaps import Sitemap
from apps.post.models import Post
from datetime import datetime
from django.urls import reverse_lazy


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Post.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.created


class Sitemap(Sitemap):
    protocol = "https"

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)