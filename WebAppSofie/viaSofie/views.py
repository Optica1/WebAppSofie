from django.shortcuts import render_to_response #renders pages
from django.shortcuts import render #renders pages
from django.http import HttpResponseRedirect,Http404, HttpResponse #handles redirects
from django.contrib import auth #handles the authantication
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf #anti crosssite scripting
from django.template import RequestContext
from django.utils.translation import ugettext as _ #translation
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from datetime import date
from haystack.generic_views import SearchView
import sys
import traceback

def pandensearch(request):
    form = PandenSearchForm(request.GET)
    panden = form.search()
    context = {'panden': panden}
    return render(request, 'templates/notes.html', context)

def index(request):
	s = Properties.objects.filter(sale = True, sold = False, available = True).order_by('-date_modified')[:4]
	r = Properties.objects.filter(sale = False, sold = False, available = True).order_by('-date_modified')[:4]

	return render(request, 'templates/home.html', {'Sales':s, 'Rents':r})

def about(request):
	try:
		pages = Aboutpage.objects.all()
		page = pages[0]
	except Aboutpage.DoesNotExist:
		raise Http404('page does not exist')
	return render(request, 'templates/about.html', {
		'pageTitle': _(page.title),
		'pageContent': _(page.text),
	})
def status(request):
	try:
		if not request.user.is_authenticated():
			return HttpResponseRedirect('/accounts/login')
		else:
			user = request.user
			userInfo = User.objects.get(id=user.id)
			status = Status.objects.get(id=user.id)
	except Exception as e:
		raise Http404(e)
	return render(request, 'templates/status.html' , {
		'status': status.get_dossierStatus_display,
		'info': userInfo,
	})
def account(request):
	try:
		if not request.user.is_authenticated():
			return HttpResponseRedirect('/accounts/login')
		else:
			user = request.user
			userInfo = User.objects.get(id=user.id)
			properties = Properties.objects.filter(user_id=user.id)
			status = Status.objects.all()
	except Exception as e:
		raise Http404(e)
	return render(request, 'templates/account.html' , {
		'status': status,
		'info': userInfo,
		'properties': properties,
	})
def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'templates/login.html', c)

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
		return render(request, 'templates/loggedin.html',
								{'full_name': request.user.username}) #passes full_name to template

def invalid_login(request):
	return render(request, 'templates/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'templates/logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success/')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()

	return render(request, 'templates/register.html', args)

def register_success(request):
	return render(request, 'templates/register_success.html')

def property(request, p_id='1'):
    try:
        p = Properties.objects.get(id = p_id)
        bedrooms = Bedroom.objects.filter(property_id = p.id)
        bedroomcount = bedrooms.count()
        bathrooms = Bathroom.objects.filter(property_id = p.id)
        bathroomcount = bathrooms.count()
        toilets = Toilet.objects.filter(property_id = p.id)
        toiletcount = toilets.count()
        kitchens = Kitchen.objects.filter(property_id = p.id)
        kitchencount = kitchens.count()
        garages = Garage.objects.filter(property_id = p.id)
        garagecount = garages.count()
        bergingen = Storageroom.objects.filter(property_id = p.id)
        bergingcount = bergingen.count()
        basements = Basement.objects.filter(property_id = p.id)
        basementcount = basements.count()
        attics = Attic.objects.filter(property_id = p.id)
        atticcount = attics.count()
        livingrooms = Livingroom.objects.filter(property_id = p.id)
        livingroomcount = livingrooms.count()
        storagerooms = Storageroom.objects.filter(property_id = p.id)
        storageroomcount = storagerooms.count()
        planningInfo = PlanningInfo.objects.filter(property_id = p.id)
        photos = Photo.objects.filter(property_id = p.id)
        documents = PropertyDocuments.objects.filter(property_id = p.id)

        returned_values = {'Property':p, 'Bedrooms':bedrooms, 'Bedroomcount':bedroomcount,
        'Bathrooms':bathrooms, 'Bathroomcount':bathroomcount,
        'Toiletcount':toiletcount, 'Toilets': toilets,
        'Kitchens':kitchens, 'Kitchencount':kitchencount,
        'Garagecount':garagecount, 'Garages':garages,
        'Bergingcount':bergingcount, 'Bergingen':bergingen,
        'Basementcount':basementcount, 'Basements':basements,
        'Atticcount':atticcount, 'Attics':attics,
        'Livingroomcount':livingroomcount, 'Livingrooms':livingrooms,
        'Storageroomcount':storageroomcount, 'Storagerooms':storagerooms, 'PlanningInfo':planningInfo,
        'Photos':photos, 'Documents':documents}
    except Properties.DoesNotExist:
        raise Http404("Property does not exist.")
    return render(request, 'templates/property.html', returned_values)

def offer_sales(request):
	p = Properties.objects.filter(sale = True, sold = False, available = True).order_by('date_modified')[:10]
	return render(request, 'templates/offer.html', {'Properties':p})

def offer_rent(request):
	p = Properties.objects.filter(sale = False, sold = False, available = True).order_by('date_modified')[:10]
	return render(request, 'templates/offer.html', {'Properties':p})

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

def partner(request):
	partner = Partner.objects.filter(available=1)
	context = {'Partner': partner}
	return render(request, 'templates/partner.html', context)

def ebook(request):
	args = {}
	args.update(csrf(request))
	args['form'] = MyEbookForm(request.POST or None)

	if request.method == 'POST':
		if args['form'].is_valid():
			if args['form'].cleaned_data['newsletter']:
				mail = args['form'].cleaned_data['email']
				newsletter = Newsletter(email=mail)
				if Newsletter.objects.filter(email=mail).exists():
					pass
				else:
					newsletter.save()
			args['form'].save()
		else:
			forms.ValidationError(_('Fill in all fields'), code='invalid')



	return render(request, 'templates/ebook.html', args)

def contact(request):
	args = {}
	args.update(csrf(request))
	args['form'] = ContactForm(request.POST or None)

	if request.method == 'POST':
		if args['form'].is_valid():
			subject = request.POST.get('subject', '')
			email = request.POST.get('email', '')
			content = request.POST.get('content', '')

			if subject and content and email:
				try:
					send_mail(subject, content, email, ['nick.vanheertum@student.ap.be'])
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				return HttpResponseRedirect('/contact/thanks/')
			else:
				# In reality we'd use a form class
				# to get proper validation errors.
				return HttpResponse('Make sure all fields are entered and valid.')
	return render(request, 'templates/contact.html', args)


def newsletterSubscribe(request):
	args = {}
	args.update(csrf(request))
	args['form'] = NewsletterForm(request.POST or None)

	if request.method == 'POST':
		if args['form'].is_valid():
			mail = args['form'].cleaned_data['mail']
			if Newsletter.objects.filter(email=mail).exists():
				pass #raise forms.ValidationError(u'email "%s" is already in use.' % mail)
			else:
				args['form'].save()
	
	return render(request, 'templates/newsletter.html', args)

def newsletterUnsubscribe(request):
	args = {}
	args.update(csrf(request))
	args['form'] = NewsletterUnsubscribeForm(request.POST or None)

	if request.method == 'POST':
		if args['form'].is_valid():
			email = args['form'].cleaned_data['email']
			Newsletter.objects.filter(email=email).delete()
	return render(request, 'templates/newsletter_unsubscribe.html', args)
