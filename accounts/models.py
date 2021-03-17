from django.db import models
from django import forms 
# Create your models here.
class loan(models.Model):
    sn= models.IntegerField()
    pa= models.FloatField()
    pap=models.FloatField()
    iap=models.FloatField()
    lob=models.FloatField()
    
