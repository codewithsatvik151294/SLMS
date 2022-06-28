from django.urls import path
from ..views.time_table_views.time_table_views import *

urlpatterns = [
    # time table URLS
    path('add-time-table', add_time_table,name='add_time_table'),
    path('view-time-table', view_time_table,name='view_time_table'),
    # path('paper-approval-list', paper_approval_list,name='paper_approval_list'),
    path('filter-time-table', filter_time_table,name='filter_time_table'),
    path('get-teacher', get_teacher,name='get_teacher'),

    # path('fetch-exam',fetch_exam,name="fetch_exam"),
    # path('approve_exam/<int:id>',approve_exam,name="approve_exam"),
    # path('reject_exam/<int:id>',reject_exam,name="reject_exam"),


]