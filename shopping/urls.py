from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="shopping-home")# mapp to ordering menu
]