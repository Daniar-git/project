from rest_framework.permissions import BasePermission
from project.main.models import Todo


class TodoPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        todo_id = request.parser_context['kwargs']['pk']
        if Todo.objects.filter(id=todo_id).first().user == request.user:
            return True
        return False