import datetime
from haystack import indexes

from .models import *


class PropertiesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    postalcode = indexes.CharField(model_attr='postalcode')
    city = indexes.CharField(model_attr='city')
    price = indexes.CharField(model_attr='price')
    title_dutch = indexes.CharField(model_attr='title_dutch')
    description_dutch = indexes.CharField(model_attr='description_dutch')
    pand_id = indexes.IntegerField(model_attr='id')

    def get_model(self):
        return Properties

    def get_priorityImage(self):
		priorityImage = Photo.filter(property_id = self, priority = True)
		return priorityImage

class PictureIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    photo = indexes.CharField(model_attr='photo')
    priority = indexes.CharField(model_attr='priority')

    def get_model(self):
        return Photo
