from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

class UserDetails(models.Model):
	user = models.OneToOneField(User)
	phonenumber = models.CharField(max_length=12)
	street = models.CharField(max_length=50)
	housenumber = models.CharField(max_length=4)
	busnumber = models.CharField(max_length=3, null=True, blank=True)
	postalcode = models.CharField(max_length=10)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)

class Aboutpage(models.Model):
    title = models.CharField(max_length=60)
    text = HTMLField()
	# text = HTMLField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) makes it bigger because you can't resize it to what you need.

class Ebook(models.Model):
	name = models.CharField(max_length=20)
	path = models.FilePathField(max_length=100)
	language = models.CharField(max_length=3)
	available = models.BooleanField()

class EbookRequests(models.Model):
	email = models.EmailField(max_length=70)
	ebook_id = models.ForeignKey(Ebook, on_delete=models.PROTECT)
	send = models.BooleanField()

class Properties(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	title = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	housenumber = models.CharField(max_length=4)
	busnumber = models.CharField(max_length=3)
	postalcode = models.CharField(max_length=10)
	city = models.CharField(max_length=30)
	longitude = models.CharField(max_length=10, editable=False)
	latitude = models.CharField(max_length=10, editable=False)
	price = models.CharField(max_length=8)
	BUILDINGTYPE = (
		('O', 'Open'),
		('H', 'Half'),
		('CL', 'Closed'),
		('A', 'Appartment'),
		('M', 'Mezzanine'),
		('B', 'Bungalow'),
		('CA', 'Caravan'),
	)
	buildingtype = models.CharField(max_length=1, choices=BUILDINGTYPE, default=BUILDINGTYPE[0][0])
	sale = models.BooleanField()
	area = models.CharField(max_length=10)
	livingarea = models.CharField(max_length=10)
	year = models.CharField(max_length=4) #buildyear
	rateable_value = models.CharField(max_length=8) #kadastraal inkomen
	description = models.TextField()
	HEATING_TYPE = (
		('E', 'Electric'),
		('G', 'Gas'),
		('F', 'Furnace'),
		('H', 'Heat pump'),
		('S', 'Special'),
	)
	heating_type = models.CharField(max_length=1, choices=HEATING_TYPE, default=HEATING_TYPE[0][0])
	energy_label = models.CharField(max_length=5)
	extra_information = models.TextField()
	available = models.BooleanField()
	sold = models.BooleanField()

class PropertyDocuments(models.Model):
	property_id = models.ForeignKey(Properties, on_delete=models.PROTECT)
	path = models.FilePathField(max_length=100)
	available = models.BooleanField()

class PropertyPictures(models.Model):
	property_id = models.ForeignKey(Properties, on_delete=models.PROTECT)
	path = models.FilePathField(max_length=100)

class PlanningInfo(models.Model): #moet nog vertaald worden
	property_id = models.ForeignKey(Properties, on_delete=models.PROTECT)
	voorkooprecht = models.BooleanField()
	bouwvergunning = models.BooleanField()
	dagvaarding = models.BooleanField()
	verkaveling = models.BooleanField()
	juridische_beslissing = models.BooleanField()
	co2_emission = models.CharField(max_length=5)
	epc = models.CharField(max_length=10)
	unique_code = models.CharField(max_length=10)

class Room(models.Model):
	property_id = models.ForeignKey(Properties, on_delete=models.PROTECT)
	area = models.CharField(max_length=8)

	class meta:
		abstract = True

class Bathroom(Room):
	bath_type = models.CharField(max_length=15)

class Bedroom(Room):
	pass

class Garage(Room):
	pass

class Toilet(Room):
	pass

class Kitchen(Room):
	pass

class Livingroom(Room):
	pass

class Storageroom(Room):
	pass

class Translations(models.Model):
	english = models.CharField(max_length=30)
	french = models.CharField(max_length=30)
	dutch = models.CharField(max_length=30)
