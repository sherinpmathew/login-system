
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django_countries.fields import CountryField
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    
    is_admin=models.BooleanField('is_admin',default=True)
    is_student=models.BooleanField('is_student',default=True)
    is_staff=models.BooleanField('is_staff',default=True)
    is_editor=models.BooleanField('is_editor',default=True)
    country = models.CharField(max_length=200,blank=True,null=True)


    mobile = RegexValidator(regex="0-9",message=("enter a valid phone number"))
    nationality = models.CharField(max_length=100,default=False)
   


# Name
# Role
# email
# country
# nationality
# mobile
# password