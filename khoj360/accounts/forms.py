from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=30, required=False)
    area = forms.CharField(max_length=120, required=False)
    blood_group = forms.ChoiceField(choices=Profile.BLOOD_GROUPS, required=False)

    class Meta:
        model = User
        fields = ("username", "full_name", "phone", "area", "blood_group", "password1", "password2")
