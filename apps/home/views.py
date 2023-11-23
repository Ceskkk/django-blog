from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from apps.post.models import Post
from apps.home.models import Home
from .forms import SubscriberForm, ContactForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["home"] = Home.objects.latest('created')
        context["cover"] = Post.objects.post_in_cover()
        context["posts_home"] = Post.objects.posts_in_home()
        context["last_posts"] = Post.objects.last_posts()

        context["form"] = SubscriberForm

        return context


class SubscriberView(CreateView):
    form_class = SubscriberForm
    success_url = '/'


class ContactView(CreateView):
    form_class = ContactForm
    success_url = '/'
