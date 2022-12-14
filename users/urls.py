from django.urls import path
from rest_framework import routers
from users.routers import CustomRouter, CustomRouter2
from users.api import UserViewSet, UserGetListViewSet, UserGetOneViewSet

router = routers.DefaultRouter(trailing_slash=False)
# router = CustomRouter(trailing_slash=False)
# router = CustomRouter2(trailing_slash=False)

router.register('api/v2/users', UserViewSet, basename='user')
router.register('api/v3/users', UserGetListViewSet, basename='usergetlist')
router.register('api/v3/users', UserGetOneViewSet, basename='usergetone')

urlpatterns = router.urls
