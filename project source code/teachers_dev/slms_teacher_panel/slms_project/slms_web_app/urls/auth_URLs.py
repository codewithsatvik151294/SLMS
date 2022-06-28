from django.urls import path
from ..views.auth_views import *


urlpatterns = [
    path('super-admin-login', user_login,name='login'),
    path('', teacher_login,name='teacher_login'),
    # path('', user_login,name='login'),

    path('logout', user_logout,name='logout'),
    path('reset-password', password_reset,name='password_reset'),
    path('dashboard', dashboard,name='dashboard'),
    path('teacher-profile',teacher_profile,name='teacher_profile'),
]

