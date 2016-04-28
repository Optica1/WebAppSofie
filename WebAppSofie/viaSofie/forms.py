from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(label='Gebruikersnaam', max_lenght=20, required=True)
	password1 = forms.CharField(label='Paswoord', max_lenght=20, required=True)
	password2 = forms.CharField(label='Herhalen paswoord', max_lenght=20, required=True)
	phonenumber = forms.CharField(label='Telefoonnummer', max_lenght=10, required=True)
	firstname = forms.CharField(label='Voornaam', max_lenght=15, required=True)
	lastname = forms.CharField(label='Achternaam', max_lenght=30, required=True)

	class Meta:
		model = User
		field = ('email', 'username', 'password1', 'password2', 'phonenumber', 'firstname', 'lastname')


	#overwriting the save method for custom fields
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)# commit false because we do this at end of var assignments
		user.email = self.cleaned_data['email']#cleaned so all character are valid
		user.username = self.cleaned_data['username']
		user.password1 = self.cleaned_data['password1']
		user.password2 = self.cleaned_data['password2']
		user.phonenumber = self.cleaned_data['phonenumber']
		user.firstname = self.cleaned_data['firstname']
		user.lastname = self.cleaned_data['lastname']


		if commit
			user.save()

		return user	