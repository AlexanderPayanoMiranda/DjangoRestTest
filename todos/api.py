from django.http import Http404
# from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response
from todos.models import Todo, TestValidation
from todos.serializers import TodoSerializer, TestTodoSerializer, TestValidationSerializer
from todos.pagination import StandardResultsSetPagination


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination
    # Mixed filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'body']
    # filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'title', 'body', 'created_at']


class OneTodo(APIView):
    permission_classes = [IsAuthenticated]

    def get_todo(self, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            return todo
        except Todo.DoesNotExist:
            raise Http404()

    def valid_update_serializer(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise Http404()

    def get(self, request, pk):
        todo = self.get_todo(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_todo(pk)
        updated_todo = TodoSerializer(instance=todo, data=request.data)
        self.valid_update_serializer(updated_todo)

    def patch(self, request, pk):
        todo = self.get_todo(pk)
        updated_todo = TodoSerializer(instance=todo, data=request.data, partial=True)
        self.valid_update_serializer(updated_todo)

    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class AllTodo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Todo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def patch(self, request, pk):
    todo = Todo.objects.get(pk=pk)

    serializer = TodoSerializer(instance=todo, data=request.data, partial=True)

    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializer.data)


class GetAllTodo(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class GetTwoTodos(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.all * ()[:2]
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class DeleteAllTodo(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        Todo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestTodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTodoSerializer


class TestValidationViewSet(viewsets.ModelViewSet):
    queryset = TestValidation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestValidationSerializer


class TodoViewSetCustom(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    pagination_class = StandardResultsSetPagination
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'body']
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'body']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'title', 'body', 'created_at']

    def get_serializer_class(self):
        return TodoSerializer

    # Pagination with Values from settings.py
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # List function to work with filters
    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = TodoSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def list(self, request):
    #     queryset = Todo.objects.all()
    #     serializer = TodoSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # Pagination with Values from settings.py
    # def list(self, request):
    #     page = self.paginate_queryset(self.queryset)
    #     if page is not None:
    #         serializer_class = self.get_serializer_class()
    #         serializer = serializer_class(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = TodoSerializer(data=request.data, many=True)
        else:
            serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
