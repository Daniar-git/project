from .models import User, Note
from .serializers import UserSerializer, NoteSerializer, BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response

from ..common.permissions import NotePermission


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class NotesView(generics.ListAPIView):
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self):
        self.queryset.filter(user=self.request.user)


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    permission_classes = [NotePermission]
    serializer_class = NoteSerializer


    def update(self, request, *args, **kwargs):
        serializer_class = self.serializer_class
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = serializer_class(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogsView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer



class BlogView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer