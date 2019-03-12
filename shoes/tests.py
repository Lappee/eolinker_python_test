from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Shoe
from .serializers import UserSerializer, ShoeSerializer

# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient

    @staticmethod
    def create_user(name="", phone=""):
        if name != "" and phone != "":
            User.objects.create(name=name, phone=phone)

    def setUp(self):
        self.create_user('lappe', '1111111111')
        self.create_user('gepe', '2222222222')
        self.create_user('lorgok', '33333333333')
        self.create_user('seventh', '4444444444')


class GetAllUserTest(BaseViewTest):

    def test_get_all_users(self):
        response = self.client.get(
            reverse('users-all')
        )
        expected = User.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
