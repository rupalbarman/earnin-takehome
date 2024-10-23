from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from user.models import User
from user.serializers import UserCreateSerializer


class UserViewSet(ViewSet):
    @action(
        detail=False,
        methods=["POST"],
        url_path="create",
        permission_classes=(AllowAny,),
    )
    def create_user(self, request):
        # Validations
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        name = validated_data["name"]
        email = validated_data["email"]
        password = validated_data["password"]

        try:
            user = User(name=name, email=email, username=name.lower())
            user.set_password(password)
            user.save()
        except IntegrityError:
            raise PermissionDenied(f"User with email {email} already exists")

        # Response
        data = {"detail": "ok"}
        return Response(data, status=status.HTTP_200_OK)
