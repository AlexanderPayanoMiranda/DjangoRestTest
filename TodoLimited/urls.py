from rest_framework import (routers)
from TodoLimited.api import (TodoViewSet)

router = routers.DefaultRouter(trailing_slash=False)

router.register('api/v1/TodoLimited', TodoViewSet, 'todos')

urlpatterns = router.urls
