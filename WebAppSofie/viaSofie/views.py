from django.shortcuts import render_to_response #renders pages
from django.http import HttpResponseRedirect #handles redirects
from django.contrib import auth #handles the authantication
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf #anti crosssite scripting
from forms import MyRegistrationForm
from .models import *

def index(request):
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

def property(request, property_id):
	try:
		p = Properties.objects.get(property_id)
		
	except Properties.DoesNotExist:
		raise Http404("Property does not exist.")
	return render_to_response(request, 'templates/property.html', {'Property':p})

def offer_sales(request):
	return render_to_response('templates/offer.html')

def about_sofie(request):
	sofie = AboutSofiePage.objects.order_by('-language')[:5]
	context = {'Sofie': sofie}
	return render(request, 'templates/aboutSofie.html', context)

def disclaimer(request):
	return render_to_response('templates/disclaimer.html')

def faq(request):
	faq = Faq.objects.order_by('-visible')[:5]
	context = {'Faq': faq}
	return render(request, 'templates/faq.html', context)

def privacy(request):
	return render_to_response('templates/privacy.html')

def ebook(request):
	return render_to_response('templates/ebook.html')

def contact(request):
	return render_to_response('templates/contact.html')
