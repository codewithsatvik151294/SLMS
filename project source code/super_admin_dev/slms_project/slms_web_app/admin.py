from django.contrib import admin
from .models.auth_models import userType,super_admin_profile
from .models.manage_models import branch,director_user,director_profile,principal_user,principal_profile,schoolAdmin_user,schoolAdmin_profile,Teacher_profile,Teacher_user,student_profile,student_user,class_master,topic_master,parent_user
from .models.master_models import class_type_master,section_detail,section_master,subject_master,user_designation_master,Authority_master,SubAuthority_master,year_master,question_type_master,badge_trigger_master,file_type_master,exam_type_master
from .models.authority_models import assign_authority
from .models.question_management_models import question
from .models.paper_models import question_paper_model
from .models.exam_models import exam_model,exam_paper_detail
from .models.assignment_models import assignment_model
from .models.studey_material_models import study_material
from .models.badge_models import badge_management
from .models.time_table_models import time_table_model
from .models.attendance_models import attendance_model
# Register your models here.

@admin.register(userType)
class Users_Type(admin.ModelAdmin):
    list_display = ('id', 'userType','created_at','created_by','last_updated_at')

@admin.register(super_admin_profile)
class super_admin_profile(admin.ModelAdmin):
    list_display = ('id', 'user_fk','super_admin_contact','super_admin_gender')
# ==========================================================================================================================================
'''time_table models'''
# ==========================================================================================================================================
# time_table model
@admin.register(time_table_model)
class time_table_model(admin.ModelAdmin):
    list_display = ('id', 'time_table_ID','time_table_session','time_table_effective_from','year_fk','branch_fk','class_fk','section_fk','time_table_active_status','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''attendance_model models'''
# ==========================================================================================================================================
# attendance_model model
@admin.register(attendance_model)
class attendance_model(admin.ModelAdmin):
    list_display = ('id', 'attendance_ID','attendance_session','student_fk','branch_fk','class_fk','section_fk','attendance_status','attendance_date','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''question models'''
# ==========================================================================================================================================
# question model
@admin.register(question)
class question(admin.ModelAdmin):
    list_display = ('id', 'question_ID','class_fk','subject_fk','year_fk','topic_name','question_text','correct_mark','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''question_paper_model models'''
# ==========================================================================================================================================
# question_paper_model model
@admin.register(question_paper_model)
class question_paper_model(admin.ModelAdmin):
    list_display = ('id', 'paper_ID','class_fk','subject_fk','year_fk','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''assign_authority models'''
# ==========================================================================================================================================
# assign_authority model
@admin.register(assign_authority)
class assign_authorities(admin.ModelAdmin):
    list_display = ('id', 'assign_authorityID','designation_fk','authority_fk','sub_authority_fk','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''Branch models'''
# ==========================================================================================================================================
# branch model
@admin.register(branch)
class Branches(admin.ModelAdmin):
    list_display = ('id', 'branch_code','branch_name','branch_email','branch_contact','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''Directors models'''
# ==========================================================================================================================================
# director-user model
@admin.register(director_user)
class director_user(admin.ModelAdmin):
    list_display = ('id', 'director_name','director_email','director_contact','director_password','active_status','created_at','created_by','last_updated_at')

# director-profile model
@admin.register(director_profile)
class director_profile(admin.ModelAdmin):
    list_display = ('id', 'director_FK','branch_FK','director_DOB','director_gender','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''Principal models'''
# ==========================================================================================================================================
# principal-user model
@admin.register(principal_user)
class principal_user(admin.ModelAdmin):
    list_display = ('id', 'principal_name','principal_email','principal_contact','principal_password','active_status','created_at','created_by','last_updated_at')

# principal-profile model
@admin.register(principal_profile)
class principal_profile(admin.ModelAdmin):
    list_display = ('id', 'principal_FK','branch_FK','principal_DOB','principal_gender','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''schoolAdmin models'''
# ==========================================================================================================================================
# schoolAdmin-user model
@admin.register(schoolAdmin_user)
class schoolAdmin_user(admin.ModelAdmin):
    list_display = ('id', 'schoolAdmin_name','schoolAdmin_email','schoolAdmin_contact','schoolAdmin_password','active_status','created_at','created_by','last_updated_at')

# schoolAdmin-profile model
@admin.register(schoolAdmin_profile)
class schoolAdmin_profile(admin.ModelAdmin):
    list_display = ('id', 'schoolAdmin_FK','branch_FK','schoolAdmin_DOB','schoolAdmin_gender','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''teacher models'''
# ==========================================================================================================================================
# teacher-user model
@admin.register(Teacher_user)
class teacher_user(admin.ModelAdmin):
    list_display = ('id', 'teacher_name','teacher_email','teacher_contact','teacher_password','active_status','class_teacher_status','created_at','created_by','last_updated_at')

# teacher-profile model
@admin.register(Teacher_profile)
class teacher_profile(admin.ModelAdmin):
    list_display = ('id', 'teacher_FK','branch_FK','teacher_DOB','teacher_gender','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''student models'''
# ==========================================================================================================================================
# student-user model
@admin.register(student_user)
class student_user(admin.ModelAdmin):
    list_display = ('id', 'student_first_name','student_email','student_contact','student_password','active_status','created_at','created_by','last_updated_at')

# student-profile model
@admin.register(student_profile)
class student_profile(admin.ModelAdmin):
    list_display = ('id', 'student_FK','branch_FK','student_DOB','student_gender','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''parent models'''
# ==========================================================================================================================================
# parent-user model
@admin.register(parent_user)
class parent_user(admin.ModelAdmin):
    list_display = ('id', 'parent_name','parent_contact','parent_password','active_status','created_at','created_by','last_updated_at')
# ==========================================================================================================================================
'''MASTER models'''
# ==========================================================================================================================================
# class_type_master model
@admin.register(class_type_master)
class class_type_master(admin.ModelAdmin):
    list_display = ('id', 'classTypeID','classType_name','class_subType_name','created_at','created_by','last_updated_at')

# topic_master model
@admin.register(topic_master)
class topic_master(admin.ModelAdmin):
    list_display = ('id', 'topicID','class_FK','subject_FK','topic_name','created_at','created_by','last_updated_at')

# class_master model
@admin.register(class_master)
class class_master(admin.ModelAdmin):
    list_display = ('id', 'classID','class_name','created_at','created_by','last_updated_at')

# subject_master model
@admin.register(subject_master)
class subject_master(admin.ModelAdmin):
    list_display = ('id', 'subjectID','subject_name','created_at','created_by','last_updated_at')

# section_master model
@admin.register(section_master)
class section_master(admin.ModelAdmin):
    list_display = ('id', 'sectionID','section_name','created_at','created_by','last_updated_at')

# section_detail model
@admin.register(section_detail)
class section_detail(admin.ModelAdmin):
    list_display = ('id', 'section_fk','classType_fk','created_at','created_by','last_updated_at')


# user_designation_master model
@admin.register(user_designation_master)
class user_designation_master(admin.ModelAdmin):
    list_display = ('id', 'designationID','designation_name','created_at','created_by','last_updated_at')


# user_authority_master model
@admin.register(Authority_master)
class Authority_master(admin.ModelAdmin):
    list_display = ('id', 'authorityID','authority_name','created_at','created_by','last_updated_at')


# subAuthority_master model
@admin.register(SubAuthority_master)
class SubAuthority_master(admin.ModelAdmin):
    list_display = ('id','authority_FK', 'subAuthorityID','subAuthority_name','created_at','created_by','last_updated_at')

# year_master model
@admin.register(year_master)
class year_master(admin.ModelAdmin):
    list_display = ('id', 'yearID','year_name','created_at','created_by','last_updated_at')

# question_type_master model
@admin.register(question_type_master)
class question_type_master(admin.ModelAdmin):
    list_display = ('id', 'questionTypeID','questionType_name','created_at','created_by','last_updated_at')

# badge_trigger_master model
@admin.register(badge_trigger_master)
class badge_trigger_master(admin.ModelAdmin):
    list_display = ('id', 'badge_triggerID','badge_trigger_name','created_at','created_by','last_updated_at')

# file_type_master model
@admin.register(file_type_master)
class file_type_master(admin.ModelAdmin):
    list_display = ('id', 'file_typeID','file_type_name','created_at','created_by','last_updated_at')

# exam_type_master model
@admin.register(exam_type_master)
class exam_type_master(admin.ModelAdmin):
    list_display = ('id', 'exam_typeID','exam_type_name','created_at','created_by','last_updated_at')



# ==========================================================================================================================================
'''Exam models'''
# ==========================================================================================================================================
#exam model
@admin.register(exam_model)
class exam_model(admin.ModelAdmin):
    list_display = ('id', 'exam_ID','exam_name','class_fk','created_at','created_by','last_updated_at')

#paper details model
@admin.register(exam_paper_detail)
class exam_paper_detail(admin.ModelAdmin):
    list_display = ('id', 'exam_fk','paper_fk','exam_start_date_time','exam_end_date_time','proctor_fk','created_at','created_by','last_updated_at')


# ==========================================================================================================================================
'''Assignment models'''
# ==========================================================================================================================================
#Assignment model
@admin.register(assignment_model)
class assignment_model(admin.ModelAdmin):
    list_display = ('id', 'assignment_ID','assignment_name','branch_FK','class_fk','question_array','created_at','created_by','last_updated_at')


# ==========================================================================================================================================
'''study material models'''
# ==========================================================================================================================================
#study material model
@admin.register(study_material)
class study_material(admin.ModelAdmin):
    list_display = ('id', 'study_material_ID','class_fk','branch_fk','subject_fk','topic','file_type_fk','published_status','created_at','created_by','last_updated_at')


# ==========================================================================================================================================
'''badge_management models'''
# ==========================================================================================================================================
#badge_management model
@admin.register(badge_management)
class badge_management(admin.ModelAdmin):
    list_display = ('id', 'badge_ID','badge_title','badge_trigger_fk','badge_desrciption','created_at','created_by','last_updated_at')

