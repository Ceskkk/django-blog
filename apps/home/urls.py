from django.urls import path
from . import views


app_name = "home_app"


urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name="index"
    ),
    path(
        'subscribe/',
        views.SubscriberView.as_view(),
        name="subscribe"
    ),
    path(
        'contact/',
        views.ContactView.as_view(),
        name="contact"
    )
]
