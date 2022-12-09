from django.urls import path
from MyAPI.views import pais

from rest_framework import routers
from MyAPI.api import UserViewSet

# Adding trailing_slash=False that caused error that made PATCH and PUT to fail
router = routers.DefaultRouter(trailing_slash=False)

router.register('api/users', UserViewSet, 'users')

urlpatterns = router.urls

# urlpatterns = [
#     # path('pais/', pais, name='pais'),
#     path('pais/', pais.as_view(), name='pais')
# ]
