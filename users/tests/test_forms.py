from django.test import SimpleTestCase, TestCase
from users.forms import *

class TestForms(SimpleTestCase):

    def test_login_form_as_valid(self):
        form = LoginForm(
            data={
                'email': 'email',
                'password': 'password'
            }
        )

        self.assertTrue(form.is_valid())


    def test_login_form_as_invalid(self):
        form = LoginForm(
            data={}
        )

        self.assertFalse(form.is_valid())


    def test_set_password_form_as_valid(self):
        form = SetPasswordForm(
            data={
                'password': 'password'
            }
        )

        self.assertTrue(form.is_valid())