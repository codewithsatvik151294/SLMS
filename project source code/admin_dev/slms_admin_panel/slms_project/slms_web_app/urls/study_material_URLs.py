from django.urls import path
from ..views.study_material_views.study_material_views import *

urlpatterns = [
    # manage assignment URLS
    path('study-material-list', study_material_list,name='study_material_list'),
    path('add-study-material', add_study_material,name='add_study_material'),
    path('view-study-material/<int:id>', view_study_material,name='view_study_material'),
    path('edit-study-material/<int:id>', edit_study_material,name='edit_study_material'),
    path('delete-study_material/<int:id>', delete_study_material,name='delete_study_material'),

    path('fetch-questions', fetch_questions,name='fetch_questions'),
    path('check-assignment',check_assignment,name="check_assignment"),

    path('study-material-status-change/<int:id>',study_material_status_change,name='study_material_status_change'),
]