from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from todo.models import ToDO
from todo.seriializers import ToDoSerializer


class TodoListCreateAPIView(APIView):
    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        todos = ToDO.objects.all()
        many = True
        serializer = ToDoSerializer(todos, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        todos = get_object_or_404(ToDO, pk=pk)
        many = False
        serializer = ToDoSerializer(todos, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        todos = get_object_or_404(ToDO, pk=pk)
        serializer = ToDoSerializer(instance=todos, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        todos = get_object_or_404(ToDO, pk=pk)
        todos.delete()
        return Response(todos, status=status.HTTP_204_NO_CONTENT)