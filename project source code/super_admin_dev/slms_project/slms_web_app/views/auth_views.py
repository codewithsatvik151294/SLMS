from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models.manage_models import branch, director_profile,principal_profile,schoolAdmin_profile,Teacher_profile,student_profile,class_master
from ..models.manage_models import director_user,principal_user,schoolAdmin_user
from ..models.auth_models import super_admin_profile
import json
from cryptography.fernet import Fernet
key_data = b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

from .utils_views import get_auth_dict,get_Subauth_dict

# #####################################################################################################################
# login view
# #####################################################################################################################
def user_login(request):
    if request.method == 'GET':
        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                return redirect('dashboard')
            else:
                return render(request,'admin_template/auth/login.html')
        else:
            return render(request,'admin_template/auth/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if(user.is_superuser):
                request.session['userType'] = 'super_admin_login'
                if(super_admin_profile.objects.get(user_fk = user)):
                    request.session['contact'] = str(super_admin_profile.objects.get(user_fk = user).super_admin_contact)
                    request.session['gender'] = str(super_admin_profile.objects.get(user_fk = user).super_admin_gender)
                    request.session['image'] = str(super_admin_profile.objects.get(user_fk = user).super_admin_profile_image)

            return redirect('dashboard')
        else:
            messages.success(request,'Invalid credentials')
            return redirect('login')
        
    else:
        return HttpResponse(request,'Invalid Request Method.allowed method "GET/POST"')


# #####################################################################################################################
# logout view
# #####################################################################################################################
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')

# #####################################################################################################################
# password_reset view
# #####################################################################################################################
def password_reset(request):
    return render(request,'admin_template/auth/recover-password.html')

# #####################################################################################################################
# restricted_access view
# #####################################################################################################################
def restricted_access(request):
    if request.method == 'GET':
        return render(request,'403.html')


# #####################################################################################################################
# admin_profile view
# #####################################################################################################################
def admin_profile(request):
    return render(request,'admin_template/auth/admin-profile.html')

# #####################################################################################################################
# dashboard view
# #####################################################################################################################
@login_required(login_url='/')
def dashboard(request):
    if 'userType' in request.session:
        if(request.session['userType'] == 'super_admin_login'):
            context = {}
            context['branchCount'] = len(branch.objects.all())
            context['directorCount'] = len(director_profile.objects.all())
            context['principalCount'] = len(principal_profile.objects.all())
            context['schoolAdminCount'] = len(schoolAdmin_profile.objects.all())
            context['teacherCount'] = len(Teacher_profile.objects.all())
            context['studentCount'] = len(student_profile.objects.all())
            context['classCount'] = len(class_master.objects.all())

            return render(request,'admin_template/dashboard/dashboard.html',context)
        
        else:
            redirect('login')
    else:
        redirect('login')




def my_custom_page_not_found_view(request,exception):
    return render(request,'404.html')


def my_custom_error_view(request):
    return render(request,'500.html')