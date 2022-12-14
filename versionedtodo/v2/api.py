from todos.models import Todo
from versionedtodo.v2.serializers import TodoSerializer
from todos.pagination import StandardResultsSetPagination
from rest_framework import viewsets


class TodoViewSetCustomNew(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination
