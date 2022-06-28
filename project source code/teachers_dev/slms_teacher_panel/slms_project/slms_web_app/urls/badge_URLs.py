from django.urls import path
from ..views.badge_views.badge_views import *

urlpatterns = [
    # badge URLS
    path('badge-list', badge_list,name='badge_list'),
    path('add-badge', add_badge,name='add_badge'),
    path('edit-badge/<int:id>', edit_badge,name='edit_badge'),
    path('delete-badge/<int:id>', delete_badge,name='delete_badge'),

    path('check-title',check_badge_title,name="check_badge_title"),
    path('check-trigger',check_badge_trigger,name="check_badge_trigger"),

]