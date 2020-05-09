from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def register(request):
	if request.method == 'POST':
		reg_form = UserRegistrationForm(request.POST)
		if reg_form.is_valid():
			reg_form.save()
			username = reg_form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }')
			return redirect('polls_app:index')
	else:
		reg_form =  UserRegistrationForm()
	return render(request, 'user/register.html', {'reg_form': reg_form})