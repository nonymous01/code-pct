from .views import *
from django.urls import path,include

urlpatterns = [
    path('index/', index, name="index"),
    path('inscription/', inscription, name="inscription"),
    path('connexion/', connexion, name="connexion"),
    path('commande1/', commande1, name="commande1"),
    path('commande2/', commande2, name="commande2"),
    path('commande3/', commande3, name="commande3"),
    path('contact/', contact, name="contact"),
    path('services/', services, name="services"),
    path('PLATFORME/', PLATFORME, name="PLATFORME")
]
