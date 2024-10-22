from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from account.models import Account
from account.serializers import AccountSerializer, SignUpSerializer
from account.throttle import AccountMetricThrottle
from metric.external import call_api

class SignUpViewSet(ViewSet):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

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
        detail=True,
        methods=["GET"],
        url_path="metric",
        permission_classes=(IsAuthenticated,),
        throttle_classes=[AccountMetricThrottle],
    )
    def metric(self, request, pk: int):
        user = request.user
        account = get_object_or_404(Account.objects.filter(user=user), pk=pk)
        metric_ids = request.GET.get("metric_ids")

        # If metrics are explicitly provided, use them
        # Otherwise, fetch metrics registered to account
        if metric_ids and isinstance(metric_ids, str):
            metric_ids = metric_ids.split(",")

        # Fetch metric slugs based on IDs provided or all from the account
        if not len(metric_ids):
            print("Fetching from DB")
            metric_slugs = account.metrics.values_list("metric__slug", flat=True)
        else:
            metric_slugs = account.metrics.filter(id__in=metric_ids).values_list("metric__slug", flat=True)

        print(metric_ids)
        print(metric_slugs)

        data = call_api(metrics=metric_slugs)

        return Response({"detail": data}, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["POST"],
        url_path="create",
    )
    def create_account(self, request):
        return Response({"detail": "ok"}, status=status.HTTP_200_OK)
