from datetime import datetime
from email.policy import default
from django.db import models
from django.forms import DateTimeField
from sqlalchemy import null
from .master_models import *
from .manage_models import *
from .paper_models import *
from .manage_models import *
from datetime import  datetime
# # ######################################################################################################################################
# '''time table's Models'''
# # ######################################################################################################################################
# time table model
class time_table_model(models.Model):
    STATUS_CHOICES = (
        ('1', 'Active'),
        ('2', 'Inactive'),
        ('3', 'Pending'),
    )

    MONTH_CHOICES = (
        ('1', 'January'),
        ('2', 'Feburary'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    )

    time_table_ID = models.CharField(unique=True,max_length=50)
    time_table_session = models.CharField(max_length=50,default='')
    time_table_effective_from = models.CharField(max_length=2, choices=MONTH_CHOICES,default='0')

    year_fk = models.ForeignKey(year_master, verbose_name=("year_fk"), on_delete=models.CASCADE)
    branch_fk = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    section_fk = models.ForeignKey(section_master, verbose_name=("section_fk"), on_delete=models.CASCADE)


    monday_slot = models.TextField(default='[]')
    tuesday_slot = models.TextField(default='[]')
    wednesday_slot = models.TextField(default='[]')
    thursday_slot = models.TextField(default='[]')
    friday_slot = models.TextField(default='[]')
    saturday_slot = models.TextField(default='[]')

    time_table_active_status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='2')
    
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    class Meta:
        unique_together = ('time_table_session','time_table_effective_from','year_fk','branch_fk','class_fk','section_fk')

