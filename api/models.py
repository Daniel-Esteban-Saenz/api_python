from django.db import models

# Create your models here.

class programer(models.Model):
    Fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None)
    is_active = models.BooleanField(default=True)