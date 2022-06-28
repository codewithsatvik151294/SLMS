from django.urls import path
from ..views.question_bank_view.question_bank_view import *

urlpatterns = [
    # manage authority URLS
    path('question-list', question_list,name='question_list'),
    path('add-question', add_question,name='add_question'),
    path('view-question/<int:id>', view_question,name='view_question'),
    path('edit-question/<int:id>', edit_question,name='edit_question'),
    path('delete-question/<int:id>', delete_question,name='delete_question'),
    path('filter-question', filter_question,name='filter_question'),

    path('fetch-topics',fetch_topics,name="fetch_topics"),
]