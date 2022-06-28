from datetime import datetime
from django.db import models
from django.forms import DateTimeField
from .master_models import subject_master,year_master,question_type_master
from .manage_models import class_master,topic_master,branch


# ######################################################################################################################################
'''question_bank's Models'''
# ######################################################################################################################################
# branch model
class question(models.Model):
    question_ID = models.CharField(unique=True,max_length=50)
    branch_fk = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE)
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    subject_fk = models.ForeignKey(subject_master, verbose_name=("subject_fk"), on_delete=models.CASCADE)
    year_fk = models.ForeignKey(year_master, verbose_name=("year_fk"), on_delete=models.CASCADE)

    topic_name = models.TextField()
    question_type_fk = models.ForeignKey(question_type_master, verbose_name=("question_type_fk"), on_delete=models.CASCADE)
    question_subtype_type = models.CharField(max_length=255,default='')

    question_text = models.TextField()
    option_count = models.CharField(default=0, max_length=20)
    option_array = models.TextField(default='[]')

    DIFFICULTY_CHOICES = (
        ('1', 'Easy'),
        ('2', 'Moderate'),
        ('3', 'Hard'),
    )
    difficulty_type = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES,default='1')
    correct_mark = models.CharField(default=0, max_length=20)
    negative_mark = models.CharField(default=0, max_length=20)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)


    class Meta:
        unique_together = ('class_fk', 'subject_fk','year_fk','topic_name','question_type_fk','question_subtype_type','question_text')


