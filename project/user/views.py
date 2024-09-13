from .models import User
from .serializers import UserSerializer, UserDetailsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, views
from rest_framework.response import Response



class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserInfoView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)
