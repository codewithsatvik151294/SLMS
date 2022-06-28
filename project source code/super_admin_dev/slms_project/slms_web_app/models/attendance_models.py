from django.db import models
from .master_models import *
from .manage_models import *
from datetime import  datetime
# # ######################################################################################################################################
# '''Attendance Models'''
# # ######################################################################################################################################
# Attendance model
class attendance_model(models.Model):
    STATUS_CHOICES = (
        ('1', 'Present'),
        ('2', 'Absent'),
        ('3', 'Pending'),
    )

    attendance_ID = models.CharField(unique=True,max_length=50)
    attendance_session = models.CharField(max_length=50,default='')

    student_fk = models.ForeignKey(student_profile, verbose_name=("student_fk"), on_delete=models.CASCADE)
    branch_fk = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    section_fk = models.ForeignKey(section_master, verbose_name=("section_fk"), on_delete=models.CASCADE)

    attendance_status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='3')
    attendance_date  = models.DateField(auto_now=False, auto_now_add=False)

    
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    class Meta:
        unique_together = ('attendance_ID','attendance_session','student_fk','branch_fk','class_fk','section_fk','attendance_date')

