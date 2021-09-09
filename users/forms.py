from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ['username', 'email', 'password1', 'password2']
		#fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields