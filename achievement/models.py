from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from cycle.models import Cycle

class Achievement(models.Model):
    DURATION_CHOICES = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('F', 'Full Cycle'),
    )
    
    CATEGORY_CHOICES = (
        ('E', 'Easy'),
        ('A', 'Average'),
        ('H', 'Hard'),
    )

    name = models.CharField(max_length = 255, unique=True)
    points = models.IntegerField()
    description = models.TextField()   
    deadline = models.DateTimeField()
    duration = models.CharField(max_length=1, choices=DURATION_CHOICES)    
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    user_vote = models.ManyToManyField(User, blank=True, null=True)
    status = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
class CompletedAchievement(models.Model):
    user = models.ForeignKey(User, related_name='completed_achievement')
    achievement = models.ForeignKey(Achievement)
    witness = models.ForeignKey(User, related_name='witness_completed_achievement')
    cycle = models.ForeignKey(Cycle)
    date = models.DateTimeField(default = datetime.now)
    
    def __unicode__(self):
        return u"%s is compleated by %s" % (self.achievement, self.user)
