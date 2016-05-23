from django.shortcuts import render_to_response #renders pages
from django.http import HttpResponseRedirect #handles redirects
from django.contrib import auth #handles the authantication
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf #anti crosssite scripting
from forms import MyRegistrationForm
from .models import *
import pdb

def index(request):
	pdb.set_trace()
	return render_to_response('templates/home.html')
def about(request):
	try:
		page = Aboutpage.objects.get(id=1)
	except Aboutpage.DoesNotExist:
		raise Http404('page does not exist')
	return render_to_response('templates/about.html', {
		'page': page,
	})
def client(request, id):
	try:
		client = Client.objects.get(id=id)
	except Client.DoesNotExist:
		raise Http404('User does not exist')
	return render_to_response('templates/client.html' , {
		'client': client,
	})
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('templates/login.html', c)

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
		return render_to_response('templates/loggedin.html',
								{'full_name': request.user.username}) #passes full_name to template

def invalid_login(request):
	return render_to_response('templates/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('templates/logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success/')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()

	return render_to_response('templates/register.html', args)

def register_success(request):
	return render_to_response('templates/register_success.html')

def property(request):
	return render_to_response('templates/property.html')

def offer_sales(request):
	return render_to_response('templates/offer.html')
