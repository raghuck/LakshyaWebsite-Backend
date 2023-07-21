from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class candidate(models.Model):
    email = models.EmailField(max_length=250,primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    type = models.CharField(max_length=10) #Student or Woman
    age = models.ImageField(null=True)
    resume = models.FileField(upload_to='static/uploads/resume',null=True)
    pp = models.ImageField(upload_to="static/uploads/pp",null=True)
    
class mentor(models.Model):
    email = models.EmailField(max_length=250,primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    pp = models.ImageField(upload_to="static/uploads/pp",null=True)
    
class company(models.Model):
    email = models.EmailField(max_length=250,primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="static/uploads/logo",null=True)

class skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    
