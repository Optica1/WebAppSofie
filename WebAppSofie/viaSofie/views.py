from django.shortcuts import render_to_response #renders pages
from django.shortcuts import render #renders pages
from django.http import HttpResponseRedirect,Http404 #handles redirects
from django.contrib import auth #handles the authantication
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf #anti crosssite scripting
from django.utils.translation import ugettext as _ #translation
from django.contrib.auth.models import User
from forms import *
from .models import *


def index(request):
	return render_to_response('templates/home.html')
def about(request):
	try:
		pages = Aboutpage.objects.all()
		page = pages[0]
	except Aboutpage.DoesNotExist:
		raise Http404('page does not exist')
	return render_to_response('templates/about.html', {
		'pageTitle': _(page.title),
		'pageContent': _(page.text),
	})
def status(request):
	try:
		if not request.user.is_authenticated():
			return HttpResponseRedirect('/accounts/login')
		else:
			user = request.user
			userDetail = User.objects.get(id=user.id)
			userdetail = UserDetails.objects.get(id=user.id)
			status = Status.objects.get(id=user.id)
	except Status.DoesNotExist:
		raise Http404('User does not exist')
	return render_to_response('templates/status.html' , {
		'status': status.get_dossierStatus_display,

		'detail': userDetail,
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
		room = Properties.objects.get(property_id = p.id)
	except Properties.DoesNotExist:
		raise Http404("Property does not exist.")
	return render_to_response(request, 'templates/property.html', {'Property':p})

def offer_sales(request):
	return render_to_response('templates/offer.html')

def about_sofie(request):
	sofie = AboutSofiePage.objects.all()
	context = {'Sofie': sofie}
	return render(request, 'templates/aboutSofie.html', context)

def disclaimer(request):
	disclaimer = DisclaimerPage.objects.all()
	context = {'Disclaimer': disclaimer}
	return render(request, 'templates/disclaimer.html', context)
	# return render_to_response('templates/disclaimer.html')

def faq(request):
	# faq = Faq.objects.get(visible=1) can onlly retrieve one not more.
	faq = Faq.objects.filter(visible=1)
	context = {'Faq': faq}
	return render(request, 'templates/faq.html', context)

def privacy(request):
	privacy = PrivacyPage.objects.all()
	context = {'Privacy': privacy}
	return render(request, 'templates/privacy.html', context)

def ebook(request):
	if request.method == 'POST':
		form = MyEbookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	else:
		args = {}
		args.update(csrf(request))
		args['form'] = MyEbookForm()

	return render(request, 'templates/ebook.html', args)

def contact(request):
	return render_to_response('templates/contact.html')
