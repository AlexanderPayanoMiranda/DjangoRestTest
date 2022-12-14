from rest_framework import (routers)
from versionedtodo.v2.api import TodoViewSetCustomNew as TodoCustomV2

router = routers.DefaultRouter(trailing_slash=False)

router.register('todos', TodoCustomV2, 'todos')

urlpatterns = router.urls
