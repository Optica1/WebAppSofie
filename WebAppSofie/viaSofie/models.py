from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class UserDetails(models.Model):
    user = models.OneToOneField(User)
    phonenumber = models.CharField(max_length=12)

class Client(models.Model):
    voornaam = models.CharField(max_length=60)
    achternaam = models.CharField(max_length=60)

class Aboutpage(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(max_length=1024)

class Ebook(models.Model):
	name = models.CharField(max_length=20)
	path = models.FilePathField(max_length=100)
	language = models.CharField(max_length=3)
	available = models.BooleanField()

class EbookRequests(models.Model):
	email = models.EmailField(max_length=70)
	ebook_id = models.ForeignKey(Reporter, on_delete=models.PROTECT)
	send = models.BooleanField()

class Properties(models.Model):
	title =
	address =
	price =
	buildingtype = 
	sale = models.BooleanField()
	area =
	livingarea =
	bedrooms =
	bathrooms =
	garages =
	floors =
	extra_sections = 
	year =
	rateable_value =
	description =
	heating =
	available = models.BooleanField()
	sold = models.BooleanField()







	1. naam + korte beschrijving (titel)
2. adres
3. oppervlakte
4. vraagprijs
5. huis/appartement
6. verhuren/verkopen
7. aantal badkamers
8. aantal slaapkamers
9. aantal garages
10. aantal verdiepingen
11. beschrijving indeling huis
1. aantal toiletten
2. zolder (ja of nee)
3. kelder (ja of nee)
4. zonnepanelen (ja of nee)
5. …
12. omschrijving huis (korte tekst)
13. soort verwarming (CV / stookolie / ...)
14. beschrijving tuin/…
15. energieprestatie en keuringsverslagen.
16. Stedenbouwkundige voorschriften
17. ligging (google maps)
18. oppervlakte (bewoonbare / grond)
19. Kadastraal inkomen
20. Bouwjaar
21. extra informatie
22. documenten (voor een plan of andere informatie)

class PropertyDocuments (models.Model):
	property_id = models.ForeignKey(Properties, on_delete=models.PROTECT)
	path = models.FilePathField(max_length=100)
	available = models.BooleanField()