from rest_framework.permissions import BasePermission

from project.user.models import Note


class Permission(BasePermission):
    message = "Access Denied!"

    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user and request.user.is_authenticated
        elif request.method == 'GET':
            return True


class NotePermission(Permission):

    def get_note(self, request):
        note_id = request.parser_context['kwargs']['pk']
        channel = Note.objects.filter(user=request.user, id=note_id).first()
        return channel

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            note = self.get_note(request)
            if note:
                return True
            else:
                return False
        elif request.method == 'GET':
            return True
        return False