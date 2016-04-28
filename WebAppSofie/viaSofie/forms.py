from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(label='Gebruikersnaam', max_length=20, required=True)
	password1 = forms.CharField(label='Paswoord', max_length=20, required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label='Herhalen paswoord', max_length=20, required=True, widget=forms.PasswordInput)
	phonenumber = forms.CharField(label='Telefoonnummer', max_length=10, required=True)
	firstname = forms.CharField(label='Voornaam', max_length=15, required=True)
	lastname = forms.CharField(label='Achternaam', max_length=30, required=True)

	class Meta:
		model = User
		fields = ('email', 'username', 'password1', 'password2', 'phonenumber', 'firstname', 'lastname')

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError(_("The two password fields didn't match."))
		return password2

	#overwriting the save method for custom fields
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)# commit false because we do this at end of var assignments
		user.email = self.cleaned_data['email']#cleaned so all character are valid
		user.username = self.cleaned_data['username']
		user.password = self.cleaned_data['password1']
		user.phonenumber = self.cleaned_data['phonenumber']
		user.first_name = self.cleaned_data['firstname']
		user.last_name = self.cleaned_data['lastname']


		if commit:
			user.save()

		return user	