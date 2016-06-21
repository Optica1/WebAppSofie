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
    pand_id = indexes.CharField(model_attr='id')
    # photo = models.ImageField()
    priority = models.BooleanField()
    # priority = indexes.IntegerField(model_attr='id')

    def get_model(self):
        return Properties

    def prepare_photo(self, object):

        self.prepared_data = super(PropertiesIndex, self).prepare(object)

        # Retrieve the photo url and priority
        p = Photo.objects.get(property_id = object.id)
        # meta = get_Photo(property_id=object.id)
        # self.prepared_data['photo'] = [photo.photo for photo in object.photo.filter(property_id = object.pand_id).filter(priority=1)]
        # self.prepared_data['priority'] = [photo.priority for photo in object.photo.filter(property_id = object.pand_id)]
        # self.prepared_data['photo'] = p.photo
        self.prepared_data['priority'] = p.priority
        return self.prepared_data
