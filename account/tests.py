from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from account.models import Account
from metric.models import Metric
from metric.utils import create_initial_metrics
from user.models import User


class AccountViewTest(TestCase):
    def setUp(self) -> None:
        self.api = APIClient()

        self.user = User.objects.create(
            email="dummy@gmail.com",
            name="Dummy",
        )

        self.account = Account.objects.create(
            user=self.user,
            name="Account Dummy",
        )

        create_initial_metrics()

        self.metrics = list(Metric.objects.all())

    def test_account_create(self):
        self.api.force_authenticate(self.user)

        data = {
            "name": "Account 1",
        }

        response = self.api.post(
            path="/account/create/",
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_account_add_metrics(self):
        self.api.force_authenticate(self.user)

        data = {
            "metric_ids": [m.id for m in self.metrics][:2],
        }

        response = self.api.post(
            path=f"/account/{self.account.id}/add-metrics/",
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_account_info(self):
        self.api.force_authenticate(self.user)

        # Positive check
        response = self.api.get(
            path=f"/account/{self.account.id}/info/",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.account.id)
        self.assertEqual(response.data["name"], self.account.name)
        print(response.data)

        # 404 check
        response = self.api.get(
            path=f"/account/12/info/",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_account_metric(self):
        self.api.force_authenticate(self.user)

        response = self.api.get(
            path=f"/account/{self.account.id}/metric/?metric_ids=1,23,4",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
