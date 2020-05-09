from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import validate_email
from django.contrib import messages

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta():
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def clean(self):
		email = self.cleaned_data.get('email')
		validate_email(email)
		if User.objects.filter(email=email).exists():
		 	raise forms.ValidationError("Email already exists.")
		# try:
		# 	if User.objects.filter(email=email).exists():
		# 	    raise forms.ValidationError("Email exists")
		# except:
		# 	messages.error(request, f'Email already exists.')
		return self.cleaned_data