from django.urls import path
from . import views


app_name = "favorites_app"


urlpatterns = [
    path(
        'user/profile',
        views.ProfileView.as_view(),
        name="profile"
    ),
    path(
        'add-post/<pk>',
        views.AddToFavoritesView.as_view(),
        name="add-post"
    ),
    path(
        'remove-post/<pk>',
        views.RemoveFromFavoritesView.as_view(),
        name="remove-post"
    ),
]
