from django.db import models


class FavoritesManager(models.Manager):

    def user_posts(self, user):
        return self.filter(
            post__public=True,
            user=user
        ).order_by('-created')
