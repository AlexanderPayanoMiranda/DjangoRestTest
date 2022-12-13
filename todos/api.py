from django.http import Http404
# from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response
from todos.models import Todo, TestValidation
from todos.serializers import TodoSerializer, TestTodoSerializer, TestValidationSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer


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
