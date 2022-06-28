from datetime import datetime
from django.db import models
from django.forms import DateTimeField
from sqlalchemy import null
from .master_models import badge_trigger_master

# ######################################################################################################################################
'''badge_management's Models'''
# ######################################################################################################################################
# branch model
class badge_management(models.Model):
    badge_ID = models.CharField(unique=True,max_length=50)
    badge_title = models.CharField(unique=True,max_length=255)
    badge_trigger_fk = models.OneToOneField(badge_trigger_master, verbose_name=("badge_trigger_fk"), on_delete=models.CASCADE,unique=True)
    badge_image = models.ImageField(upload_to='Upload_badge/badge_images/',blank=True,null=True)
    badge_desrciption = models.TextField(default='')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)
