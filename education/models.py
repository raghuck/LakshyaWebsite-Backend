from django.db import models
from common import models as commonModels

# Create your models here.
class abrodEdu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    link = models.URLField()
    
class applied(models.Model):
    cadidate = models.ForeignKey(commonModels.candidate,on_delete=models.CASCADE)
    post = models.ForeignKey(abrodEdu,on_delete=models.CASCADE)
    class Meta:
        unique_together = [['cadidate', 'post']]