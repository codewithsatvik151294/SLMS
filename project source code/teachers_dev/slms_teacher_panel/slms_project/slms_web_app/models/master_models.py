from datetime import datetime
from django.db import models
# ######################################################################################################################################
'''class_type_master's Models'''
# ######################################################################################################################################
# class_type_master model
class class_type_master(models.Model):
    classTypeID = models.CharField(unique=True,max_length=30)
    classType_name = models.CharField(max_length=255)
    class_subType_name = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('classType_name','class_subType_name')

    def __str__(self):
        return f"{self.classTypeID} - {self.classType_name} - {self.class_subType_name}"
    


# ######################################################################################################################################
'''section_master's Models'''
# ######################################################################################################################################
# section_master model
class section_master(models.Model):
    sectionID = models.CharField(unique=True,max_length=30)
    section_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('sectionID', 'section_name')

    def __str__(self):
        return f"{self.sectionID} - {self.section_name}"


# ######################################################################################################################################
'''section_detail's Models'''
# ######################################################################################################################################
# section_detail model
class section_detail(models.Model):
    section_fk = models.ForeignKey(section_master, verbose_name=("section_fk"), on_delete=models.CASCADE)
    classType_fk = models.ForeignKey(class_type_master, verbose_name=("classType_fk"), on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    def __str__(self):
        return f"{self.section_fk} - {self.classType_fk}"


# ######################################################################################################################################
'''subject_master's Models'''
# ######################################################################################################################################
# subject_master model
class subject_master(models.Model):
    subjectID = models.CharField(unique=True,max_length=30)
    subject_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('subjectID', 'subject_name')

    def __str__(self):
        return f"{self.subjectID} - {self.subject_name}"





# ######################################################################################################################################
'''year_master's Models'''
# ######################################################################################################################################
# year_master model
class year_master(models.Model):
    yearID = models.CharField(unique=True,max_length=30)
    year_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('yearID', 'year_name')

    def __str__(self):
        return f"{self.yearID} - {self.year_name}"



# ######################################################################################################################################
'''designation_master's Models'''
# ######################################################################################################################################
# designation_master model
class user_designation_master(models.Model):
    designationID = models.CharField(unique=True,max_length=30)
    designation_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('designationID', 'designation_name')

    def __str__(self):
        return f"{self.designationID} - {self.designation_name}"


# ######################################################################################################################################
'''authority_master's Models'''
# ######################################################################################################################################
# authority_master model
class Authority_master(models.Model):
    authorityID = models.CharField(unique=True,max_length=30)
    authority_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('authorityID', 'authority_name')

    def __str__(self):
        return f"{self.authorityID} - {self.authority_name}"


# ######################################################################################################################################
'''sub_authority_master's Models'''
# ######################################################################################################################################
# subAuthority_master model
class SubAuthority_master(models.Model):
    subAuthorityID = models.CharField(unique=True,max_length=30)
    subAuthority_name = models.TextField(default='[]')
    authority_FK = models.ForeignKey(Authority_master, verbose_name=("authority_FK"), on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('subAuthorityID', 'subAuthority_name')

    def __str__(self):
        return f"{self.subAuthorityID} - {self.subAuthority_name}"


# ######################################################################################################################################
'''question_type's Models'''
# ######################################################################################################################################
# subAuthority_master model
class question_type_master(models.Model):
    questionTypeID = models.CharField(unique=True,max_length=30)
    questionType_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('questionTypeID', 'questionType_name')

    def __str__(self):
        return f"{self.questionTypeID} - {self.questionType_name}"


# ######################################################################################################################################
'''badge_trigger's Models'''
# ######################################################################################################################################
# subAuthority_master model
class badge_trigger_master(models.Model):
    badge_triggerID = models.CharField(unique=True,max_length=30)
    badge_trigger_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('badge_triggerID', 'badge_trigger_name')

    def __str__(self):
        return f"{self.badge_triggerID} - {self.badge_trigger_name}"


# ######################################################################################################################################
'''file_type's Models'''
# ######################################################################################################################################
# subAuthority_master model
class file_type_master(models.Model):
    file_typeID = models.CharField(unique=True,max_length=30)
    file_type_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('file_typeID', 'file_type_name')

    def __str__(self):
        return f"{self.file_typeID} - {self.file_type_name}"


# ######################################################################################################################################
'''exam type's Models'''
# ######################################################################################################################################
# subAuthority_master model
class exam_type_master(models.Model):
    exam_typeID = models.CharField(unique=True,max_length=30)
    exam_type_name = models.CharField(unique=True,max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('exam_typeID', 'exam_type_name')

    def __str__(self):
        return f"{self.exam_typeID} - {self.exam_type_name}"


