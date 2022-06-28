from datetime import datetime
from django.db import models
from django.forms import DateTimeField
from django.contrib.auth.models import User
# Create your models here.


# user type model
class userType(models.Model):
    USERTYPE_CHOICES = (
        ('1', 'Director'),
        ('2', 'SchoolAdmin'),
        ('3', 'Principal'),
        ('4', 'ClassTeacher'),
        ('5', 'Teacher'),
        ('6', 'Student'),
        ('7', 'Parent'),
    )
    userType =models.CharField(max_length=1,unique=True, choices=USERTYPE_CHOICES)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)



class super_admin_profile(models.Model):
    user_fk = models.OneToOneField(User, verbose_name=("user_fk"), on_delete=models.CASCADE)
    super_admin_contact = models.CharField(max_length=10,blank=True,null=True)
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    super_admin_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    super_admin_profile_image = models.ImageField(upload_to='Upload_Images/super_admin_profile_image/',blank=True,null=True)
