from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import *


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('users:login')
        self.assertEquals(resolve(url).func, login)

    def test_logout_url_is_resolved(self):
        url = reverse('users:logout')
        self.assertEquals(resolve(url).func, logout)

    def test_social_login_url_is_resolved(self):
        url = reverse('users:social_login')
        self.assertEquals(resolve(url).func, social_login)

    def test_user_list_url_is_resolved(self):
        url = reverse('users:list_user')
        self.assertEquals(resolve(url).func, list_user)

    def test_add_user_url_is_resolved(self):
        url = reverse('users:add_user')
        self.assertEquals(resolve(url).func, add_user)

    def test_list_roles_url_is_resolved(self):
        url = reverse('users:list_roles')
        self.assertEquals(resolve(url).func, roles_list)
