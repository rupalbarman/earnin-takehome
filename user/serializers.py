from rest_framework import serializers


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
