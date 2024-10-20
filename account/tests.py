from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from account.models import Account
from user.models import User

class SignUpViewTest(TestCase):
    def setUp(self) -> None:
        self.api = APIClient()

        self.user = User.objects.create(
            email='dummy@gmail.com',
            name='Dummy',
        )

        self.account = Account.objects.create(
            user=self.user,
            name="Account Dummy",
        )

    def test_account_signup(self):
        data = {
            "user": {
                "name": "Rupal",
                "email": "rupal@gmail.com"
            },
            "password": 124,
            "account_name": "Account 1",
        }

        response = self.api.post(
            path="/account/create-account/",
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

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

        # 404 check
        response = self.api.get(
            path=f"/account/12/info/",
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
