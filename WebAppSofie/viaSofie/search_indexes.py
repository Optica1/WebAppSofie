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
    photo = models.ImageField()
    priority = models.IntegerField()

    def get_model(self):
        return Properties

    def prepare(self, object):
        """
        Prepare the search data
        """
        self.prepared_data = super(PropertiesIndex, self).prepare(object)

        # Retrieve the tutorial metas and return the prepared data
        meta = get_Photo(property_id_id=object.pand_id)
        self.prepared_data['photo'] = meta.photo
        self.prepared_data['priority'] = meta.priority
