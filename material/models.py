from django.db import models
from common import models as commonModels

# Create your models here.
class studyMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    by = models.ForeignKey(commonModels.mentor, on_delete=models.CASCADE)
    file = models.FileField(upload_to="static/upload/material",null=True)
    link = models.URLField(null=True)
    stat = models.IntegerField(default=0)