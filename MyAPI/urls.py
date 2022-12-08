from django.urls import path
from MyAPI.views import pais

urlpatterns = [
    path('pais/', pais, name='pais')
]
