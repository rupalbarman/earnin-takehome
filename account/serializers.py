from rest_framework import serializers

from user.serializers import UserSerializer

class SignUpSerializer(serializers.Serializer):
    user = UserSerializer()
    password = serializers.CharField(required=True)
    account_name = serializers.CharField(required=True)

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
