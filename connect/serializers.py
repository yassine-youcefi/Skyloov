

from rest_framework import serializers
from django.contrib.auth.models import User


class PostConnectUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
