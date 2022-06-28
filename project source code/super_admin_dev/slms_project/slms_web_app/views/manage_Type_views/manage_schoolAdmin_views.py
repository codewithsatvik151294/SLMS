from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.manage_models import branch,schoolAdmin_profile,schoolAdmin_user
from django.contrib.auth.hashers import check_password,make_password
from cryptography.fernet import Fernet
key_data = b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)
# #####################################################################################################################
# schoolAdmin view
# #####################################################################################################################
@login_required(login_url='/')
def schoolAdmin_list(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        schoolAdmin_profile_obj = schoolAdmin_profile.objects.all().order_by('-id')
        return render(request,'admin_template/manage-type/school_admin/school-admin.html',{'branchObj':branchObj,'schoolAdmin_profile_obj':schoolAdmin_profile_obj})

# #####################################################################################################################
# add new schoolAdmin view
# #####################################################################################################################
@login_required(login_url='/')
def add_new_schoolAdmin(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        return render(request,'admin_template/manage-type/school_admin/add-school-admin.html',{'branchObj':branchObj})

    if request.method == 'POST':
        message = 'success'
        schoolAdminName = request.POST.get('schoolAdmin_name')
        schoolAdminDob = request.POST.get('schoolAdmin_dob')
        if(len(str(schoolAdminDob)) != 0):
            import datetime
            schoolAdminDob = datetime.datetime.strptime(str(schoolAdminDob), '%m/%d/%Y').strftime('%Y-%m-%d')
        else:
            schoolAdminDob = None
        schoolAdminGender = request.POST.get('schoolAdmin_gender')
        schoolAdminFathers_name = request.POST.get('schoolAdmin_fathers_name')
        schoolAdminEmail = request.POST.get('schoolAdmin_email')
        schoolAdminContact = request.POST.get('schoolAdmin_contact')
        schoolAdminAddress = request.POST.get('schoolAdmin_address')
        branchPinCode = request.POST.get('branchPinCode')
        schoolAdminCity = request.POST.get('schoolAdminCity')
        schoolAdminState = request.POST.get('schoolAdmin_state')
        branchCode = request.POST.get('branchCode')
        profileImage = request.FILES.get('profile_image')

        try:
            pwd_str = encrypt(b'123456',key_data)
            schoolAdmin_user_obj = schoolAdmin_user(schoolAdmin_name = schoolAdminName,
                                    schoolAdmin_email = schoolAdminEmail,
                                    schoolAdmin_contact = schoolAdminContact,
                                    schoolAdmin_password = pwd_str,
                                    profile_image = profileImage)
            schoolAdmin_user_obj.save()
            branchObj = branch.objects.get(id = int(branchCode))
            schoolAdmin_profile_obj = schoolAdmin_profile(schoolAdmin_FK = schoolAdmin_user_obj,
                                                    branch_FK = branchObj,
                                                    schoolAdmin_DOB = schoolAdminDob,
                                                    schoolAdmin_gender = schoolAdminGender,
                                                    schoolAdmin_fathers_name = schoolAdminFathers_name,
                                                    schoolAdmin_address = schoolAdminAddress,
                                                    schoolAdmin_pinCode = branchPinCode,
                                                    schoolAdmin_city = schoolAdminCity,
                                                    schoolAdmin_state = schoolAdminState)
            schoolAdmin_profile_obj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# upload schoolAdmin list view
# #####################################################################################################################
@login_required(login_url='/')
def upload_schoolAdmin_list(request):
    if request.method == 'GET':
        return render(request,'admin_template/manage-type/school_admin/upload-school-admin-list.html')

# #####################################################################################################################
# schoolAdmin details view
# #####################################################################################################################
@login_required(login_url='/')
def schoolAdmin_detail(request,id):
    if request.method == 'GET':
        schoolAdmin_profile_obj = schoolAdmin_profile.objects.get(id=int(id))
        return render(request,'admin_template/manage-type/school_admin/school-admin-details.html',{'schoolAdmin_profile_obj':schoolAdmin_profile_obj})

# #####################################################################################################################
# schoolAdmin edit view
# #####################################################################################################################
@login_required(login_url='/')
def edit_schoolAdmin(request,id):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        schoolAdmin_profile_obj = schoolAdmin_profile.objects.get(id=int(id))
        return render(request,'admin_template/manage-type/school_admin/edit-school-admin-details.html',{'branchObj':branchObj,'schoolAdmin_profile_obj':schoolAdmin_profile_obj})

    if request.method == 'POST':
        message = 'success'
        schoolAdminName = request.POST.get('schoolAdmin_name')
        schoolAdminDob = request.POST.get('schoolAdmin_dob')
        if(len(str(schoolAdminDob)) != 0):
            import datetime
            schoolAdminDob = datetime.datetime.strptime(str(schoolAdminDob), '%m/%d/%Y').strftime('%Y-%m-%d')
        else:
            schoolAdminDob = None
        schoolAdminGender = request.POST.get('schoolAdmin_gender')
        schoolAdminFathers_name = request.POST.get('schoolAdmin_fathers_name')
        schoolAdminEmail = request.POST.get('schoolAdmin_email')
        schoolAdminContact = request.POST.get('schoolAdmin_contact')
        schoolAdminAddress = request.POST.get('schoolAdmin_address')
        branchPinCode = request.POST.get('branchPinCode')
        schoolAdminCity = request.POST.get('schoolAdminCity')
        schoolAdminState = request.POST.get('schoolAdmin_state')
        branchCode = request.POST.get('branchCode')
        profileImage = request.FILES.get('profile_image')

        print('profileImage >>> ',profileImage)

        try:
            schoolAdmin_profile_obj = schoolAdmin_profile.objects.get(id=int(id))

            schoolAdmin_user_obj = schoolAdmin_user.objects.get(id=int(schoolAdmin_profile_obj.schoolAdmin_FK.id))
            schoolAdmin_user_obj.schoolAdmin_name = schoolAdminName
            schoolAdmin_user_obj.schoolAdmin_email = schoolAdminEmail
            schoolAdmin_user_obj.schoolAdmin_contact = schoolAdminContact
            # schoolAdmin_user_obj.schoolAdmin_password = '123456'
            if(profileImage != None):
                print('none data')
                schoolAdmin_user_obj.profile_image = profileImage
            schoolAdmin_user_obj.save()

            branchObj = branch.objects.get(id = int(branchCode))
            
            schoolAdmin_profile_obj.schoolAdmin_FK = schoolAdmin_user_obj
            schoolAdmin_profile_obj.branch_FK = branchObj
            schoolAdmin_profile_obj.schoolAdmin_DOB = schoolAdminDob
            schoolAdmin_profile_obj.schoolAdmin_gender = schoolAdminGender
            schoolAdmin_profile_obj.schoolAdmin_fathers_name = schoolAdminFathers_name
            schoolAdmin_profile_obj.schoolAdmin_address = schoolAdminAddress
            schoolAdmin_profile_obj.schoolAdmin_pinCode = branchPinCode
            schoolAdmin_profile_obj.schoolAdmin_city = schoolAdminCity
            schoolAdmin_profile_obj.schoolAdmin_state = schoolAdminState
            schoolAdmin_profile_obj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def delete_schoolAdmin(request,id):
    if request.method == 'GET':
        schoolAdmin_profileObj = schoolAdmin_profile.objects.get(id=int(id))
        schoolAdmin_userObj = schoolAdmin_user.objects.get(id=int(schoolAdmin_profileObj.schoolAdmin_FK.id))
        schoolAdmin_userObj.delete()
        return redirect('schoolAdmin_list')


# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def change_schoolAdmin_status(request):
    if request.method == 'POST':
        message = 'success'
        schoolAdminId = request.POST['schoolAdminId']
        data = request.POST['data']

        if(data == 'true'):
            data = '1'
        if(data == 'false'):
            data = '2'

        try:
            schoolAdmin_profileObj = schoolAdmin_profile.objects.get(id=int(schoolAdminId))
            schoolAdmin_userObj = schoolAdmin_user.objects.get(id=int(schoolAdmin_profileObj.schoolAdmin_FK.id))

            schoolAdmin_userObj.active_status = data
            schoolAdmin_userObj.save()

        except:
            message = 'failed'
        return JsonResponse({'message':message})

# #####################################################################################################################
# check branch for existing schoolAdmin view
# #####################################################################################################################
@login_required(login_url='/')
def schoolAdmin_checkBranch(request):
    if request.method == 'GET':
        message = 'not-exist'
        searchStr = request.GET['branchCode']
        branchObj = branch.objects.get(id = int(searchStr))
        try:
            if(schoolAdmin_profile.objects.filter(branch_FK = branchObj)):
                message = 'schoolAdmin-branch-exist'
        except:
            message = 'not-exist'
        return JsonResponse({'message':message})


# #####################################################################################################################
# schoolAdmin fields check view
# #####################################################################################################################
@login_required(login_url='/')
def schoolAdmin_field_check(request):
    if request.method == 'GET':
        message = 'not-exist'
        fieldType = request.GET['fieldType']
        searchString = request.GET['searchString']

        if(fieldType == 'schoolAdmin_email'):
            schoolAdminObj = schoolAdmin_user.objects.filter(schoolAdmin_email=searchString)
            if(schoolAdminObj):
                message = 'schoolAdmin-email-exist'

        elif(fieldType == 'schoolAdmin_contact'):
            schoolAdminObj = schoolAdmin_user.objects.filter(schoolAdmin_contact=searchString)
            if(schoolAdminObj):
                message = 'schoolAdmin-contact-exist'

        return JsonResponse({'message':message})