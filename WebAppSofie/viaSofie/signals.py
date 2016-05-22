import googlemaps
import json
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

from my_user_profile_app.models import UserDetails

@receiver(pre_save, sender=User)
def model_pre_change(sender, **kwargs):
    Propertie_street=UserDetails.street
    Propertie_streetnumber=UserDetails.housenumber
    Propertie_postalcode=UserDetails.postalcode
    Propertie_city=UserDetails.city
    location=Propertie_street+Propertie_streetnumber+','+Propertie_postalcode+Propertie_city

    gmaps = googlemaps.Client(key='AIzaSyCpFy6NnC1cbEvM8bLRAgzGskxYUeTL-_M')

    # Geocoding an address
    geocode_result = gmaps.geocode(location)

    # query schrijven voor de json die we hebben terug gekregen om dan de longitude en latitude mee in de database te steken.
    latitude = geocode_result[0]["geometry"]["location"]["lat"]
    longitude = geocode_result[0]["geometry"]["location"]["lng"]

    Propertie=viaSofie_properties(longitude=longitude, latitude=latitude)
    Propertie.save()

    # full link to google maps geolocation api with right key: https://maps.googleapis.com/maps/api/geocode/json?address=Lindelei35,2620Hemiksem&key=AIzaSyCpFy6NnC1cbEvM8bLRAgzGskxYUeTL-_M
