from rest_framework import routers
from todos.api import TodoViewSet, TestTodoViewSet, TestValidationViewSet

# Adding trailing_slash=False that caused error that made PATCH and PUT to fail
router = routers.DefaultRouter(trailing_slash=False)

router.register('api/todos', TodoViewSet, 'todos')
router.register('api/test/todos', TestTodoViewSet, 'test_todos')
router.register('api/validation', TestValidationViewSet, 'test_validation')

urlpatterns = router.urls

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
