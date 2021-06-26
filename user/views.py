from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from .forms import UserForm
from .models import *

from PIL import Image

from django.conf import settings


def home(request):
	user_data = {}
	context = {}
	form = UserForm(request.POST or None)
	if form.is_valid():
		form = UserForm()
		user_data = User(name=request.user, 
					surname=request.POST.dict().get('surname'), 
					email=request.POST.dict().get('email'), 
					description=request.POST.dict().get('description'),
					profil_picture=request.POST.dict().get('profil_picture'))
		user_data.save()
		# user_data = User.objects.all()
		context = {'myform' : form, 'u_data' : user_data}
	return render(request, 'home.html', context)

def register(request):
	if  request.user.is_authenticated:
		return redirect('home')
	if  request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
			messages.success(request, f'Your user has been created, you are now able to log in')
			login(request, new_user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form':form})
