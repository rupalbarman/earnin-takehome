from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from metric.models import Metric
from metric.serializers import MetricSerializer


class MetricViewSet(ViewSet):
    @action(
        detail=False, methods=["GET"], url_path="all", permission_classes=(AllowAny,)
    )
    def get_all(self, request):
        metrics = Metric.objects.all()
        data = MetricSerializer(metrics, many=True).data
        return Response(data, status=status.HTTP_200_OK)
