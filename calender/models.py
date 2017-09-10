from django.db import models
from django.utils import timezone


class Calender(models.Model):    
    creator_name = models.CharField(max_length=40, default="Admin")
    event_level = models.CharField(max_length=10, default="General")
    event_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)
    def __str__(self):
        return 'Event:{} On {}'.format(self.event_name,self.start_date)
