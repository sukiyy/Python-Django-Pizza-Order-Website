from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse #updates python3
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegistrationForm

def logout_view(request):
	'''log the user out.'''
	logout(request) 
	return HttpResponseRedirect(reverse('pizzas:index'))
	
def register(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse('pizzas:index'))
    return render(request, 'pizzas/register.html', { 'form': form })
           

