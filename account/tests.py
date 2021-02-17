import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.api.serializers import AccountSerializaer
from account.models import Account


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "test",
            "password": "Testowehaslo1!",
            "password2": "Testowehaslo1!"
        }
        response = self.client.post("/api/account/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_registration_but_user_exists(self):
        data = {
            "username": "test",
            "password": "Testowehaslo1!",
            "password2": "Testowehaslo1!"
        }
        self.client.post("/api/account/register/", data)
        response = self.client.post("/api/account/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_but_data_is_empty(self):
        data = {
        }
        response = self.client.post("/api/account/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ChangePasswordTestCase(APITestCase):

    def setUp(self):
        self.user = Account.objects.create_user(username="pass_chng_tester",
        password="VeryStrongPassword10/10")

        self.token = Token.objects.get(user=self.user)
        self.api_authentication()


    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_change_password_authenticated(self):
        data = {
            "old_password" : "VeryStrongPassword10/10",
            "new_password" : "Bardziej_testowe_haslo",
            "new_password2" : "Bardziej_testowe_haslo"
        }

        response = self.client.put("/api/account/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_change_password_authenticated_but_wrong_old_password(self):
        data = {
            "old_password" : "ZleHaslo",
            "new_password" : "Bardziej_testowe_haslo",
            "new_password2" : "Bardziej_testowe_haslo"
        }

        response = self.client.put("/api/account/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_authenticated_but_new_passwords_not_equal(self):
        data = {
            "old_password" : "Bardziej_testowe_haslo",
            "new_password" : "Haslo_numer_1",
            "new_password2" : "Haslo_numer_2"
        }

        response = self.client.put("/api/account/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_authenticated_but_everything_is_wrong(self):
        data = {
            "old_password" : "AAAAAAAAAAAAAAAAAAAA",
            "new_password" : "BBBBBBBBBBBBBBBBBBBB",
            "new_password2" : "CCCCCCCCCCCCCCCCCCCC"
        }

        response = self.client.put("/api/account/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_authenticated_but_data_is_missing_fields(self):
        data = {
            "old_password" : "AAAAAAAAAAAAAAAAAAAA",
            "new_password2" : "CCCCCCCCCCCCCCCCCCCC"
        }

        response = self.client.put("/api/account/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_not_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "old_password" : "Bardziej_testowe_haslo",
            "new_password" : "Bardziej_testowe_haslo1",
            "new_password2" : "Bardziej_testowe_haslo1"
        }

        response = self.client.put("/api/account/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class DeleteAccountTestCase(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user(username="pass_chng_tester",
        password="VeryStrongPassword10/10")

        self.token = Token.objects.get(user=self.user)
        self.api_authentication()


    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_delete_account(self):
        response = self.client.delete("/api/account/delete_account/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
   
    def test_delete_account_but_account_dosent_exist(self):
        self.client.delete("/api/account/delete_account/")
        response = self.client.delete("/api/account/delete_account/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_account_but_not_authorized(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete("/api/account/delete_account/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)        
