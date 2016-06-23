from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
import time
import googlemaps
import json
import datetime
import ssl
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from tinymce import models as tinymce_models
from datetime import date
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import sys
import traceback

# ssl._create_default_https_context = ssl._create_unverified_context
fs = FileSystemStorage()

class UserDetails(models.Model):
	user = models.OneToOneField(User)
	phonenumber = models.CharField('Telefoonnummer', max_length=12)
	street = models.CharField('Straat', max_length=50)
	housenumber = models.CharField('Huisnummer', max_length=4)
	busnumber = models.CharField('Busnummer', max_length=3, null=True, blank=True)
	postalcode = models.CharField('Postcode', max_length=10)
	city = models.CharField('Plaats', max_length=30)
	country = models.CharField('Land', max_length=30)

class Aboutpage(models.Model):
	title = models.CharField('titel', max_length=60)
	text = tinymce_models.HTMLField()
	language = models.CharField('taal', max_length=20, default='NL')
	class Meta:
		verbose_name_plural = "Over ons pagina"

class PrivacyPage(models.Model):
	title = models.CharField('titel', max_length=60)
	text = HTMLField()
	language = models.CharField('taal', max_length=20)
	class Meta:
		verbose_name_plural = "Privacy pagina"

class DisclaimerPage(models.Model):
	title = models.CharField('titel', max_length=60)
	text = HTMLField()
	language = models.CharField('taal', max_length=20)
	class Meta:
		verbose_name_plural = "Disclaimer pagina"

class Ebook(models.Model):
	name = models.CharField('naam', max_length=20)
	path = models.FilePathField(max_length=100, editable=False)
	language = models.CharField('taal', max_length=3)
	available = models.BooleanField('Beschikbaar', default=True)
	class Meta:
		verbose_name_plural = "Ebooks"

	def __unicode__(self):
		return u'{0}'.format(self.name)

class EbookRequests(models.Model):
	email = models.EmailField(max_length=70)
	ebook_id = models.ForeignKey(Ebook, blank=True, null=True, on_delete=models.PROTECT)
	send = models.BooleanField()
	class Meta:
		verbose_name_plural = "EbookRequests"
		verbose_name = "EbookRequest"

class Properties(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	title_dutch = models.CharField(max_length=100)
	title_french = models.CharField(max_length=100)
	street = models.CharField('straat', max_length=50)
	housenumber = models.CharField('huisnummer', max_length=4)
	busnumber = models.CharField('busnummer', max_length=3, blank=True)
	postalcode = models.CharField('postcode', max_length=10)
	city = models.CharField('dorp/stad', max_length=30)
	longitude = models.CharField(max_length=10, editable=False)
	latitude = models.CharField(max_length=10, editable=False)
	price = models.CharField('prijs', max_length=8)
	BUILDINGTYPE = (
		('O', 'Open'),
		('H', 'Half'),
		('CL', 'Closed'),
		('A', 'Appartment'),
		('M', 'Mezzanine'),
		('B', 'Bungalow'),
		('CA', 'Caravan'),
	)
	buildingtype = models.CharField('gebouwtype', max_length=2, choices=BUILDINGTYPE, default=BUILDINGTYPE[0][0])
	sale = models.BooleanField('verkopen', default=True)
	area = models.CharField('oppervlakte', max_length=10)
	livingarea = models.CharField('leef oppervlakte', max_length=10)
	year = models.CharField('bouwjaar', max_length=4) #buildyear
	rateable_value = models.CharField('kadastraal inkomen', max_length=8) #kadastraal inkomen
	description_dutch = models.TextField()
	description_french = models.TextField()
	HEATING_TYPE = (
		('E', 'Electric'),
		('G', 'Gas'),
		('F', 'Furnace'),
		('H', 'Heat pump'),
		('S', 'Special'),
	)
	heating_type = models.CharField('verwarmingstype', max_length=1, choices=HEATING_TYPE, default=HEATING_TYPE[0][0])
	energy_label = models.CharField('energie label', max_length=5)
	extra_information_dutch = models.TextField()
	extra_information_french = models.TextField()
	available = models.BooleanField('Beschikbaar', default=True)
	sold = models.BooleanField('verkocht')
	date_created = models.DateTimeField(editable=False)
	date_modified = models.DateTimeField(editable=False)
	pub_date = models.DateTimeField()
	class Meta:
		verbose_name_plural = "Panden"
		verbose_name = "Pand"

	def get_priorityImage(self):
		priorityImage = Photo.objects.filter(property_id = self, priority = True)
		return priorityImage

	def save(self, *args, **kwargs):
		# Property_street=self.street
		# Property_streetnumber=self.housenumber
		# Property_postalcode=self.postalcode
		# Property_city=self.city
		#
		# # making the url for the google maps.
		# location=Property_street+Property_streetnumber+','+Property_postalcode+Property_city
		#
		# gmaps = googlemaps.Client(key='AIzaSyDP2GIaLZod3VOwu9rh0fdyxbiNBAmNswE')
		#
	    # # Geocoding an address
		# geocode_result = gmaps.geocode(location)
		#
		# # if (geocode_result):
	    # # query json
		# latitude = geocode_result[0]["geometry"]["location"]["lat"]
		# longitude = geocode_result[0]["geometry"]["location"]["lng"]
		#
	    # # adding longitude and latitude to the database
		# self.longitude = longitude
		# self.latitude = latitude
		# else:
			# raise ValidationError({'street': 'controleer straatnaam'}
			# raise ValidationError({'housenumber': 'controleer huisnumber'}
			# raise ValidationError({'postalcode': 'controleer postcode'}
			# raise ValidationError({'city': 'controleer gemeente'}
		# full link to google maps geolocation api with right key: https://maps.googleapis.com/maps/api/geocode/json?address=Lindelei35,2620Hemiksem&key=AIzaSyCpFy6NnC1cbEvM8bLRAgzGskxYUeTL-_M

		if not self.id:
			self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()
		return super(Properties, self).save(*args, **kwargs)
	def __unicode__(self):
		return  self.title_dutch

class PropertyDocuments(models.Model):
	property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, default = 'Pand Informatie')
	document = models.FileField(storage = fs, upload_to = 'uploads/', null=True)
	available = models.BooleanField('Bestand weergeven')
	remove_the_file = models.BooleanField('Verwijder document')

	def save(self):
		if self.remove_the_file:
			super(PropertyDocuments, self).delete()
			return
		super(PropertyDocuments, self).save()


class Partner(models.Model):
	name = models.CharField(max_length=30)
	text = models.TextField()
	photo = models.ImageField(storage = fs, default='/media/partner.jpg')
	available = models.BooleanField('zichtbaar')
	class Meta:
		verbose_name_plural = "Partners"
		verbose_name = "Partner"

class PlanningInfo(models.Model): #moet nog vertaald worden
	property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
	voorkooprecht = models.BooleanField()
	bouwvergunning = models.BooleanField()
	dagvaarding = models.BooleanField()
	verkaveling = models.BooleanField()
	juridische_beslissing = models.BooleanField()
	co2_emission = models.CharField(max_length=5)
	epc = models.CharField(max_length=10)
	unique_code = models.CharField(max_length=10)

class Photo(models.Model):
	property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
	photo = models.ImageField(storage = fs)
	priority = models.BooleanField('Kies als hoofdfoto')
	remove_the_file = models.BooleanField('Verwijder foto')
	def image_thumb(self):
		return '<img src="/media/%s" width="100" height="100" />' % (self.photo)
	image_thumb.allow_tags = True

	def save(self):
		if self.remove_the_file:
			super(Photo, self).delete()
			return
		super(Photo, self).save()

class Room(models.Model):
	property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
	area = models.CharField('oppervlakte', max_length=8)

	class meta:
		abstract = True

class Bathroom(Room):
	bath_type = models.CharField('type bad', max_length=15)
	class Meta:
		verbose_name = "Badkamer"

class Bedroom(Room):
	class Meta:
		verbose_name = "Slaapkamer"

class Garage(Room):
	pass

class Toilet(Room):
	class Meta:
		verbose_name_plural = "Toiletten"

class Kitchen(Room):
	class Meta:
		verbose_name = "Keuken"

class Livingroom(Room):
	class Meta:
		verbose_name = "Woonkamer"

class Storageroom(Room):
	class Meta:
		verbose_name_plural = "Bergingen"
		verbose_name = "Berging"

class Basement(Room):
	class Meta:
		verbose_name = "Kelder"

class Attic(Room):
	class Meta:
		verbose_name = "Zolder"

class Translations(models.Model):
	english = models.CharField(max_length=30)
	french = models.CharField(max_length=30)
	dutch = models.CharField(max_length=30)

class Faq(models.Model):
	question = models.TextField('vraag')
	answer = tinymce_models.HTMLField('antwoord')
	visible = models.BooleanField('zichtbaar', default=True)
	pub_date = models.DateTimeField()

	def __unicode__(self):
		return self.question

	class Meta:
		verbose_name_plural = "Faq's"
		verbose_name = "Faq"

class Newsletter(models.Model):
	email = models.EmailField()
	class Meta:
		verbose_name_plural = "Nieuwsbrief"
		verbose_name = "Nieuwsbrief"

class Status(models.Model):
	STATUS = [
		('', ''),
		('WB', 'Word Behandeld'),
		('C', 'Compromis'),
		('F', 'Finale Akte'),
	]
	datum = models.DateField(default=date.today)
	dossierStatus = models.CharField(max_length=2, choices=STATUS, default=STATUS[0][0])
	eigendom = models.ForeignKey(Properties,on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = "Status"

@receiver(post_delete, sender=Photo)
def photo_post_delete_handler(sender, **kwargs):
	picture = kwargs['instance']
	storage, path = picture.photo.storage, picture.photo.path
	storage.delete(path)

@receiver(post_delete, sender=PropertyDocuments)
def photo_post_delete_handler(sender, **kwargs):
	storedFile = kwargs['instance']
	storage, path = storedFile.document.storage, storedFile.document.path
	storage.delete(path)
