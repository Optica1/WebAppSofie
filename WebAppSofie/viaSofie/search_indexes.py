import datetime
from haystack import indexes

from .models import *


class PropertiesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    postalcode = indexes.CharField(model_attr='postalcode')
    city = indexes.CharField(model_attr='city')
    price = indexes.CharField(model_attr='price')

    def get_model(self):
        return Properties

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
