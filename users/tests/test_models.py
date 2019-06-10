from django.test import TestCase, Client
from django.urls import resolve, reverse
from users.models import *

class TestModels(TestCase):

    def setUp(self):
        self.client = Client()

        self.role1 = Role.objects.create(
            role_title='role 1'
        )

        self.user1 = User.objects.create(
            first_name= 'first_name 1',
            last_name= 'last_name 1',
            password= 'password1',
            email= 'email@email.com',
            role_id = self.role1.id
        )


    def test_user_modal_POST(self):
        self.assertEquals(self.user1.first_name, 'first_name 1')
        self.assertEquals(self.user1.email, 'email@email.com')