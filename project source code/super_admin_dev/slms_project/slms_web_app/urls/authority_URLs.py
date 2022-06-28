from django.urls import path
from ..views.authority_views.authority_views import *

urlpatterns = [
    # manage authority URLS
    path('authority-list', authority_list,name='authority_list'),
    path('add-authority', add_new_authority,name='add_new_authority'),
    path('authority-detail/<int:id>', authority_detail,name='authority_detail'),
    path('edit-authority/<int:id>', edit_authority,name='edit_authority'),
    path('delete-authority/<int:id>', delete_authority,name='delete_authority'),

    path('check-designation',check_designation,name="check_designation"),
]