from .serializers import PostConnectUserSerializer
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response



class SignUp(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostConnectUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        response_serializer = self.get_serializer(user)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

