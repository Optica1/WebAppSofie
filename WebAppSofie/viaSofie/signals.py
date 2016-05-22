import googlemaps
import json
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from my_user_profile_app.models import UserDetails


@receiver(pre_save, sender=User)
def model_pre_change(sender, **kwargs):
    Userdetails_street=UserDetails.street
    Userdetails_streetnumber=UserDetails.housenumber
    Userdatails_postalcode=UserDetails.postalcode
    Userdetails_city=UserDetails.city
    location=Userdetails_street+Userdetails_streetnumber+','+Userdatails_postalcode+Userdetails_city

    gmaps = googlemaps.Client(key='AIzaSyCpFy6NnC1cbEvM8bLRAgzGskxYUeTL-_M')

    # Geocoding an address
    geocode_result = gmaps.geocode(location)

    # query schrijven voor de json die we hebben terug gekregen om dan de longitude en latitude mee in de database te steken.
    latitude = geocode_result[0]["geometry"]["location"]["lat"]
    longitude = geocode_result[0]["geometry"]["location"]["lng"]

    UserDetails.longitude=longitude
    UserDetails.latitude=latitude

    # full link to google maps geolocation api with right key: https://maps.googleapis.com/maps/api/geocode/json?address=Lindelei35,2620Hemiksem&key=AIzaSyCpFy6NnC1cbEvM8bLRAgzGskxYUeTL-_M
