from django.urls import path
from ..views.auth_views import *


urlpatterns = [
    path('super-admin-login', user_login,name='login'),
    path('', admin_login,name='admin_login'),
    # path('', user_login,name='login'),

    path('logout', user_logout,name='logout'),
    path('reset-password', password_reset,name='password_reset'),
    path('dashboard', dashboard,name='dashboard'),
    path('admin-profile',admin_profile,name='admin_profile'),
]

