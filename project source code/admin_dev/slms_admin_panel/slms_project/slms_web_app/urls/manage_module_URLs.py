from django.urls import path
from ..views.manage_Type_views.manage_branch_views import *
from ..views.manage_Type_views.manage_director_views import *
from ..views.manage_Type_views.manage_principal_views import *
from ..views.manage_Type_views.manage_schoolAdmin_views import *
from ..views.manage_Type_views.manage_Teacher_views import *
from ..views.manage_Type_views.manage_student_views import *

urlpatterns = [
    # manage branch URLS
    # path('branch-list', branch_list,name='branch_list'),
    # path('add-branch', add_new_branch,name='add_new_branch'),
    # path('branch-upload', upload_branch_list,name='upload_branch_list'),
    # path('branch-detail/<int:id>', branch_detail,name='branch_detail'),
    # path('edit-branch/<int:id>', edit_branch,name='edit_branch'),
    # path('delete-branch/<int:id>', delete_branch,name='delete_branch'),
    # path('add-branch-field-check', field_check,name='field_check'),


    # # manage director URLS
    # path('director-list', director_list,name='director_list'),
    # path('add-director', add_new_director,name='add_new_director'),
    # path('director-upload', upload_director_list,name='upload_director_list'),
    # path('director-detail/<int:id>', director_detail,name='director_detail'),
    # path('edit-director/<int:id>', edit_director,name='edit_director'),
    # path('director-checkBranch', director_checkBranch,name='director-checkBranch'),
    # path('add-director-field-check', director_field_check,name='director_field_check'),
    # path('delete-director/<int:id>', delete_director,name='delete_director'),
    # path('change-director-status', change_director_status,name='change_director_status'),


    # # manage principal URLS
    # path('principal-list', principal_list,name='principal_list'),
    # path('add-principal', add_new_principal,name='add_new_principal'),
    # path('principal-upload', upload_principal_list,name='upload_principal_list'),
    # path('principal-detail/<int:id>', principal_detail,name='principal_detail'),
    # path('edit-principal/<int:id>', edit_principal,name='edit_principal'),
    # path('principal-checkBranch', principal_checkBranch,name='principal-checkBranch'),
    # path('add-principal-field-check', principal_field_check,name='principal_field_check'),
    # path('delete-principal/<int:id>', delete_principal,name='delete_principal'),
    # path('change-principal-status', change_principal_status,name='change_principal_status'),


    # # manage school-admin URLS
    # path('school-admin-list', schoolAdmin_list,name='schoolAdmin_list'),
    # path('add-school-admin', add_new_schoolAdmin,name='add_new_schoolAdmin'),
    # path('school-admin-upload', upload_schoolAdmin_list,name='upload_schoolAdmin_list'),
    # path('school-admin-detail/<int:id>', schoolAdmin_detail,name='schoolAdmin_detail'),
    # path('edit-school-admin/<int:id>', edit_schoolAdmin,name='edit_schoolAdmin'),
    # path('school-admin-checkBranch', schoolAdmin_checkBranch,name='school-admin-checkBranch'),
    # path('add-school-admin-field-check', schoolAdmin_field_check,name='schoolAdmin_field_check'),
    # path('delete-school-admin/<int:id>', delete_schoolAdmin,name='delete_schoolAdmin'),
    # path('change-school-admin-status', change_schoolAdmin_status,name='change_schoolAdmin_status'),


    # manage teacher URLS
    path('teacher-list', Teacher_list,name='Teacher_list'),
    path('add-teacher', add_new_Teacher,name='add_new_Teacher'),
    path('teacher-upload', upload_Teacher_list,name='upload_Teacher_list'),
    path('teacher-detail/<int:id>', Teacher_detail,name='Teacher_detail'),
    path('edit-teacher/<int:id>', edit_Teacher,name='edit_Teacher'),
    path('teacher-checkBranch', Teacher_checkBranch,name='teacher-checkBranch'),
    path('add-teacher-field-check', Teacher_field_check,name='Teacher_field_check'),
    path('delete-teacher/<int:id>', delete_Teacher,name='delete_Teacher'),
    path('change-teacher-status', change_Teacher_status,name='change_Teacher_status'),
    path('add-teacher-get-class',add_teacher_get_class,name='add_teacher_get_class'),
    path('get-subject-and-section',get_subject_and_section,name='get_subject_and_section'),


    # manage student URLS
    path('student-list', student_list,name='student_list'),
    path('add-student', add_new_student,name='add_new_student'),
    path('student-upload', upload_student_list,name='upload_student_list'),
    path('student-detail/<int:id>', student_detail,name='student_detail'),
    path('edit-student/<int:id>', edit_student,name='edit_student'),
    path('student-checkBranch', student_checkBranch,name='student-checkBranch'),
    path('add-student-field-check', student_field_check,name='student_field_check'),
    path('delete-student/<int:id>', delete_student,name='delete_student'),
    path('change-student-status', change_student_status,name='change_student_status'),


]