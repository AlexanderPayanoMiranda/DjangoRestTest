from rest_framework import routers
from django.urls import path
from GViews.api import (
    UserList, UserRetrieve, UserCreate,
    UserUpdate, UserDestroy, UserListCreate,
    UserRetrieveUpdate, UserRetrieveDestroy,
    UserRetrieveUpdateDestroy
)
from GViews.api import (
    UserReadOnlyViewSet
)

router = routers.DefaultRouter(trailing_slash=False)
router.register("UserReadOnly", UserReadOnlyViewSet, 'UserReadOnly')

urlpatterns = [
    path('UserList', UserList.as_view(), name='UserList'),
    path('UserRetrieve/<int:pk>', UserRetrieve.as_view(), name='UserRetrieve'),
    path('UserCreate', UserCreate.as_view(), name='UserCreate'),
    path('UserUpdate/<int:pk>', UserUpdate.as_view(), name='UserUpdate'),
    path('UserDestroy/<int:pk>', UserDestroy.as_view(), name='UserDestroy'),
    path('UserListCreate', UserListCreate.as_view(), name='UserListCreate'),
    path('UserRetrieveUpdate/<int:pk>', UserRetrieveUpdate.as_view(), name='UserRetrieveUpdate'),
    path('UserRetrieveDestroy/<int:pk>', UserRetrieveDestroy.as_view(), name='UserRetrieveDestroy'),
    path('UserRetrieveUpdateDestroy/<int:pk>', UserRetrieveUpdateDestroy.as_view(), name='UserRetrieveUpdateDestroy'),
]

urlpatterns += router.urls
