from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from account.models import Account
from account.serializers import AccountSerializer, SignUpSerializer

class SignUpViewSet(ViewSet):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)
    throttle_classes = []

    @action(
        detail=True,
        methods=["GET"],
        url_path="info",
        permission_classes=(IsAuthenticated,)
    )
    def info(self, request, pk: int):
        user = request.user
        account = get_object_or_404(Account.objects.filter(user=user), pk=pk)
        account_data = AccountSerializer(account).data
        return Response(account_data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["POST"],
        url_path="create-account",
    )
    def create_account(self, request):
        return Response({"detail": "ok"}, status=status.HTTP_200_OK)
