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
# '''paper's Models'''
# # ######################################################################################################################################
# paper model
class study_material(models.Model):
    study_material_ID = models.CharField(unique=True,max_length=50)
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    branch_fk = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    subject_fk = models.ForeignKey(subject_master, verbose_name=("subject_fk"), on_delete=models.CASCADE)
    topic = models.CharField(default='',max_length=255)
    file_type_fk = models.ForeignKey(file_type_master, verbose_name=("section_fk"), on_delete=models.CASCADE)
    content = models.FileField(upload_to='upload_assignment_content/content/',null=True,blank=True)
    published_status = models.BooleanField(default=False)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    class Meta:
        unique_together = ('study_material_ID', 'class_fk','branch_fk','subject_fk','topic')

