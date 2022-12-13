from rest_framework import (routers)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from django.urls import (path)
from todos.api import (
    TodoViewSet, TestTodoViewSet, TestValidationViewSet
)
from todos.api import (
    AllTodo, GetAllTodo, DeleteAllTodo,
    OneTodo, patch
)

# Adding trailing_slash=False that caused error that made PATCH and PUT to fail
router = routers.DefaultRouter(trailing_slash=False)

router.register('api/v1/todos', TodoViewSet, 'todos')
router.register('api/v1/test/todos', TestTodoViewSet, 'test_todos')
router.register('api/v1/validation', TestValidationViewSet, 'test_validation')

urlpatterns = [
    path('api/v1/todos/getAll', GetAllTodo.as_view(), name='get_all'),
    path('api/v1/todos/deleteAll', DeleteAllTodo.as_view(), name='delete_all'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v2/todos', AllTodo.as_view(), name='fullView'),
    path('api/v2/todos/<int:pk>', OneTodo.as_view(), name='oneTodo'),
    path('api/v2/todos/patch/<int:pk>', patch, name='patch'),
]

urlpatterns += router.urls

# Testing with HTTPie
# GET
# http://127.0.0.1:8000/Todos/api/todos
# http://127.0.0.1:8000/Todos/api/todos/1
# POST
# http://127.0.0.1:8000/Todos/api/todos
# In body using JSON as an example use:
# {
#     "title": "Todo - Comprar leche",
#     "body": "Comprar leche.",
#     "status": 0
# }
# PUT
# http://127.0.0.1:8000/Todos/api/todos/1
# In body using JSON as an example modify the resource with id=1:
# {
#     "title": "Todo - Comprar cajas de leche",
#     "body": "Comprar leche.",
#     "status": 0
# }
# PATCH
# http://127.0.0.1:8000/Todos/api/todos/1
# In body using JSON as an example modify the resource with id=1:
# {
#     "title": "Todo - Comprar leche",
#     "body": "Comprar leche.",
#     "status": 0
# }
# DELETE
# http://127.0.0.1:8000/Todos/api/todos/1
