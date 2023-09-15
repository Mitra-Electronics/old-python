from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    path('track', views.tracker, name = "tracker"),
    path('item', views.product, name = "product"),
    path('checkout', views.checkout, name = "checkout"),
    path('search', views.search, name = "search"),
]