from datetime import datetime
from email.policy import default
from django.db import models
from django.forms import DateTimeField
from .master_models import *
from .manage_models import *
from .paper_models import *
from .manage_models import *
from datetime import  datetime
# # ######################################################################################################################################
# '''paper's Models'''
# # ######################################################################################################################################
# paper model
class assignment_model(models.Model):
    assignment_ID = models.CharField(unique=True,max_length=50)
    assignment_name = models.CharField(unique=True, max_length=255)
    branch_FK = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    section_fk = models.ForeignKey(section_master, verbose_name=("section_fk"), on_delete=models.CASCADE)
    subject_fk = models.ForeignKey(subject_master, verbose_name=("subject_fk"), on_delete=models.CASCADE)
    total_marks = models.CharField(default='',max_length=255)
    passing_marks = models.CharField(default='',max_length=255)
    starts_at  = models.DateTimeField(auto_now_add=True)
    ends_at  = models.DateTimeField(auto_now_add=True)
    questionType = models.TextField(default='')
    guidelines = models.TextField(default='')
    question_array = models.TextField(default='')
    published_status = models.BooleanField(default=False)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)


    class Meta:
        unique_together = ('assignment_ID', 'assignment_name','branch_FK','class_fk')

