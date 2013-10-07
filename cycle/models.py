from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Cycle(models.Model):
    winner = models.ForeignKey(User, related_name='winner_user', default=None, blank=True, null=True)
    place_two = models.ForeignKey(User, related_name='place_to_user', default=None, blank=True, null=True)
    place_three = models.ForeignKey(User, related_name='place_three_user', default=None, blank=True, null=True)
    is_active =  models.BooleanField(default=False)
    start_date = models.DateTimeField(default = datetime.now)

def __unicode__(self):
        return u"Cycle N%d" % self.id
