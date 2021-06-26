from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime
from .models import User


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name', 'surname', 'email', 'description', 'profil_picture']
