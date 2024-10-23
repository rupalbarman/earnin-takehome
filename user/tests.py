from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class UserViewTest(TestCase):
    def setUp(self) -> None:
        self.api = APIClient()

    def test_user_create(self):
        data = {
            "name": "User 1",
            "email": "hello@hello.com",
            "password": "12,3",
        }

        response = self.api.post(
            path="/user/create/",
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_user_create_same_email(self):
        # Attempt 1
        data = {
            "name": "User 1",
            "email": "hello1@hello.com",
            "password": "12,3",
        }

        response = self.api.post(
            path="/user/create/",
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Attempt 2
        data = {
            "name": "User 2",
            "email": "hello1@hello.com",
            "password": "12,4",
        }

        response = self.api.post(
            path="/user/create/",
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.data)
