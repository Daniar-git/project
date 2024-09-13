from .models import Todo
from .serializers import TodoSerializer
from .filters import TodoFilter
from ..common.permissions import TodoPermission

from rest_framework import filters, generics, status
from rest_framework.permissions import IsAuthenticated




class TodosView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = TodoFilter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



class TodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [TodoPermission]