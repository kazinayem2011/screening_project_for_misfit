from django import forms
from .models import *
from django.core.exceptions import ValidationError
# from .get_views_list import all_views_list


# def view_function_list():
#     function_list = [('', '-------')]
#     function_list = function_list + [(entry, entry) for entry in all_views_list]  # converts ValuesQuerySet into Python list
#     return function_list

# class ImageThumbnailFileInput(ClearableFileInput):
#     template_name = 'includes/custom_imagefield.html'


class LoginForm(forms.Form):
    email = forms.CharField(max_length='50', label='Email', widget=forms.TextInput(attrs={'class': 'form-control placeholder-no-fix','placeholder':'Email','autocomplete':'off'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control placeholder-no-fix','placeholder':'Password','autocomplete':'off'}))


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_active', 'activation_code', 'password_reset_code', )
        widgets = {

            'first_name': forms.TextInput(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Last Name'}),
            'password': forms.PasswordInput(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Password'}),
            'email': forms.TextInput(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Email', 'type': 'email'}),
            'role': forms.Select(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Role'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 7:
            raise ValidationError("Password must have 7 characters.")
        return password


class SetPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)
        widgets = {
            'password': forms.PasswordInput(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Password'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 7:
            raise ValidationError("Password must have 7 characters.")
        return password