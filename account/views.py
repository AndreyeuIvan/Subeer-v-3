from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Sign up view
def signup(request):
	if request.method == 'POST':
		# Process completed form
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			# Log the user in and the redirect to home page
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('login'))
	else:
		# Display black registration form
		form = UserCreationForm()
	context = {'form':form}
	return render(request, 'signup.html', context)