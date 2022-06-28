from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from slms_web_app.views.auth_views import restricted_access
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('slms_web_app.urls.auth_URLs')),
    path('manage/',include('slms_web_app.urls.manage_module_URLs')),
    # path('master/',include('slms_web_app.urls.master_URLs')),
    # path('authority-management/',include('slms_web_app.urls.authority_URLs')),
    path('question-bank-management/',include('slms_web_app.urls.question_bank_URLs')),
    path('paper-management/',include('slms_web_app.urls.paper_URLs')),
    path('exam-management/',include('slms_web_app.urls.exam_URLs')),
    path('assignment-management/',include('slms_web_app.urls.assignment_URLs')),
    path('study-material-management/',include('slms_web_app.urls.study_material_URLs')),
    path('badge-management/',include('slms_web_app.urls.badge_URLs')),

    path('restricted-access',restricted_access,name='restricted_access')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

# handler404 = 'slms_web_app.views.auth_views.my_custom_page_not_found_view'
# handler500 = 'slms_web_app.views.auth_views.my_custom_error_view'