from django.urls import path
from MyAPI.views import pais

urlpatterns = [
    # path('pais/', pais, name='pais'),
    path('pais/', pais.as_view(), name='pais')
]
