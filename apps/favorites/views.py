from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View, DeleteView
from .models import Favorites
from django.urls import reverse_lazy, reverse
from apps.post.models import Post
from django.http import HttpResponseRedirect


class ProfileView(LoginRequiredMixin, ListView):
    template_name = "pages/user/profile.html"
    context_object_name = 'user_posts'
    login_url = reverse_lazy('users_app:login')

    def get_queryset(self):
        return Favorites.objects.user_posts(self.request.user)


class AddToFavoritesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:login')

    def post(self, request, *args, **kwargs):
        user = self.request.user
        post = Post.objects.get(id=self.kwargs['pk'])
        Favorites.objects.create(
            user=user,
            post=post
        )

        return HttpResponseRedirect(
            reverse(
                'favorites_app:profile'
            )
        )


class RemoveFromFavoritesView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favorites_app:profile')
