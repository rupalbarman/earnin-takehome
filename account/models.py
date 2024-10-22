from django.db import models


class Account(models.Model):
    user = models.ForeignKey(
        "user.User",
        related_name="accounts",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255, null=True)


class AccountMetric(models.Model):
    account = models.ForeignKey(
        "account.Account",
        related_name="metrics",
        on_delete=models.CASCADE,
    )
    metric = models.OneToOneField(
        "metric.Metric",
        related_name="account_metrics",
        on_delete=models.CASCADE,
        null=True,
    )
    metric_name = models.CharField(max_length=255, null=True, blank=True)
