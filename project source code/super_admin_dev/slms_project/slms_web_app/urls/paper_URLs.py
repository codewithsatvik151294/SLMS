from django.urls import path
from ..views.paper_views.paper_views import *

urlpatterns = [
    # manage paper URLS
    path('paper-list', paper_list,name='paper_list'),
    path('add-paper', add_paper,name='add_paper'),
    # path('view-paper/<int:id>', view_paper,name='view_paper'),
    # path('edit-paper/<int:id>', edit_paper,name='edit_paper'),
    path('delete-paper/<int:id>', delete_paper,name='delete_paper'),

    path('fetch-questions', fetch_questions,name='fetch_questions'),
    path('check-paper-name',check_paper_name,name="check_paper_name"),
    path('get-questions',get_questions,name='get_questions'),
]