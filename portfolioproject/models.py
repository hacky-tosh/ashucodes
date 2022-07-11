from django.db import models
import datetime
# Create your models here.
#from hitcount.models import HitCountMixin
#from hitcount.settings import MODEL_HITCOUNT


class Contact(models.Model):

    # contact us form
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField()
    date  = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

#class hitcountview(models.Model,HitCountMixin):
 #   hit_count_genric = GenricRelation(
  #          MODEL_HITCOUNT, object_id_field = 'object_pk',
   #         related_query_name = 'hitcount_genric_relation')



