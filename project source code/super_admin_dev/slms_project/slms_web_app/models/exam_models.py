from datetime import datetime
from django.db import models
from django.forms import DateTimeField
from .master_models import subject_master,year_master,exam_type_master
from .manage_models import Teacher_profile, class_master,Teacher_user
from .paper_models import question_paper_model
from .manage_models import branch
from .master_models import exam_type_master
from datetime import  datetime
# # ######################################################################################################################################
# '''paper's Models'''
# # ######################################################################################################################################
# paper model
class exam_model(models.Model):
    # page 01 data
    APPROVAL_CHOICES = (
        ('1', 'Approved'),
        ('2', 'Rejected'),
        ('3', 'Pending'),
    )
    exam_ID = models.CharField(unique=True,max_length=50)
    exam_name = models.CharField(unique=True, max_length=255)
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    year = models.CharField(default='',max_length=255)
    total_papers = models.CharField(default='',max_length=255)
    exam_type_fk = models.ForeignKey(exam_type_master, verbose_name=("exam_type_fk"), on_delete=models.CASCADE,blank=True,null=True)
    branch_FK = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    negative_marking_status = models.BooleanField(default=False)

    published_status = models.BooleanField(default=False)
    approved_status = models.CharField(max_length=1, choices=APPROVAL_CHOICES,default='3')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)


    class Meta:
        unique_together = ('exam_ID', 'exam_name','class_fk','year')


# paper detail model
class exam_paper_detail(models.Model):
    exam_fk = models.ForeignKey(exam_model, verbose_name=("exam_fk"), on_delete=models.CASCADE)
    paper_fk = models.ForeignKey(question_paper_model, verbose_name=("paper_fk"), on_delete=models.CASCADE)
    # total_time = models.CharField(default='',max_length=50)
    exam_start_date_time = models.DateTimeField(default=datetime.now())
    exam_end_date_time = models.DateTimeField(default=datetime.now())
    # exam_start_time = models.TimeField()
    # exam_end_time = models.TimeField()
    proctor_fk = models.ForeignKey(Teacher_profile, verbose_name=("proctor_fk"), on_delete=models.CASCADE)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)
