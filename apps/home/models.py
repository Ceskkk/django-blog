from django.db import models
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):

    title = models.CharField()
    description = models.TextField()
    about_title = models.CharField('About us title', max_length=50)
    about_text = models.TextField()
    email = models.EmailField('Email', blank=True, null=True)
    phone = models.CharField('Phone', max_length=20)

    class Meta:
        verbose_name= 'Home'
        verbose_name_plural = 'Homes'

    def __str__(self):
        return self.title


class Subscriber(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name= 'Subscriber'
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):

    name = models.CharField('Name', max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name= 'Contact'
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name