from django.urls import path
from ..views.attendance_views.attendance_views import *

urlpatterns = [
    # attendance URLS
    path('add-attendance', add_attendance,name='add_attendance'),
    path('attendance-list', attendance_list,name='attendance_list'),


    path('filter-student', filter_student,name='filter_student'),
    path('filter-student-monthwise',filter_student_monthwise,name="filter_student_monthwise"),

    path('view-attendance/<int:id>', view_attendance,name='view_attendance'),
    path('edit-attendance/<int:id>',edit_attendance,name="edit_attendance"),
    # path('reject_exam/<int:id>',reject_exam,name="reject_exam"),


]