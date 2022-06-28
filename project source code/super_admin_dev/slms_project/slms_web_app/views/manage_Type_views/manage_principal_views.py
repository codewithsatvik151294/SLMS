from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.manage_models import branch,principal_profile,principal_user
from django.contrib.auth.hashers import check_password,make_password
from cryptography.fernet import Fernet
key_data = b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)
# #####################################################################################################################
# principal view
# #####################################################################################################################
@login_required(login_url='/')
def principal_list(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        principal_profile_obj = principal_profile.objects.all().order_by('-id')
        return render(request,'admin_template/manage-type/principal/principle.html',{'branchObj':branchObj,'principal_profile_obj':principal_profile_obj})

# #####################################################################################################################
# add new principal view
# #####################################################################################################################
@login_required(login_url='/')
def add_new_principal(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        return render(request,'admin_template/manage-type/principal/add-principle.html',{'branchObj':branchObj})

    if request.method == 'POST':
        message = 'success'
        principalName = request.POST.get('principal_name')
        principalDob = request.POST.get('principal_dob')
        if(len(str(principalDob)) != 0):
            import datetime
            principalDob = datetime.datetime.strptime(str(principalDob), '%m-%d-%Y').strftime('%Y-%m-%d')
        else:
            principalDob = None
        principalGender = request.POST.get('principal_gender')
        principalFathers_name = request.POST.get('principal_fathers_name')
        principalEmail = request.POST.get('principal_email')
        principalContact = request.POST.get('principal_contact')
        principalAddress = request.POST.get('principal_address')
        branchPinCode = request.POST.get('branchPinCode')
        principalCity = request.POST.get('principalCity')
        principalState = request.POST.get('principal_state')
        branchCode = request.POST.get('branchCode')
        profileImage = request.FILES.get('profile_image')

        try:
            pwd_str = encrypt(b'123456',key_data)
            principal_user_obj = principal_user(principal_name = principalName,
                                    principal_email = principalEmail,
                                    principal_contact = principalContact,
                                    principal_password = pwd_str,
                                    profile_image = profileImage)
            principal_user_obj.save()
            branchObj = branch.objects.get(id = int(branchCode))
            principal_profile_obj = principal_profile(principal_FK = principal_user_obj,
                                                    branch_FK = branchObj,
                                                    principal_DOB = principalDob,
                                                    principal_gender = principalGender,
                                                    principal_fathers_name = principalFathers_name,
                                                    principal_address = principalAddress,
                                                    principal_pinCode = branchPinCode,
                                                    principal_city = principalCity,
                                                    principal_state = principalState)
            principal_profile_obj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# upload principal list view
# #####################################################################################################################
@login_required(login_url='/')
def upload_principal_list(request):
    if request.method == 'GET':
        return render(request,'admin_template/manage-type/principal/upload-principle-list.html')

# #####################################################################################################################
# principal details view
# #####################################################################################################################
@login_required(login_url='/')
def principal_detail(request,id):
    if request.method == 'GET':
        principal_profile_obj = principal_profile.objects.get(id=int(id))
        return render(request,'admin_template/manage-type/principal/principle-details.html',{'principal_profile_obj':principal_profile_obj})

# #####################################################################################################################
# principal edit view
# #####################################################################################################################
@login_required(login_url='/')
def edit_principal(request,id):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        principal_profile_obj = principal_profile.objects.get(id=int(id))
        return render(request,'admin_template/manage-type/principal/edit-principle-details.html',{'branchObj':branchObj,'principal_profile_obj':principal_profile_obj})

    if request.method == 'POST':
        message = 'success'
        principalName = request.POST.get('principal_name')
        principalDob = request.POST.get('principal_dob')
        if(len(str(principalDob)) != 0):
            import datetime
            principalDob = datetime.datetime.strptime(str(principalDob), '%m-%d-%Y').strftime('%Y-%m-%d')
        else:
            principalDob = None
        principalGender = request.POST.get('principal_gender')
        principalFathers_name = request.POST.get('principal_fathers_name')
        principalEmail = request.POST.get('principal_email')
        principalContact = request.POST.get('principal_contact')
        principalAddress = request.POST.get('principal_address')
        branchPinCode = request.POST.get('branchPinCode')
        principalCity = request.POST.get('principalCity')
        principalState = request.POST.get('principal_state')
        branchCode = request.POST.get('branchCode')
        profileImage = request.FILES.get('profile_image')

        print('profileImage >>> ',profileImage)

        try:
            principal_profile_obj = principal_profile.objects.get(id=int(id))

            principal_user_obj = principal_user.objects.get(id=int(principal_profile_obj.principal_FK.id))
            principal_user_obj.principal_name = principalName
            principal_user_obj.principal_email = principalEmail
            principal_user_obj.principal_contact = principalContact
            # principal_user_obj.principal_password = '123456'
            if(profileImage != None):
                print('none data')
                principal_user_obj.profile_image = profileImage
            principal_user_obj.save()

            branchObj = branch.objects.get(id = int(branchCode))
            
            principal_profile_obj.principal_FK = principal_user_obj
            principal_profile_obj.branch_FK = branchObj
            principal_profile_obj.principal_DOB = principalDob
            principal_profile_obj.principal_gender = principalGender
            principal_profile_obj.principal_fathers_name = principalFathers_name
            principal_profile_obj.principal_address = principalAddress
            principal_profile_obj.principal_pinCode = branchPinCode
            principal_profile_obj.principal_city = principalCity
            principal_profile_obj.principal_state = principalState
            principal_profile_obj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def delete_principal(request,id):
    if request.method == 'GET':
        principal_profileObj = principal_profile.objects.get(id=int(id))
        principal_userObj = principal_user.objects.get(id=int(principal_profileObj.principal_FK.id))
        principal_userObj.delete()
        return redirect('principal_list')


# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def change_principal_status(request):
    if request.method == 'POST':
        message = 'success'
        principalId = request.POST['principalId']
        data = request.POST['data']

        if(data == 'true'):
            data = '1'
        if(data == 'false'):
            data = '2'

        try:
            principal_profileObj = principal_profile.objects.get(id=int(principalId))
            principal_userObj = principal_user.objects.get(id=int(principal_profileObj.principal_FK.id))

            principal_userObj.active_status = data
            principal_userObj.save()

        except:
            message = 'failed'
        return JsonResponse({'message':message})

# #####################################################################################################################
# check branch for existing principal view
# #####################################################################################################################
@login_required(login_url='/')
def principal_checkBranch(request):
    if request.method == 'GET':
        message = 'not-exist'
        searchStr = request.GET['branchCode']
        branchObj = branch.objects.get(id = int(searchStr))
        try:
            if(principal_profile.objects.filter(branch_FK = branchObj)):
                message = 'principal-branch-exist'
        except:
            message = 'not-exist'
        return JsonResponse({'message':message})


# #####################################################################################################################
# principal fields check view
# #####################################################################################################################
@login_required(login_url='/')
def principal_field_check(request):
    if request.method == 'GET':
        message = 'not-exist'
        fieldType = request.GET['fieldType']
        searchString = request.GET['searchString']

        if(fieldType == 'principal_email'):
            principalObj = principal_user.objects.filter(principal_email=searchString)
            if(principalObj):
                message = 'principal-email-exist'

        elif(fieldType == 'principal_contact'):
            principalObj = principal_user.objects.filter(principal_contact=searchString)
            if(principalObj):
                message = 'principal-contact-exist'

        return JsonResponse({'message':message})