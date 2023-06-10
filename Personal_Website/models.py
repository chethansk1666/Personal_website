from django.db import models
from phonenumbers.phonenumber import PhoneNumber

# Create your models here.
class  Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone = PhoneNumber()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



