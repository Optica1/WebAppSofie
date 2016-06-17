from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password
from .models import *
from django import forms
import sys
import traceback
from haystack.forms import SearchForm
#from passlib.hash import sha256_crypt

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(label='Gebruikersnaam', max_length=20, required=True)
	password1 = forms.CharField(label='Paswoord', max_length=20, required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label='Herhalen paswoord', max_length=20, required=True, widget=forms.PasswordInput)
	phonenumber = forms.CharField(label='Telefoonnummer', max_length=10, required=True)
	firstname = forms.CharField(label='Voornaam', max_length=15, required=True)
	lastname = forms.CharField(label='Achternaam', max_length=30, required=True)

	class Meta(UserCreationForm.Meta):
		model = User
		fields =('email', 'username', 'password1', 'password2', 'phonenumber', 'firstname', 'lastname')

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError(_("De paswoorden kwamen niet overeen."))

	#overwriting the save method for custom fields
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)# commit false because we do this at end of var assignments

		user.email = self.cleaned_data['email']#cleaned so all character are valid
		user.username = self.cleaned_data['username']
		user.password = make_password(self.cleaned_data['password1'])
		user.first_name = self.cleaned_data['firstname']
		user.last_name = self.cleaned_data['lastname']

		user.phonenumber = self.cleaned_data['phonenumber']

		if commit:
			user.save()
		return

class MyEbookForm(forms.Form):
	email = forms.EmailField(required=True)
	ebook = forms.ModelChoiceField(queryset=Ebook.objects.filter(available=1).order_by('id'))

	class Meta:
		model = EbookRequests
		fields =('email', 'ebook')

	def save(self, commit=True):
		EbookRequests.email = self.cleaned_data['email']
		EbookRequests.ebook = self.cleaned_data['id_ebook'].id

		if commit:
			EbookRegistration.save()

		return

class ContactForm(forms.Form):
	subject = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)

class NewsletterForm(forms.ModelForm):
	mail = forms.EmailField(required=True)

	class Meta:
		model = Newsletter
		fields = ['mail']

	def clean_email(self):
		mail = self.cleaned_data['mail']
		checkmail = Newsletter.objects.filter(email = mail)
		if Newsletter.objects.filter(email=email).exists():
			raise forms.ValidationError(u'email "%s" is already in use.' % email)

	def save(self, commit=True):
		Newsletter = super(NewsletterForm, self).save(commit=False)# commit false because we do this at end of var assignments

		Newsletter.email = self.cleaned_data['mail']#cleaned so all character are valid
		print Newsletter.email
		if commit:
			Newsletter.save()
		return

class NewsletterUnsubscribeForm(forms.Form):
	email = forms.EmailField(required=True)

	class Meta:
		model = Newsletter
		fields = ('email')

	def clean_email(self):
		email = self.cleaned_data['email']
		if Newsletter.objects.filter(email).exists():
			pass
		else:
			raise forms.ValidationError(u'email "%s" is not subscribed to the newsletter' % email)

class PandenSearchForm(SearchForm):
	# def search(self):
	def no_query_found(self
		return self.searchqueryset.all()
