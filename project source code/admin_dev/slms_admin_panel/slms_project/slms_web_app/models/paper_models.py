from datetime import datetime
from django.db import models
from django.forms import DateTimeField
from .master_models import subject_master,year_master,question_type_master
from .manage_models import class_master,topic_master,branch


# # ######################################################################################################################################
# '''paper's Models'''
# # ######################################################################################################################################
# paper model
class question_paper_model(models.Model):
    # page 01 data
    paper_ID = models.CharField(unique=True,max_length=50)
    paper_name = models.CharField(unique=True, max_length=255)
    branch_FK = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    subject_fk = models.ForeignKey(subject_master, verbose_name=("subject_fk"), on_delete=models.CASCADE)
    year_fk = models.ForeignKey(year_master, verbose_name=("year_fk"), on_delete=models.CASCADE)
    total_marks = models.CharField(default=0, max_length=50)
    passing_marks = models.CharField(default=0, max_length=50)
    section_count = models.CharField(default=0, max_length=50)
    # total_question_count = models.CharField(default=0, max_length=50)
    section_detail = models.TextField(default='[]')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)


    class Meta:
        unique_together = ('paper_name', 'class_fk','year_fk','subject_fk')