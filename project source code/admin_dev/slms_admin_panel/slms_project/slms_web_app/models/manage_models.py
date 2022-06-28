from datetime import datetime
from django.db import models
from django.forms import DateTimeField
from .master_models import section_master, subject_master
# ######################################################################################################################################
'''Branch's Models'''
# ######################################################################################################################################
# branch model
class branch(models.Model):
    branch_code = models.CharField(unique=True,max_length=30)
    branch_name = models.CharField(unique=True,max_length=255)
    branch_email = models.CharField(unique=True,max_length=255)
    branch_contact = models.CharField(unique=True,max_length=10)
    branch_address = models.TextField(default='',blank=True,null=True)
    branch_pinCode = models.CharField(default='',max_length=6)
    branch_city = models.CharField(default='',max_length=255)
    branch_state = models.CharField(default='',max_length=255)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    class Meta:
        unique_together = ('branch_code', 'branch_name','branch_email','branch_contact',)

    def __str__(self):
        return f"{self.branch_name} - {self.branch_code}"


# ######################################################################################################################################
'''class_master's Models'''
# ######################################################################################################################################
# class_master model
class class_master(models.Model):
    classID = models.CharField(unique=True,max_length=30)
    class_name = models.CharField(max_length=255)
    predessor_class = models.CharField(blank=True,null=True,max_length=100,default='')
    successor_class = models.CharField(blank=True,null=True,max_length=100,default='')
    class_description = models.TextField(blank=True,null=True,default='')
    section_details_fk = models.TextField(blank=True,null=True,default='[]')
    # subject_fk = models.ManyToManyField(subject_master, verbose_name=("subject_fk"))
    subject_fk = models.TextField(blank=True,null=True,default='[]')
    branch_FK = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    class Meta:
        unique_together = ('class_name','branch_FK')

    def __str__(self):
        return f"{self.classID} - {self.class_name}"


# ######################################################################################################################################
'''topic_master's Models'''
# ######################################################################################################################################
# topic_master model
class topic_master(models.Model):
    topicID = models.CharField(unique=True,max_length=30)
    branch_FK = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE,blank=True,null=True)
    class_FK = models.ForeignKey(class_master, verbose_name=("class_FK"), on_delete=models.CASCADE)
    subject_FK = models.ForeignKey(subject_master, verbose_name=("subject_FK"), on_delete=models.CASCADE)
    topic_name = models.TextField(default='[]')
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,default='',max_length=200)

    class Meta:
        unique_together = ('class_FK', 'subject_FK')

    def __str__(self):
        return f"{self.topicID} - {self.class_FK} - {self.subject_FK}"

# ######################################################################################################################################
'''Director's Models'''
# ######################################################################################################################################
# director-user model
class director_user(models.Model):
    director_name = models.CharField(max_length=255)
    director_email = models.CharField(unique=True,max_length=255)
    director_contact = models.CharField(unique=True,max_length=10)
    director_password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='Upload_Images/director_profile_images/',blank=True,null=True)
    status_CHOICES = (
        ('1', 'Active'),
        ('2', 'Inactive'),
        ('3', 'On-hold'),
    )
    active_status = models.CharField(max_length=1, choices=status_CHOICES,default='1')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return self.director_name

# director-profile model
class director_profile(models.Model):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    director_FK = models.OneToOneField(director_user, verbose_name=("director_user_fk"), on_delete=models.CASCADE)
    branch_FK = models.OneToOneField(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE)
    director_DOB = models.DateField(blank=True,null=True)
    director_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    director_fathers_name = models.CharField(default='',max_length=255)
    director_address = models.TextField(default='')
    director_pinCode = models.CharField(default='',max_length=6)
    director_city = models.CharField(default='',max_length=255)
    director_state = models.CharField(default='',max_length=255)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

# ######################################################################################################################################
# ######################################################################################################################################
'''Principal's Models'''
# ######################################################################################################################################
# principal-user model
class principal_user(models.Model):
    principal_name = models.CharField(max_length=255)
    principal_email = models.CharField(unique=True,max_length=255)
    principal_contact = models.CharField(unique=True,max_length=10)
    principal_password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='Upload_Images/principal_profile_images/',blank=True,null=True)
    status_CHOICES = (
        ('1', 'Active'),
        ('2', 'Inactive'),
        ('3', 'On-hold'),
    )
    active_status = models.CharField(max_length=1, choices=status_CHOICES,default='1')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return self.principal_name

# principal-profile model
class principal_profile(models.Model):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    principal_FK = models.OneToOneField(principal_user, verbose_name=("principal_user_fk"), on_delete=models.CASCADE)
    branch_FK = models.OneToOneField(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE)
    principal_DOB = models.DateField(blank=True,null=True)
    principal_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    principal_fathers_name = models.CharField(default='',max_length=255)
    principal_address = models.TextField(default='')
    principal_pinCode = models.CharField(default='',max_length=6)
    principal_city = models.CharField(default='',max_length=255)
    principal_state = models.CharField(default='',max_length=255)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

# ######################################################################################################################################
# ######################################################################################################################################
'''schoolAdmin's Models'''
# ######################################################################################################################################
# schoolAdmin-user model
class schoolAdmin_user(models.Model):
    schoolAdmin_name = models.CharField(max_length=255)
    schoolAdmin_email = models.CharField(unique=True,max_length=255)
    schoolAdmin_contact = models.CharField(unique=True,max_length=10)
    schoolAdmin_password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='Upload_Images/schoolAdmin_profile_images/',blank=True,null=True)
    status_CHOICES = (
        ('1', 'Active'),
        ('2', 'Inactive'),
        ('3', 'On-hold'),
    )
    active_status = models.CharField(max_length=1, choices=status_CHOICES,default='1')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return self.schoolAdmin_name

# schoolAdmin-profile model
class schoolAdmin_profile(models.Model):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    schoolAdmin_FK = models.OneToOneField(schoolAdmin_user, verbose_name=("schoolAdmin_user_fk"), on_delete=models.CASCADE)
    branch_FK = models.OneToOneField(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE)
    schoolAdmin_DOB = models.DateField(blank=True,null=True)
    schoolAdmin_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    schoolAdmin_fathers_name = models.CharField(default='',max_length=255)
    schoolAdmin_address = models.TextField(default='')
    schoolAdmin_pinCode = models.CharField(max_length=6)
    schoolAdmin_city = models.CharField(default='',max_length=255)
    schoolAdmin_state = models.CharField(default='',max_length=255)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)


# ######################################################################################################################################
# ######################################################################################################################################
'''teacher's Models'''
# ######################################################################################################################################
# teacher-user model
class Teacher_user(models.Model):
    teacher_name = models.CharField(max_length=255)
    teacher_email = models.CharField(unique=True,max_length=255)
    teacher_contact = models.CharField(unique=True,max_length=10)
    teacher_password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='Upload_Images/teacher_profile_images/',blank=True,null=True)
    status_CHOICES = (
        ('1', 'Active'),
        ('2', 'Inactive'),
        ('3', 'On-hold'),
    )
    active_status = models.CharField(max_length=1, choices=status_CHOICES,default='1')
    classTeacher_status_CHOICES = (
        ('1', 'teacher'),
        ('2', 'classTeacher'),
    )
    class_teacher_status = models.CharField(max_length=1,choices=classTeacher_status_CHOICES,default='1')
    class_master_fk = models.ForeignKey(class_master, verbose_name=("class_master_fk"), on_delete=models.CASCADE,blank=True,null=True)
    section_master_fk = models.ForeignKey(section_master, verbose_name=("section_master_fk"), on_delete=models.CASCADE,blank=True,null=True)

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return self.teacher_name


# class-section-subject_detail master
class class_section_subject_detail(models.Model):
    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE)
    section_fk = models.ForeignKey(section_master, verbose_name=("section_fk"), on_delete=models.CASCADE)
    subject_fk = models.ForeignKey(subject_master, verbose_name=("subject_fk"), on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return f"{self.class_fk} - {self.section_fk} - {self.subject_fk}"


# teacher-profile model
class Teacher_profile(models.Model):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    teacher_FK = models.OneToOneField(Teacher_user, verbose_name=("teacher_user_fk"), on_delete=models.CASCADE)
    branch_FK = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE)
    teacher_DOB = models.DateField(blank=True,null=True)
    teacher_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    teacher_fathers_name = models.CharField(default='',max_length=255)
    teacher_address = models.TextField(default='')
    teacher_pinCode = models.CharField(default='',max_length=6)
    teacher_city = models.CharField(default='',max_length=255)
    teacher_state = models.CharField(default='',max_length=255)
    class_section_subject_detail_fk = models.TextField(default='[]')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)


# ######################################################################################################################################
# ######################################################################################################################################
'''student's Models'''
# ######################################################################################################################################
# student-user model
class student_user(models.Model):
    student_first_name = models.CharField(max_length=255)
    student_last_name = models.CharField(default='',max_length=255)
    student_email = models.CharField(unique=True,max_length=255)
    student_registration_number = models.CharField(unique=True,max_length=255)
    student_contact = models.CharField(unique=True,max_length=10)
    student_password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='Upload_Images/student_profile_images/',blank=True,null=True)
    status_CHOICES = (
        ('1', 'Active'),
        ('2', 'Inactive'),
        ('3', 'On-hold'),
    )
    active_status = models.CharField(max_length=1, choices=status_CHOICES,default='1')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)



# student-profile model
class student_profile(models.Model):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    student_FK = models.OneToOneField(student_user, verbose_name=("student_user_fk"), on_delete=models.CASCADE)
    branch_FK = models.ForeignKey(branch, verbose_name=("branch_fk"), on_delete=models.CASCADE)
    student_DOB = models.DateField(blank=True,null=True)
    student_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_fathers_name = models.CharField(default='',max_length=255)
    student_parent_relation = models.CharField(default='',max_length=255)
    student_hobbies = models.CharField(default='',max_length=255)
    student_parent_contact = models.CharField(unique=True,max_length=10,blank=True,null=True)

    student_address = models.TextField(default='')
    student_pinCode = models.CharField(default='',max_length=6)
    student_city = models.CharField(default='',max_length=255)
    student_state = models.CharField(default='',max_length=255)

    class_fk = models.ForeignKey(class_master, verbose_name=("class_fk"), on_delete=models.CASCADE,blank=True,null=True)
    section_fk = models.ForeignKey(section_master, verbose_name=("section_fk"), on_delete=models.CASCADE,blank=True,null=True)
    # subject_fk = models.ManyToManyField(subject_master, verbose_name=("subject_fk"))
    subject_fk = models.TextField(default='[]')


    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)



# ######################################################################################################################################
# ######################################################################################################################################
'''student's Models'''
# ######################################################################################################################################
# student-user model
class parent_user(models.Model):
    student_fk = models.OneToOneField(student_profile, verbose_name=("student_fk"), on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=255)
    parent_contact = models.CharField(unique=True,max_length=10)
    parent_password = models.CharField(max_length=255)
    status_CHOICES = (
        ('1', 'Active'),
        ('2', 'Inactive'),
        ('3', 'On-hold'),
    )
    active_status = models.CharField(max_length=1, choices=status_CHOICES,default='1')

    created_at  = models.DateTimeField(auto_now_add=True)
    last_updated_at  = models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(default='superAdmin',max_length=200)
    last_updated_by = models.CharField(blank=True,null=True,max_length=200)




