from django import forms

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = forms.CharField(validators=[phone_regex]) # validators should be a list
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'password',)

# class ModifiedPersonForm(UserForm):
	
# 	class Meta(UserForm.Meta):
# 		fields = UserForm.Meta.fields + ('phone_number')
	
