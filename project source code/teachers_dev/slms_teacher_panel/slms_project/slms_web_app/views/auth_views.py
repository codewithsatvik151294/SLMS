from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models.manage_models import Teacher_user, branch, director_profile,principal_profile,schoolAdmin_profile,Teacher_profile,student_profile,class_master
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
            if(request.session['userType'] == 'super_teacher_login'):
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        else:
            return render(request,'admin_template/auth/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if(user.is_superuser):
                request.session['userType'] = 'super_teacher_login'
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



# authencicating admin users
def authenticate_user(email_id='', pwd=''):
    if(email_id != '' and pwd != ''):
        try:
            if(Teacher_user.objects.get(teacher_email = email_id)):
                saved_pwd = bytes(Teacher_user.objects.get(teacher_email = email_id).teacher_password.split("'")[1], 'utf-8')
                generate_pwd = decrypt(saved_pwd,key_data)
                if (str(pwd).strip() == str(generate_pwd.decode("utf-8") ).strip()):
                    return Teacher_user.objects.get(teacher_email = email_id)
                else:
                    return None
            else:
                return None
        except:
            return None
    else:
        return None



def teacher_login(request):
    if request.method == 'GET':
        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                return redirect('dashboard')

            if(request.session['userType'] == 'class_teacher_login'):
                return redirect('dashboard')
        else:
            return render(request,'admin_template/auth/teacher-login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate_user(email_id=username, pwd=password)
        if user is not None:
            if(Teacher_profile.objects.get(teacher_FK = user).teacher_FK.class_teacher_status == '1'):
                request.session['userType'] = 'teacher_login'
                request.session['teacher_id'] = str(Teacher_profile.objects.get(teacher_FK = user).id)
                request.session['user_name'] = str(user.teacher_name)
            if(Teacher_profile.objects.get(teacher_FK = user).teacher_FK.class_teacher_status == '2'):
                request.session['userType'] = 'class_teacher_login'
                request.session['teacher_id'] = str(Teacher_profile.objects.get(teacher_FK = user).id)
                request.session['user_name'] = str(user.teacher_name)

            return redirect('dashboard')
        
        else:
            messages.success(request,'Invalid credentials')
            return redirect('teacher_login')
        
    else:
        return HttpResponse(request,'Invalid Request Method.allowed method "GET/POST"')

# #####################################################################################################################
# logout view
# #####################################################################################################################
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('teacher_login')

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
def teacher_profile(request):
    return render(request,'admin_template/auth/admin-profile.html')

# #####################################################################################################################
# dashboard view
# #####################################################################################################################
# @login_required(login_url='/')
def dashboard(request):
    if 'userType' not in request.session:
        return redirect('logout')
    auth_dict = get_auth_dict(request,request.session['userType'])
    sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

    print('auth_dict >>> ',auth_dict)
    print('sub_auth_dict >>> ',sub_auth_dict)


    if 'userType' in request.session:
        if(request.session['userType'] == 'teacher_login'):
            context = {}
            teacherObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
            branchObj = branch.objects.get(id=int(teacherObj.branch_FK.id))
            context['studentCount'] = len(student_profile.objects.filter(branch_FK = branchObj))
            context['auth_dict'] = auth_dict
            context['sub_auth_dict'] = sub_auth_dict

            return render(request,'admin_template/dashboard/dashboard.html',context)

        if(request.session['userType'] == 'class_teacher_login'):
            context = {}
            teacherObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
            branchObj = branch.objects.get(id=int(teacherObj.branch_FK.id))
            context['studentCount'] = len(student_profile.objects.filter(branch_FK = branchObj))
            context['auth_dict'] = auth_dict
            context['sub_auth_dict'] = sub_auth_dict

            return render(request,'admin_template/dashboard/dashboard.html',context)
        
        else:
            redirect('teacher_login')
    else:
        redirect('teacher_login')
