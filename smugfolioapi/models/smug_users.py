from django.db import models
from django.contrib.auth.models import User

class Smug_Users(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    business_name = models.CharField(max_length=256)
    business_owner = models.BooleanField()
    
    