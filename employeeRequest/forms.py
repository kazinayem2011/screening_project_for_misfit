from django import forms
from .models import *


class AddRequestForm(forms.ModelForm):
    class Meta:
        model = EmployeeRequest
        fields = ('request_name', 'request_details')
        widgets = {

            'request_name': forms.TextInput(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Request Name'}),
            'request_details': forms.Textarea(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Request details'}),
        }


class EditRequestForm(forms.ModelForm):
    class Meta:
        model = EmployeeRequest
        fields = ('request_name', 'request_details')
        widgets = {

            'request_name': forms.TextInput(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Request Name'}),
            'request_details': forms.Textarea(attrs={"class": 'form-control', 'required' : 'required','placeholder': 'Request details'}),
        }


class EditRequestStatusForm(forms.ModelForm):
    CHOICES = (
        ('', '--- Select Status ---',),
        ('0', 'Open',),
        ('1', 'Processed',),
        ('2', 'HR Reviewed',),
    )
    status = forms.ChoiceField(label='Status', widget=forms.Select(attrs={'class': 'form-control'}), choices=CHOICES, required=True)

    class Meta:
        model = EmployeeRequest
        fields = ('status',)


class EditRequestStatusForManagerForm(forms.ModelForm):
    CHOICES = (
        ('', '--- Select Status ---',),
        ('1', 'Processed',),
    )
    status = forms.ChoiceField(label='Status', widget=forms.Select(attrs={'class': 'form-control'}), choices=CHOICES, required=True)

    class Meta:
        model = EmployeeRequest
        fields = ('status',)