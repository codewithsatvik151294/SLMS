from datetime import datetime
from django.db import models
from django.forms import DateTimeField
from .master_models import user_designation_master, Authority_master,SubAuthority_master

# ######################################################################################################################################
'''assign_authority's Models'''
# ######################################################################################################################################
# branch model
class assign_authority(models.Model):
    assign_authorityID = models.CharField(unique=True,max_length=50)
    designation_fk = models.OneToOneField(user_designation_master, verbose_name=("designation_fk"), on_delete=models.CASCADE,unique=True)

    authority_fk = models.TextField(default='[]')
    sub_authority_fk = models.TextField(default='[]')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)
