from django.shortcuts import render_to_response #renders pages
from django.http import HttpResponseRedirect #handles redirects
from django.contrib import auth #handles the authantication
from django.core.context_processors import csrf #anti crosssite scripting

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login')
	else:
		return render_to_response('loggedin.html',
								{'full_name': request.user.username}) #passes full_name to template

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
