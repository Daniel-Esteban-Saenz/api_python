from django.db import models

# Create your models here.

class programer(models.Model):
    Fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None)
    is_active = models.BooleanField(default=True)
    
    
class student(models.Model):
    Name = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Sex = models.CharField(max_length=1)
    Numtoken = models.PositiveBigIntegerField(max_length=7)
    Formationstatus =models.BooleanField(default=True)
    Admissiondate =models.DateField()
    is_active = models.BooleanField(default=True)
    