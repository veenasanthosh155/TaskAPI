from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework import mixins,generics,viewsets
from django.contrib.auth.models import User
from tasks.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class Alltasks(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class = TaskSerializer

class Notcompletedtasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = self.queryset
        queryset = qs.filter(completed=False)
        return queryset

class Completedtasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs=self.queryset
        queryset = qs.filter(completed=True)
        return queryset

class CreateUser(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
