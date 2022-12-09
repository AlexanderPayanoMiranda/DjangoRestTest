from rest_framework import routers
from todos.api import TodoViewSet

# Adding trailing_slash=False that caused error that made PATCH and PUT to fail
router = routers.DefaultRouter(trailing_slash=False)

router.register('api/todos', TodoViewSet, 'todos')

urlpatterns = router.urls

# Testing with HTTPie
# GET
# http://127.0.0.1:8000/api/todos/
# http://127.0.0.1:8000/api/todos/1
# POST
# http://127.0.0.1:8000/api/todos/
# In body using JSON as an example use:
# {
#     "title": "Todo - Comprar leche",
#     "body": "Comprar leche.",
#     "status": 0
# }
# PUT
# http://127.0.0.1:8000/api/todos/1
# In body using JSON as an example modify the resource with id=1:
# {
#     "title": "Todo - Comprar cajas de leche",
#     "body": "Comprar leche.",
#     "status": 0
# }
# PATCH
# http://127.0.0.1:8000/api/todos/1
# In body using JSON as an example modify the resource with id=1:
# {
#     "title": "Todo - Comprar leche",
#     "body": "Comprar leche.",
#     "status": 0
# }
# DELETE
# http://127.0.0.1:8000/api/todos/1
