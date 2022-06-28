from django.urls import path
from ..views.assignmen_views.assignmen_views import *

urlpatterns = [
    # manage assignment URLS
    path('assignment-list', assignment_list,name='assignment_list'),
    path('add-assignment', add_assignment,name='add_assignment'),
    # path('view-assignment/<int:id>', view_paper,name='view_paper'),
    # path('edit-assignment/<int:id>', edit_paper,name='edit_paper'),
    path('delete-assignment/<int:id>', delete_assignment,name='delete_assignment'),

    path('fetch-questions', fetch_questions,name='fetch_questions'),
    path('check-assignment',check_assignment,name="check_assignment"),

    path('assignment-status-change/<int:id>',assignment_status_change,name='assignment_status_change'),
]