from django.urls import path
from ..views.approval_views.approval_views import *

urlpatterns = [
    # badge URLS
    path('exam-approval-list', exam_approval_list,name='exam_approval_list'),
    path('paper-approval-list', paper_approval_list,name='paper_approval_list'),
    path('assignment-approval-list', assignment_approval_list,name='assignment_approval_list'),
    path('study-material-approval-list', study_material_approval_list,name='study_material_approval_list'),

    path('fetch-exam',fetch_exam,name="fetch_exam"),
    path('approve_exam/<int:id>',approve_exam,name="approve_exam"),
    path('reject_exam/<int:id>',reject_exam,name="reject_exam"),


]