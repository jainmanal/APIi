from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms




class EmployeeForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        labels = {'email':'Email'}


class EmployeeChangeForm(UserChangeForm):
    class Meta:
        