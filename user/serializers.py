from rest_framework import serializers

from user.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        fields = (
            "email",
            "name",
        )
        model = User