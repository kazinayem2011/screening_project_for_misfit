from django.test import TestCase, Client
from django.urls import resolve, reverse
from users.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_user_url = reverse('users:list_user')
        self.add_user_url = reverse('users:add_user')
        self.login_url = reverse('users:login')

        self.role1 = Role.objects.create(
            role_title = 'role 1'
        )

        self.user1 = User.objects.create(
            first_name= 'first_name 1',
            last_name= 'last_name 1',
            password= 'password1',
            email= 'email@email.com',
            role_id = self.role1.id
        )


    def test_user_list_GET(self):
        response = self.client.get(self.list_user_url)
        self.assertEquals(response.status_code, 302)


    def test_add_user_GET(self):
        response = self.client.get(self.add_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


    def test_add_user_POST(self):
        response = self.client.post(self.add_user_url, {
            'first_name': 'first_name 1',
            'last_name': 'last_name 1',
            'password': 'password1',
            'email': 'email@email.com',
            'role_id' : self.role1.id
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user1.first_name, 'first_name 1')


    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


    def test_login_POST(self):
        response = self.client.post(self.login_url, {
            'email': 'email@email.com',
            'password': 'password1',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.email, 'email@email.com')