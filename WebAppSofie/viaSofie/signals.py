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



        https://maps.googleapis.com/maps/api/geocode/json?address=Lindelei35,2620Hemiksem&key=AIzaSyCpFy6NnC1cbEvM8bLRAgzGskxYUeTL-_M
# @receiver(post_save, sender=User)
# def handle_user_save(sender, instance, created, **kwargs):
#   if created:
#     UserDetails.objects.create(user=instance)
