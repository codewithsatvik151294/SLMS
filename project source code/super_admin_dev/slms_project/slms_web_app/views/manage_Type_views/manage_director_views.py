from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.manage_models import branch,director_profile,director_user
from django.contrib.auth.hashers import check_password,make_password
from cryptography.fernet import Fernet
key_data = b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)
# #####################################################################################################################
# branch_list view
# #####################################################################################################################
@login_required(login_url='/')
def director_list(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        director_profile_obj = director_profile.objects.all().order_by('-id')
        return render(request,'admin_template/manage-type/director/director.html',{'branchObj':branchObj,'director_profile_obj':director_profile_obj})

# #####################################################################################################################
# add new director view
# #####################################################################################################################
@login_required(login_url='/')
def add_new_director(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        return render(request,'admin_template/manage-type/director/add-director.html',{'branchObj':branchObj})

    if request.method == 'POST':
        message = 'success'
        directorName = request.POST.get('director_name')
        directorDob = request.POST.get('director_dob')
        if(len(str(directorDob)) != 0):
            import datetime
            directorDob = datetime.datetime.strptime(str(directorDob), '%m-%d-%Y').strftime('%Y-%m-%d')
        else:
            directorDob = None
        directorGender = request.POST.get('director_gender')
        directorFathers_name = request.POST.get('director_fathers_name')
        directorEmail = request.POST.get('director_email')
        directorContact = request.POST.get('director_contact')
        directorAddress = request.POST.get('director_address')
        branchPinCode = request.POST.get('branchPinCode')
        directorCity = request.POST.get('directorCity')
        directorState = request.POST.get('director_state')
        branchCode = request.POST.get('branchCode')
        profileImage = request.FILES.get('profile_image')

        try:
            pwd_str = encrypt(b'123456',key_data)

            director_user_obj = director_user(director_name = directorName,
                                    director_email = directorEmail,
                                    director_contact = directorContact,
                                    director_password = pwd_str,
                                    profile_image = profileImage)
            director_user_obj.save()
            branchObj = branch.objects.get(id = int(branchCode))
            director_profile_obj = director_profile(director_FK = director_user_obj,
                                                    branch_FK = branchObj,
                                                    director_DOB = directorDob,
                                                    director_gender = directorGender,
                                                    director_fathers_name = directorFathers_name,
                                                    director_address = directorAddress,
                                                    director_pinCode = branchPinCode,
                                                    director_city = directorCity,
                                                    director_state = directorState)
            director_profile_obj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# upload director list view
# #####################################################################################################################
@login_required(login_url='/')
def upload_director_list(request):
    if request.method == 'GET':
        return render(request,'admin_template/manage-type/director/upload-director-list.html')

# #####################################################################################################################
# director details view
# #####################################################################################################################
@login_required(login_url='/')
def director_detail(request,id):
    if request.method == 'GET':
        director_profile_obj = director_profile.objects.get(id=int(id))
        return render(request,'admin_template/manage-type/director/director-details.html',{'director_profile_obj':director_profile_obj})

# #####################################################################################################################
# director edit view
# #####################################################################################################################
@login_required(login_url='/')
def edit_director(request,id):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        director_profile_obj = director_profile.objects.get(id=int(id))
        return render(request,'admin_template/manage-type/director/edit-director-details.html',{'branchObj':branchObj,'director_profile_obj':director_profile_obj})

    if request.method == 'POST':
        message = 'success'
        directorName = request.POST.get('director_name')
        directorDob = request.POST.get('director_dob')
        if(len(str(directorDob)) != 0):
            import datetime
            directorDob = datetime.datetime.strptime(str(directorDob), '%m-%d-%Y').strftime('%Y-%m-%d')
        else:
            directorDob = None
        directorGender = request.POST.get('director_gender')
        directorFathers_name = request.POST.get('director_fathers_name')
        directorEmail = request.POST.get('director_email')
        directorContact = request.POST.get('director_contact')
        directorAddress = request.POST.get('director_address')
        branchPinCode = request.POST.get('branchPinCode')
        directorCity = request.POST.get('directorCity')
        directorState = request.POST.get('director_state')
        branchCode = request.POST.get('branchCode')
        profileImage = request.FILES.get('profile_image')

        print('profileImage >>> ',profileImage)

        try:
            director_profile_obj = director_profile.objects.get(id=int(id))

            director_user_obj = director_user.objects.get(id=int(director_profile_obj.director_FK.id))
            director_user_obj.director_name = directorName
            director_user_obj.director_email = directorEmail
            director_user_obj.director_contact = directorContact
            # director_user_obj.director_password = '123456'
            if(profileImage != None):
                print('none data')
                director_user_obj.profile_image = profileImage
            director_user_obj.save()

            branchObj = branch.objects.get(id = int(branchCode))
            
            director_profile_obj.director_FK = director_user_obj
            director_profile_obj.branch_FK = branchObj
            director_profile_obj.director_DOB = directorDob
            director_profile_obj.director_gender = directorGender
            director_profile_obj.director_fathers_name = directorFathers_name
            director_profile_obj.director_address = directorAddress
            director_profile_obj.director_pinCode = branchPinCode
            director_profile_obj.director_city = directorCity
            director_profile_obj.director_state = directorState
            director_profile_obj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def delete_director(request,id):
    if request.method == 'GET':
        director_profileObj = director_profile.objects.get(id=int(id))
        director_userObj = director_user.objects.get(id=int(director_profileObj.director_FK.id))
        director_userObj.delete()
        return redirect('director_list')


# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def change_director_status(request):
    if request.method == 'POST':
        message = 'success'
        directorId = request.POST['directorId']
        data = request.POST['data']

        if(data == 'true'):
            data = '1'
        if(data == 'false'):
            data = '2'

        try:
            director_profileObj = director_profile.objects.get(id=int(directorId))
            director_userObj = director_user.objects.get(id=int(director_profileObj.director_FK.id))

            director_userObj.active_status = data
            director_userObj.save()

        except:
            message = 'failed'
        return JsonResponse({'message':message})

# #####################################################################################################################
# check branch for existing director view
# #####################################################################################################################
@login_required(login_url='/')
def director_checkBranch(request):
    if request.method == 'GET':
        message = 'not-exist'
        searchStr = request.GET['branchCode']
        branchObj = branch.objects.get(id = int(searchStr))
        try:
            if(director_profile.objects.filter(branch_FK = branchObj)):
                message = 'director-branch-exist'
        except:
            message = 'not-exist'
        return JsonResponse({'message':message})


# #####################################################################################################################
# director fields check view
# #####################################################################################################################
@login_required(login_url='/')
def director_field_check(request):
    if request.method == 'GET':
        message = 'not-exist'
        fieldType = request.GET['fieldType']
        searchString = request.GET['searchString']

        if(fieldType == 'director_email'):
            directorObj = director_user.objects.filter(director_email=searchString)
            if(directorObj):
                message = 'director-email-exist'

        elif(fieldType == 'director_contact'):
            directorObj = director_user.objects.filter(director_contact=searchString)
            if(directorObj):
                message = 'director-contact-exist'

        return JsonResponse({'message':message})