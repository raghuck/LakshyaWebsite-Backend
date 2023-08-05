import datetime
from django.db import models
from django.core.validators import MinValueValidator
from common.models import company, tag,candidate

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    location = models.CharField(max_length=20,default="Remote")
    description = models.TextField()
    salary = models.FloatField(null=True)
    apply_before = models.DateField()
    MinExperience = models.IntegerField()
    type = models.CharField(max_length=10)
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    startDate = models.DateField()
    whoCanApply = models.CharField(max_length=150)
    postedDate = models.DateField(default=datetime.date.today())
    openings = models.IntegerField()
    perks = models.CharField(max_length=500)

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(tag, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('job','skill'))
        
class jobApplied(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('job','candidate'))