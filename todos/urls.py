from rest_framework import routers
from todos.api import TodoViewSet

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos')

urlpatterns = router.urls
