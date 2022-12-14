from rest_framework import (routers)
from versionedtodo.v3.api import TodoViewSetCustomNew as TodoCustomV3

router = routers.DefaultRouter(trailing_slash=False)

router.register('todos', TodoCustomV3, 'todos')

urlpatterns = router.urls
