from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from todos.models import Todo
from todos.pagination import StandardResultsSetPagination
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'body']
    filterset_fields = ['title', 'body']
    ordering_fields = ['id', 'title', 'body', 'created_at']

    # User Rate Throttle Implementation
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # Scoped Rate Throttle Implementation
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'limited_todo_limit'
