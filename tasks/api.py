from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

#Conjunto de vistas, se puede crear un CRUD automáticamente gracias al TaskViewSet.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer