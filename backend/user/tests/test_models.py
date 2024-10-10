from rest_framework.test import APITestCase

from user.models import (User,
                         Profile)


class TestUser(APITestCase):
    def setUp(self) -> None:
        self.credentials = {
            "phone":"09123456789",
            "email":"test321@gmail.com",
            "username":"test_user",
            "password":"mnbvcxz#09876543210",
            "first_name":"ben",
            "last_name":"web",
        }

        self.user = User.objects.create(**self.credentials)
    
    def test_createUser(self):
        credentials = {
            "phone":"09112345665",
            "email":"mytest321@gmail.com",
            "username":"test_user3",
            "password":"mnbvcxz#09876543217",
            "first_name":"alex",
            "last_name":"web",
        }
        user2 = User.objects.create(**credentials)
        self.assertEqual(user2.phone, "09112345665")
    
    def test_getUserPhone(self):
        self.assertEqual(self.user.phone, "09123456789")
    
    def test_updateUserPhone(self):
        self.user.phone = "09123456780"
        self.user.save()
        self.assertEqual(self.user.phone, "09123456780")


class TestProfile(APITestCase):
    def setUp(self) -> None:
        self.credentials = {
            "phone":"09123456789",
            "email":"test321@gmail.com",
            "username":"test_user",
            "password":"mnbvcxz#09876543210",
            "first_name":"ben",
            "last_name":"web",
        }

        self.user = User.objects.create(**self.credentials)
    
    def test_getProfile(self):
        p = Profile.objects.get(user=self.user)
        self.assertEqual(p.phone, "09123456789")
