from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from apps.post.models import Post


class Favorites(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='post_favorites',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'post')
        verbose_name = 'Favorite post'
        verbose_name_plural = 'Favorite posts'

    def __str__(self):
        return self.post.title
