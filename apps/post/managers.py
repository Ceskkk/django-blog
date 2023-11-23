from django.db import models


class PostManager(models.Manager):

    def post_in_cover(self):
        return self.filter(
            public=True,
            cover=True
        ).order_by('-created').first()

    def posts_in_home(self):
        return self.filter(
            public=True,
            in_home=True
        ).order_by('-created')[:4]

    def last_posts(self):
        return self.filter(
            public=True
        ).order_by('-created')[:6]

    def search_post(self, kword, cat):
        if len(cat) > 0:
            return self.filter(
                category__shortname=cat,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
