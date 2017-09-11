from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dash(request):
	return render(request, 'core/dash.html')

def comingsoon(request):
	return render(request,'comingsoon.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.email = form.cleaned_data.get('password1') + "@tvr.com"
			user.save()
			return render(request,'core/notactive.html')
	else:
		form = SignUpForm()
	return render(request, 'core/signup.html', {'form':form})
	
def authorize(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:  #to check whether user is available or not?
			# the password verified for the user
			if user.is_active:
				login(request, user)
				request.session['firstname'] = user.first_name
				request.session['username'] = user.username
				messages.success(request, "Welcome "+user.first_name)
				if request.GET['next']:
				    return redirect(request.GET['next'])
				return redirect('dash')
				#return render(request, "core/dash.html")
			else:
				# Inactive account
				form = LoginForm(request.POST)
				messages.warning(request, "Your account is not activated")
				return render(request,'core/notactive.html')
		else:
    		# the authentication system was unable to verify the username and password
			form = LoginForm(request.POST)
			messages.error(request, "The username and password were incorrect.")
	else:
		form = LoginForm()
	if 'username' in request.session:
	    messages.error(request, "Are you a human?")
	    return redirect('dash')
	return render(request,'core/login.html', {'form':form})
