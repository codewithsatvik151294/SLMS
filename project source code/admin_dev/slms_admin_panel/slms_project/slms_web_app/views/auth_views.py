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
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login' or request.session['admin_userType'] == 'school_admin_login' or request.session['admin_userType'] == 'principal_login'):
                return redirect('admin_login')
            else:
                return redirect('admin_login')
        else:
            return redirect('admin_login')

    if request.method == 'POST':
        return redirect('admin_login')
    else:
        return HttpResponse(request,'Invalid Request Method.allowed method "GET/POST"')



# authencicating admin users
def authenticate_user(email_id='', pwd='',admin_userType=''):
    print('admin_userType >>> ',admin_userType,type(admin_userType))
    if(email_id != '' and pwd != '' and admin_userType != ''):
        try:
            try:
                if(admin_userType == '1'):
                    if(director_user.objects.get(director_email = email_id)):
                        saved_pwd = bytes(director_user.objects.get(director_email = email_id).director_password.split("'")[1], 'utf-8')
                        generate_pwd = decrypt(saved_pwd,key_data)
                        if (str(pwd).strip() == str(generate_pwd.decode("utf-8") ).strip()):
                            return director_user.objects.get(director_email = email_id)
                        else:
                            return None
                    else:
                        return None
                if(admin_userType == '2'):
                    if(schoolAdmin_user.objects.get(schoolAdmin_email = email_id)):
                        saved_pwd = bytes(schoolAdmin_user.objects.get(schoolAdmin_email = email_id).schoolAdmin_password.split("'")[1], 'utf-8')
                        generate_pwd = decrypt(saved_pwd,key_data)
                        if (str(pwd).strip() == str(generate_pwd.decode("utf-8") ).strip()):
                            return schoolAdmin_user.objects.get(schoolAdmin_email = email_id)
                        else:
                            return None
                    else:
                        return None
                if(admin_userType == '3'):
                    if(principal_user.objects.get(principal_email = email_id)):
                        saved_pwd = bytes(principal_user.objects.get(principal_email = email_id).principal_password.split("'")[1], 'utf-8')
                        generate_pwd = decrypt(saved_pwd,key_data)
                        if (str(pwd).strip() == str(generate_pwd.decode("utf-8") ).strip()):
                            return principal_user.objects.get(principal_email = email_id)
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            except:
                return None
        except:
            return None
    else:
        return None


def admin_login(request):
    if request.method == 'GET':
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login' or request.session['admin_userType'] == 'school_admin_login' or request.session['admin_userType'] == 'principal_login'):
                return redirect('dashboard')
            else:
                return render(request,'admin_template/auth/admins-login.html')
        else:
            return render(request,'admin_template/auth/admins-login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user-type']

        user = authenticate_user(email_id=username, pwd=password, admin_userType=user_type)
        if user is not None:
            if(user_type == '1'):
                request.session['admin_userType'] = 'director_login'
                request.session['director_id'] = str(director_profile.objects.get(director_FK = user).id)
                request.session['user_name'] = str(user.director_name)
            if(user_type == '2'):
                request.session['admin_userType'] = 'school_admin_login'
                request.session['school_admin_id'] = str(schoolAdmin_profile.objects.get(schoolAdmin_FK = user).id)
                request.session['user_name'] = str(user.schoolAdmin_name)
            if(user_type == '3'):
                request.session['admin_userType'] = 'principal_login'
                request.session['principal_id'] = str(principal_profile.objects.get(principal_FK = user).id)
                request.session['user_name'] = str(user.principal_name)
            return redirect('dashboard')
        
        else:
            messages.success(request,'Invalid credentials or user Type')
            return redirect('admin_login')
        
    else:
        return HttpResponse(request,'Invalid Request Method.allowed method "GET/POST"')

# #####################################################################################################################
# logout view
# #####################################################################################################################
def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('admin_login')

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
# @login_required(login_url='/')
def dashboard(request):
    if 'admin_userType' in request.session:
        if(request.session['admin_userType'] == 'director_login'):
            context = {}
            auth_dict = get_auth_dict(request,request.session['admin_userType'])
            sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

            directorObj = director_profile.objects.get(id=int(request.session['director_id']))
            branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))

            context['teacherCount'] = len(Teacher_profile.objects.filter(branch_FK = branchObj))
            # context['classTeacherCount'] = len(Teacher_profile.objects.filter(branch_FK = branchObj,))
            context['studentCount'] = len(student_profile.objects.filter(branch_FK = branchObj))
            context['classCount'] = len(class_master.objects.filter(branch_FK = branchObj))
            context['auth_dict'] = auth_dict
            context['sub_auth_dict'] = sub_auth_dict

            return render(request,'admin_template/dashboard/dashboard.html',context)


        if(request.session['admin_userType'] == 'school_admin_login'):
            context = {}
            auth_dict = get_auth_dict(request,request.session['admin_userType'])
            sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
            schoolAdminObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
            branchObj = branch.objects.get(id=int(schoolAdminObj.branch_FK.id))

            context['teacherCount'] = len(Teacher_profile.objects.filter(branch_FK = branchObj))
            # context['classTeacherCount'] = len(Teacher_profile.objects.filter(branch_FK = branchObj))
            context['studentCount'] = len(student_profile.objects.filter(branch_FK = branchObj))
            context['classCount'] = len(class_master.objects.filter(branch_FK = branchObj))
            context['auth_dict'] = auth_dict
            context['sub_auth_dict'] = sub_auth_dict

            return render(request,'admin_template/dashboard/dashboard.html',context)

        if(request.session['admin_userType'] == 'principal_login'):
            context = {}
            auth_dict = get_auth_dict(request,request.session['admin_userType'])
            sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
            principalObj = principal_profile.objects.get(id=int(request.session['principal_id']))
            branchObj = branch.objects.get(id=int(principalObj.branch_FK.id))

            context['teacherCount'] = len(Teacher_profile.objects.filter(branch_FK = branchObj))
            # context['classTeacherCount'] = len(Teacher_profile.objects.filter(branch_FK = branchObj))
            context['studentCount'] = len(student_profile.objects.filter(branch_FK = branchObj))
            context['classCount'] = len(class_master.objects.filter(branch_FK = branchObj))
            context['auth_dict'] = auth_dict
            context['sub_auth_dict'] = sub_auth_dict

            return render(request,'admin_template/dashboard/dashboard.html',context)
        
        else:
            redirect('admin_login')
    else:
        redirect('admin_login')



def my_custom_page_not_found_view(request,exception):
    return render(request,'404.html')


def my_custom_error_view(request):
    return render(request,'500.html')