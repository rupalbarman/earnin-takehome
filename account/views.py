from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from account.models import Account, AccountMetric
from account.serializers import (
    AccountAddMetricSerializer,
    AccountCreateSerializer,
    AccountSerializer,
)
from account.throttle import AccountMetricThrottle
from metric.external import call_api
from metric.models import Metric


class AccountViewSet(ViewSet):
    @action(
        detail=True,
        methods=["GET"],
        url_path="info",
        permission_classes=(IsAuthenticated,),
    )
    def info(self, request, pk: int):
        user = request.user
        qs = Account.objects.filter(user=user).prefetch_related(
            "metrics",
            "metrics__metric",
        )
        account = get_object_or_404(qs, pk=pk)
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
            metric_slugs = account.metrics.filter(id__in=metric_ids).values_list(
                "metric__slug", flat=True
            )

        print(metric_ids)
        print(metric_slugs)

        data = call_api(metrics=metric_slugs)

        return Response({"detail": data}, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["POST"],
        url_path="create",
        permission_classes=(IsAuthenticated,),
    )
    def create_account(self, request):
        user = request.user

        # Validations
        serializer = AccountCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # Data operations
        account = Account.objects.create(user=user, name=validated_data["name"])

        # Response
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["POST"],
        url_path="add-metrics",
        permission_classes=(IsAuthenticated,),
    )
    def add_metrics(self, request, pk: int):
        user = request.user

        # Validations
        serializer = AccountAddMetricSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        metric_ids = validated_data["metric_ids"]

        # Data operations
        qs = Account.objects.filter(user=user)
        account = get_object_or_404(qs, pk=pk)
        metrics = Metric.objects.filter(id__in=metric_ids).all()
        account_metrics_to_create = [
            AccountMetric(account=account, metric=m) for m in metrics
        ]
        AccountMetric.objects.bulk_create(
            objs=account_metrics_to_create, batch_size=100, ignore_conflicts=True
        )

        # Response
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
