import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.api.serializers import AccountSerializaer
from account.models import Account
from backup.api.serializers import ActionSerializer, PointerSerializer
from backup.models import Action, Pointer


class PointerListTestCase(APITestCase):

    def setUp(self):
        self.user = Account.objects.create_user(username="pass_chng_tester",
        password="VeryStrongPassword10/10")

        self.token = Token.objects.get(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_post_pointer_list(self):
        data = [{
                        "Action_Name": [
                            {
                                "Action_Name": "G",
                                "icon": "A",
                                "action_position": 1,
                                "action_detail": "TEST"
                            },
                            {
                                "Action_Name": "G",
                                "icon": "B",
                                "action_position": 1,
                                "action_detail": "TEST"
                            },
                            {
                                "Action_Name": "G",
                                "icon": "C",
                                "action_position": 1,
                                "action_detail": "TEST"
                            }
                        ],
                        "position_y": 3.0,
                        "position_x": 3.0,
                        "_range": 3.0,
                        "title": "EEEEEEEEE",
                        "icon": "C",
                        "description": "C",
                        "queue": 1,
                        "groupID": "GROUPID"
                    }]
                
        response = self.client.post("/api/backup/pointer/", json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pointer_list(self):
        response = self.client.get("/api/backup/pointer/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GroupListTestCase(APITestCase):

    def setUp(self):
        self.user = Account.objects.create_user(username="pass_chng_tester",
        password="VeryStrongPassword10/10")

        self.token = Token.objects.get(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_post_group_list(self):
        data = [
                {
                    "Action_Name": [
                        {
                            "Action_Name": "ACTION NAME I",
                            "icon": "A",
                            "action_position": 1,
                            "action_detail": "ACTION DETAIL"
                        },
                        {
                            "Action_Name": "ACTION NAME II",
                            "icon": "B",
                            "action_position": 1,
                            "action_detail": "ACTION DETAIL"
                        },
                        {
                            "Action_Name": "ACTION NAME III",
                            "icon": "C",
                            "action_position": 1,
                            "action_detail": "ACTION DETAIL"
                        }
                    ],
                    "groupID": "groupID",
                    "_range": 1.0,
                    "name": "Group Name",
                    "icon": "ICON"
                }
            ]

        response = self.client.post("/api/backup/group/", json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_group_list(self):
        response = self.client.get("/api/backup/group/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)