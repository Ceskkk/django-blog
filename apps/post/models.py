from datetime import timedelta, datetime
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import PostManager
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy


class Category(TimeStampedModel):

    shortname = models.CharField('Shortname', max_length=15, unique=True)
    name = models.CharField('Name', max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):

    name = models.CharField('Name', max_length=30)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Post(TimeStampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Title', max_length=200)
    summary = models.TextField('Summary')
    content = RichTextUploadingField('Content')
    public = models.BooleanField(default=False)
    image = models.ImageField('Image', upload_to='Post')
    cover = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = PostManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('post_app:post', kwargs={'slug': self.slug})
