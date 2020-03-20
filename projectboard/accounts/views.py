from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


# Create your views here.
def homeview(request):
	user = request.user
	if(user.is_authenticated and not (user.is_staff)):
	 	return(render(request,'accounts/home.html',{'user':user}))
	return(render(request,'accounts/home.html',{}))

def login_req(request):
	if(request.method=='POST'):
		form = AuthenticationForm(request,data=request.POST)
		if(form.is_valid()):
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if(user is not None):
				login(request,user)
				return(render(request,'accounts/home.html',{}))
	else:
		form = AuthenticationForm()

	return(render(request,'accounts/register.html',{'form':form}))

def register(request):
	if(request.method=='POST'):
		form = UserCreationForm(request.POST)
		if(form.is_valid()):
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return(render(request,'accounts/home.html',{}))
	else:
		form = UserCreationForm()
	return(render(request,'accounts/register.html',{'form':form}))

def logout_req(request):
	logout(request)
	return(render(request,'accounts/home.html',{}))