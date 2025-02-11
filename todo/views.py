from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def update(self, request, *args, **kwargs):
        try:
            todo = self.get_object()  
            completed = request.data.get("completed", None)

            if completed is None:
                return Response({"error": "Missing 'completed' field"}, status=status.HTTP_400_BAD_REQUEST)

            todo.completed = completed
            todo.save()

            return Response({"message": "Task updated successfully", "todo": TodoSerializer(todo).data})

        except Todo.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
