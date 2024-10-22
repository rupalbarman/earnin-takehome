from rest_framework import serializers

from metric.serializers import MetricSerializer


class AccountMetricSerializer(serializers.Serializer):
    metric = MetricSerializer()


class AccountCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class AccountAddMetricSerializer(serializers.Serializer):
    metric_ids = serializers.ListField(child=serializers.IntegerField(), default=[])


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    account_metrics = AccountMetricSerializer(many=True, source="metrics")
