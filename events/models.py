from django.db import models
from common.models import mentor,company,candidate

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=100,null=True) 
    location = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    join_link = models.URLField()
    category = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='static/uploads/events',null=True)
    mentor = models.ForeignKey(mentor, on_delete=models.SET_NULL,null=True)
    # company = models.ForeignKey(company, on_delete=models.SET_NULL,null=True,default=None)

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)