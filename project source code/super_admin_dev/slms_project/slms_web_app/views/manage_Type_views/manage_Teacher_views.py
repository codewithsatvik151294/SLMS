from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required

from slms_web_app.models.master_models import class_type_master, section_master, subject_master
from ...models.manage_models import branch,Teacher_profile,Teacher_user,class_master,director_profile,principal_profile,schoolAdmin_profile
from cryptography.fernet import Fernet
key_data = b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

from ..utils_views import get_auth_dict,get_Subauth_dict
import datetime
# #####################################################################################################################
# branch_list view
# #####################################################################################################################
@login_required(login_url='/')
def Teacher_list(request):
    if request.method == 'GET':
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                branchObj = branch.objects.all().order_by('-id')
                Teacher_profile_obj = Teacher_profile.objects.all().order_by('-id')
                return render(request,'admin_template/manage-type/teacher/teacher.html',{'branchObj':branchObj,'Teacher_profile_obj':Teacher_profile_obj})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    Teacher_profile_obj = Teacher_profile.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/teacher/teacher.html',{'Teacher_profile_obj':Teacher_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    Teacher_profile_obj = Teacher_profile.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/teacher/teacher.html',{'Teacher_profile_obj':Teacher_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    Teacher_profile_obj = Teacher_profile.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/teacher/teacher.html',{'Teacher_profile_obj':Teacher_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')

# #####################################################################################################################
# add new Teacher view
# #####################################################################################################################
@login_required(login_url='/')
def add_new_Teacher(request):
    if request.method == 'GET':
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                branchObj = branch.objects.all().order_by('-id')
                classObj = class_master.objects.all().order_by('-id')
                return render(request,'admin_template/manage-type/teacher/add-teacher.html',{'branchObj':branchObj,'classObj':classObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.filter(branch_name=directorObj.branch_FK.branch_name)
                    classObj = class_master.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/teacher/add-teacher.html',{'branchObj':branchObj,'classObj':classObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.filter(branch_name=directorObj.branch_FK.branch_name)
                    classObj = class_master.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/teacher/add-teacher.html',{'branchObj':branchObj,'classObj':classObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.filter(branch_name=directorObj.branch_FK.branch_name)
                    classObj = class_master.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/teacher/add-teacher.html',{'branchObj':branchObj,'classObj':classObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')


    if request.method == 'POST':
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])
        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                message = 'success'
                TeacherName = request.POST.get('teacher_name')
                TeacherDob = request.POST.get('teacher_dob')
                if(len(str(TeacherDob)) != 0):
                    import datetime
                    TeacherDob = datetime.datetime.strptime(str(TeacherDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                else:
                    TeacherDob = None

                TeacherGender = request.POST.get('teacher_gender')
                TeacherFathers_name = request.POST.get('teacher_fathers_name')
                TeacherEmail = request.POST.get('teacher_email')
                TeacherContact = request.POST.get('teacher_contact')
                TeacherAddress = request.POST.get('teacher_address')
                branchPinCode = request.POST.get('branchPinCode')
                TeacherCity = request.POST.get('teacherCity')
                TeacherState = request.POST.get('teacher_state')
                branchCode = request.POST.get('branchCode')
                profileImage = request.FILES.get('profile_image')

                classList = request.POST.getlist('classArray[]')
                sectionList = request.POST.getlist('sectionArray[]')
                subjectList = request.POST.getlist('subjectArray[]')

                isClassTeacher = request.POST.get('isClassTeacher')
                classTeacherID = request.POST.get('classTeacherID')
                classTeacherSectionID = request.POST.get('classTeacherSectionID')

                class_Section_subject_detail_list = []
                for i in range(len(classList[0].split(','))):
                    class_Section_subject_detail_list.append([int(classList[0].split(',')[i]),int(sectionList[0].split(',')[i]),int(subjectList[0].split(',')[i])])

                try:
                    pwd_str = encrypt(b'123456',key_data)

                    if(isClassTeacher == 'true'):
                        isClassTeacher = '2'
                        classObj = class_master.objects.get(id=int(classTeacherID))
                        sectionObj = section_master.objects.get(id=int(classTeacherSectionID))
                        if(Teacher_user.objects.filter(class_master_fk = classObj,section_master_fk = sectionObj)):
                            return JsonResponse({'message':'Class teacher already exist'})

                        Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                        teacher_email = TeacherEmail,
                                                        teacher_contact = TeacherContact,
                                                        teacher_password = pwd_str,
                                                        profile_image = profileImage,
                                                        class_teacher_status = isClassTeacher,
                                                        class_master_fk = classObj,
                                                        section_master_fk = sectionObj)
                        Teacher_user_obj.save()
                        branchObj = branch.objects.get(id = int(branchCode))
                        Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                branch_FK = branchObj,
                                                                teacher_DOB = TeacherDob,
                                                                teacher_gender = TeacherGender,
                                                                teacher_fathers_name = TeacherFathers_name,
                                                                teacher_address = TeacherAddress,
                                                                teacher_pinCode = branchPinCode,
                                                                teacher_city = TeacherCity,
                                                                teacher_state = TeacherState,
                                                                class_section_subject_detail_fk = class_Section_subject_detail_list)
                        Teacher_profile_obj.save()
                    
                    if(isClassTeacher == 'false'):
                        isClassTeacher = '1'
                        Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                        teacher_email = TeacherEmail,
                                                        teacher_contact = TeacherContact,
                                                        teacher_password = pwd_str,
                                                        profile_image = profileImage,
                                                        class_teacher_status = isClassTeacher)

                        Teacher_user_obj.save()
                        branchObj = branch.objects.get(id = int(branchCode))
                        Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                branch_FK = branchObj,
                                                                teacher_DOB = TeacherDob,
                                                                teacher_gender = TeacherGender,
                                                                teacher_fathers_name = TeacherFathers_name,
                                                                teacher_address = TeacherAddress,
                                                                teacher_pinCode = branchPinCode,
                                                                teacher_city = TeacherCity,
                                                                teacher_state = TeacherState,
                                                                class_section_subject_detail_fk = class_Section_subject_detail_list)
                        Teacher_profile_obj.save()

                except:
                    message = 'failed'

                return JsonResponse({'message':message})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    message = 'success'
                    TeacherName = request.POST.get('teacher_name')
                    TeacherDob = request.POST.get('teacher_dob')
                    if(len(str(TeacherDob)) != 0):
                        import datetime
                        TeacherDob = datetime.datetime.strptime(str(TeacherDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        TeacherDob = None

                    TeacherGender = request.POST.get('teacher_gender')
                    TeacherFathers_name = request.POST.get('teacher_fathers_name')
                    TeacherEmail = request.POST.get('teacher_email')
                    TeacherContact = request.POST.get('teacher_contact')
                    TeacherAddress = request.POST.get('teacher_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    TeacherCity = request.POST.get('teacherCity')
                    TeacherState = request.POST.get('teacher_state')
                    branchCode = request.POST.get('branchCode')
                    profileImage = request.FILES.get('profile_image')

                    classList = request.POST.getlist('classArray[]')
                    sectionList = request.POST.getlist('sectionArray[]')
                    subjectList = request.POST.getlist('subjectArray[]')

                    isClassTeacher = request.POST.get('isClassTeacher')
                    classTeacherID = request.POST.get('classTeacherID')
                    classTeacherSectionID = request.POST.get('classTeacherSectionID')

                    class_Section_subject_detail_list = []
                    for i in range(len(classList[0].split(','))):
                        class_Section_subject_detail_list.append([int(classList[0].split(',')[i]),int(sectionList[0].split(',')[i]),int(subjectList[0].split(',')[i])])

                    try:
                        pwd_str = encrypt(b'123456',key_data)

                        if(isClassTeacher == 'true'):
                            isClassTeacher = '2'
                            classObj = class_master.objects.get(id=int(classTeacherID))
                            sectionObj = section_master.objects.get(id=int(classTeacherSectionID))
                            if(Teacher_user.objects.filter(class_master_fk = classObj,section_master_fk = sectionObj)):
                                return JsonResponse({'message':'Class teacher already exist'})

                            Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                            teacher_email = TeacherEmail,
                                                            teacher_contact = TeacherContact,
                                                            teacher_password = pwd_str,
                                                            profile_image = profileImage,
                                                            class_teacher_status = isClassTeacher,
                                                            class_master_fk = classObj,
                                                            section_master_fk = sectionObj,
                                                            created_by = f"Director - {directorObj.director_FK.director_name}")
                            Teacher_user_obj.save()
                            # branchObj = branch.objects.get(id = int(branchCode))
                            Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                    branch_FK = branchObj,
                                                                    teacher_DOB = TeacherDob,
                                                                    teacher_gender = TeacherGender,
                                                                    teacher_fathers_name = TeacherFathers_name,
                                                                    teacher_address = TeacherAddress,
                                                                    teacher_pinCode = branchPinCode,
                                                                    teacher_city = TeacherCity,
                                                                    teacher_state = TeacherState,
                                                                    class_section_subject_detail_fk = class_Section_subject_detail_list,
                                                                    created_by = f"Director - {directorObj.director_FK.director_name}")
                            Teacher_profile_obj.save()
                        
                        if(isClassTeacher == 'false'):
                            isClassTeacher = '1'
                            Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                            teacher_email = TeacherEmail,
                                                            teacher_contact = TeacherContact,
                                                            teacher_password = pwd_str,
                                                            profile_image = profileImage,
                                                            class_teacher_status = isClassTeacher,
                                                            created_by = f"Director - {directorObj.director_FK.director_name}")

                            Teacher_user_obj.save()
                            # branchObj = branch.objects.get(id = int(branchCode))
                            Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                    branch_FK = branchObj,
                                                                    teacher_DOB = TeacherDob,
                                                                    teacher_gender = TeacherGender,
                                                                    teacher_fathers_name = TeacherFathers_name,
                                                                    teacher_address = TeacherAddress,
                                                                    teacher_pinCode = branchPinCode,
                                                                    teacher_city = TeacherCity,
                                                                    teacher_state = TeacherState,
                                                                    class_section_subject_detail_fk = class_Section_subject_detail_list,
                                                                    created_by = f"Director - {directorObj.director_FK.director_name}")
                            Teacher_profile_obj.save()

                    except:
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    message = 'success'
                    TeacherName = request.POST.get('teacher_name')
                    TeacherDob = request.POST.get('teacher_dob')
                    if(len(str(TeacherDob)) != 0):
                        import datetime
                        TeacherDob = datetime.datetime.strptime(str(TeacherDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        TeacherDob = None

                    TeacherGender = request.POST.get('teacher_gender')
                    TeacherFathers_name = request.POST.get('teacher_fathers_name')
                    TeacherEmail = request.POST.get('teacher_email')
                    TeacherContact = request.POST.get('teacher_contact')
                    TeacherAddress = request.POST.get('teacher_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    TeacherCity = request.POST.get('teacherCity')
                    TeacherState = request.POST.get('teacher_state')
                    branchCode = request.POST.get('branchCode')
                    profileImage = request.FILES.get('profile_image')

                    classList = request.POST.getlist('classArray[]')
                    sectionList = request.POST.getlist('sectionArray[]')
                    subjectList = request.POST.getlist('subjectArray[]')

                    isClassTeacher = request.POST.get('isClassTeacher')
                    classTeacherID = request.POST.get('classTeacherID')
                    classTeacherSectionID = request.POST.get('classTeacherSectionID')

                    class_Section_subject_detail_list = []
                    for i in range(len(classList[0].split(','))):
                        class_Section_subject_detail_list.append([int(classList[0].split(',')[i]),int(sectionList[0].split(',')[i]),int(subjectList[0].split(',')[i])])

                    try:
                        pwd_str = encrypt(b'123456',key_data)

                        if(isClassTeacher == 'true'):
                            isClassTeacher = '2'
                            classObj = class_master.objects.get(id=int(classTeacherID))
                            sectionObj = section_master.objects.get(id=int(classTeacherSectionID))
                            if(Teacher_user.objects.filter(class_master_fk = classObj,section_master_fk = sectionObj)):
                                return JsonResponse({'message':'Class teacher already exist'})

                            Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                            teacher_email = TeacherEmail,
                                                            teacher_contact = TeacherContact,
                                                            teacher_password = pwd_str,
                                                            profile_image = profileImage,
                                                            class_teacher_status = isClassTeacher,
                                                            class_master_fk = classObj,
                                                            section_master_fk = sectionObj,
                                                            created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                            Teacher_user_obj.save()
                            # branchObj = branch.objects.get(id = int(branchCode))
                            Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                    branch_FK = branchObj,
                                                                    teacher_DOB = TeacherDob,
                                                                    teacher_gender = TeacherGender,
                                                                    teacher_fathers_name = TeacherFathers_name,
                                                                    teacher_address = TeacherAddress,
                                                                    teacher_pinCode = branchPinCode,
                                                                    teacher_city = TeacherCity,
                                                                    teacher_state = TeacherState,
                                                                    class_section_subject_detail_fk = class_Section_subject_detail_list,
                                                                    created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                            Teacher_profile_obj.save()
                        
                        if(isClassTeacher == 'false'):
                            isClassTeacher = '1'
                            Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                            teacher_email = TeacherEmail,
                                                            teacher_contact = TeacherContact,
                                                            teacher_password = pwd_str,
                                                            profile_image = profileImage,
                                                            class_teacher_status = isClassTeacher,
                                                            created_by = f"Principal - {directorObj.principal_FK.principal_name}")

                            Teacher_user_obj.save()
                            # branchObj = branch.objects.get(id = int(branchCode))
                            Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                    branch_FK = branchObj,
                                                                    teacher_DOB = TeacherDob,
                                                                    teacher_gender = TeacherGender,
                                                                    teacher_fathers_name = TeacherFathers_name,
                                                                    teacher_address = TeacherAddress,
                                                                    teacher_pinCode = branchPinCode,
                                                                    teacher_city = TeacherCity,
                                                                    teacher_state = TeacherState,
                                                                    class_section_subject_detail_fk = class_Section_subject_detail_list,
                                                                    created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                            Teacher_profile_obj.save()

                    except:
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    message = 'success'
                    TeacherName = request.POST.get('teacher_name')
                    TeacherDob = request.POST.get('teacher_dob')
                    if(len(str(TeacherDob)) != 0):
                        import datetime
                        TeacherDob = datetime.datetime.strptime(str(TeacherDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        TeacherDob = None

                    TeacherGender = request.POST.get('teacher_gender')
                    TeacherFathers_name = request.POST.get('teacher_fathers_name')
                    TeacherEmail = request.POST.get('teacher_email')
                    TeacherContact = request.POST.get('teacher_contact')
                    TeacherAddress = request.POST.get('teacher_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    TeacherCity = request.POST.get('teacherCity')
                    TeacherState = request.POST.get('teacher_state')
                    branchCode = request.POST.get('branchCode')
                    profileImage = request.FILES.get('profile_image')

                    classList = request.POST.getlist('classArray[]')
                    sectionList = request.POST.getlist('sectionArray[]')
                    subjectList = request.POST.getlist('subjectArray[]')

                    isClassTeacher = request.POST.get('isClassTeacher')
                    classTeacherID = request.POST.get('classTeacherID')
                    classTeacherSectionID = request.POST.get('classTeacherSectionID')

                    class_Section_subject_detail_list = []
                    for i in range(len(classList[0].split(','))):
                        class_Section_subject_detail_list.append([int(classList[0].split(',')[i]),int(sectionList[0].split(',')[i]),int(subjectList[0].split(',')[i])])

                    try:
                        pwd_str = encrypt(b'123456',key_data)

                        if(isClassTeacher == 'true'):
                            isClassTeacher = '2'
                            classObj = class_master.objects.get(id=int(classTeacherID))
                            sectionObj = section_master.objects.get(id=int(classTeacherSectionID))
                            if(Teacher_user.objects.filter(class_master_fk = classObj,section_master_fk = sectionObj)):
                                return JsonResponse({'message':'Class teacher already exist'})

                            Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                            teacher_email = TeacherEmail,
                                                            teacher_contact = TeacherContact,
                                                            teacher_password = pwd_str,
                                                            profile_image = profileImage,
                                                            class_teacher_status = isClassTeacher,
                                                            class_master_fk = classObj,
                                                            section_master_fk = sectionObj,
                                                            created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")
                            Teacher_user_obj.save()
                            # branchObj = branch.objects.get(id = int(branchCode))
                            Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                    branch_FK = branchObj,
                                                                    teacher_DOB = TeacherDob,
                                                                    teacher_gender = TeacherGender,
                                                                    teacher_fathers_name = TeacherFathers_name,
                                                                    teacher_address = TeacherAddress,
                                                                    teacher_pinCode = branchPinCode,
                                                                    teacher_city = TeacherCity,
                                                                    teacher_state = TeacherState,
                                                                    class_section_subject_detail_fk = class_Section_subject_detail_list,
                                                                    created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")
                            Teacher_profile_obj.save()
                        
                        if(isClassTeacher == 'false'):
                            isClassTeacher = '1'
                            Teacher_user_obj = Teacher_user(teacher_name = TeacherName,
                                                            teacher_email = TeacherEmail,
                                                            teacher_contact = TeacherContact,
                                                            teacher_password = pwd_str,
                                                            profile_image = profileImage,
                                                            class_teacher_status = isClassTeacher,
                                                            created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")

                            Teacher_user_obj.save()
                            # branchObj = branch.objects.get(id = int(branchCode))
                            Teacher_profile_obj = Teacher_profile(teacher_FK = Teacher_user_obj,
                                                                    branch_FK = branchObj,
                                                                    teacher_DOB = TeacherDob,
                                                                    teacher_gender = TeacherGender,
                                                                    teacher_fathers_name = TeacherFathers_name,
                                                                    teacher_address = TeacherAddress,
                                                                    teacher_pinCode = branchPinCode,
                                                                    teacher_city = TeacherCity,
                                                                    teacher_state = TeacherState,
                                                                    class_section_subject_detail_fk = class_Section_subject_detail_list,
                                                                    created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")
                            Teacher_profile_obj.save()

                    except:
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
        

# #####################################################################################################################
# upload Teacher list view
# #####################################################################################################################
@login_required(login_url='/')
def upload_Teacher_list(request):
    if request.method == 'GET':
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                return render(request,'admin_template/manage-type/teacher/upload-teacher-list.html')

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    return render(request,'admin_template/manage-type/teacher/upload-teacher-list.html')
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    return render(request,'admin_template/manage-type/teacher/upload-teacher-list.html')
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    return render(request,'admin_template/manage-type/teacher/upload-teacher-list.html')
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')

        return render(request,'admin_template/manage-type/teacher/upload-teacher-list.html')

# #####################################################################################################################
# Teacher details view
# #####################################################################################################################
@login_required(login_url='/')
def Teacher_detail(request,id):
    if request.method == 'GET':
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                teacher_profile_obj = Teacher_profile.objects.get(id=int(id))
                listData = []
                for i in eval(teacher_profile_obj.class_section_subject_detail_fk):
                    context = {}
                    context['class_name'] = class_master.objects.get(id=int(i[0])).class_name
                    context['section_name'] = section_master.objects.get(id=int(i[1])).section_name
                    context['subject_name'] = subject_master.objects.get(id=int(i[2])).subject_name
                    listData.append(context)
                return render(request,'admin_template/manage-type/teacher/teacher-details.html',{'teacher_profile_obj':teacher_profile_obj,'listData':listData})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        teacher_profile_obj = Teacher_profile.objects.get(id=int(id),branch_FK = branchObj)
                        listData = []
                        for i in eval(teacher_profile_obj.class_section_subject_detail_fk):
                            context = {}
                            context['class_name'] = class_master.objects.get(id=int(i[0])).class_name
                            context['section_name'] = section_master.objects.get(id=int(i[1])).section_name
                            context['subject_name'] = subject_master.objects.get(id=int(i[2])).subject_name
                            listData.append(context)
                        return render(request,'admin_template/manage-type/teacher/teacher-details.html',{'teacher_profile_obj':teacher_profile_obj,'listData':listData})
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        teacher_profile_obj = Teacher_profile.objects.get(id=int(id),branch_FK = branchObj)
                        listData = []
                        for i in eval(teacher_profile_obj.class_section_subject_detail_fk):
                            context = {}
                            context['class_name'] = class_master.objects.get(id=int(i[0])).class_name
                            context['section_name'] = section_master.objects.get(id=int(i[1])).section_name
                            context['subject_name'] = subject_master.objects.get(id=int(i[2])).subject_name
                            listData.append(context)
                        return render(request,'admin_template/manage-type/teacher/teacher-details.html',{'teacher_profile_obj':teacher_profile_obj,'listData':listData})
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        teacher_profile_obj = Teacher_profile.objects.get(id=int(id),branch_FK = branchObj)
                        listData = []
                        for i in eval(teacher_profile_obj.class_section_subject_detail_fk):
                            context = {}
                            context['class_name'] = class_master.objects.get(id=int(i[0])).class_name
                            context['section_name'] = section_master.objects.get(id=int(i[1])).section_name
                            context['subject_name'] = subject_master.objects.get(id=int(i[2])).subject_name
                            listData.append(context)
                        return render(request,'admin_template/manage-type/teacher/teacher-details.html',{'teacher_profile_obj':teacher_profile_obj,'listData':listData})
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')

# #####################################################################################################################
# Teacher edit view
# #####################################################################################################################
@login_required(login_url='/')
def edit_Teacher(request,id):
    auth_dict = get_auth_dict(request,request.session['userType'])
    sub_auth_dict = get_Subauth_dict(request,request.session['userType'])
    if request.method == 'GET':
        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                branchObj = branch.objects.all().order_by('-id')
                teacher_profile_obj = Teacher_profile.objects.get(id=int(id))
                return render(request,'admin_template/manage-type/teacher/edit-teacher-details.html',{'branchObj':branchObj,'teacher_profile_obj':teacher_profile_obj})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    teacher_profile_obj = Teacher_profile.objects.get(id=int(id))
                    return render(request,'admin_template/manage-type/teacher/teacher.html',{'Teacher_profile_obj':Teacher_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    teacher_profile_obj = Teacher_profile.objects.get(id=int(id))
                    return render(request,'admin_template/manage-type/teacher/teacher.html',{'Teacher_profile_obj':Teacher_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    teacher_profile_obj = Teacher_profile.objects.get(id=int(id))
                    return render(request,'admin_template/manage-type/teacher/teacher.html',{'Teacher_profile_obj':Teacher_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')



    if request.method == 'POST':
        message = 'success'
        TeacherName = request.POST.get('Teacher_name')
        TeacherDob = request.POST.get('Teacher_dob')
        if(len(str(TeacherDob)) != 0):
            import datetime
            TeacherDob = datetime.datetime.strptime(str(TeacherDob), '%m-%d-%Y').strftime('%Y-%m-%d')
        else:
            TeacherDob = None
        TeacherGender = request.POST.get('Teacher_gender')
        TeacherFathers_name = request.POST.get('Teacher_fathers_name')
        TeacherEmail = request.POST.get('Teacher_email')
        TeacherContact = request.POST.get('Teacher_contact')
        TeacherAddress = request.POST.get('Teacher_address')
        branchPinCode = request.POST.get('branchPinCode')
        TeacherCity = request.POST.get('TeacherCity')
        TeacherState = request.POST.get('Teacher_state')
        branchCode = request.POST.get('branchCode')
        profileImage = request.FILES.get('profile_image')

        print('profileImage >>> ',profileImage)

        try:
            Teacher_profile_obj = Teacher_profile.objects.get(id=int(id))

            Teacher_user_obj = Teacher_user.objects.get(id=int(Teacher_profile_obj.Teacher_FK.id))
            Teacher_user_obj.Teacher_name = TeacherName
            Teacher_user_obj.Teacher_email = TeacherEmail
            Teacher_user_obj.Teacher_contact = TeacherContact
            # Teacher_user_obj.Teacher_password = '123456'
            if(profileImage != None):
                print('none data')
                Teacher_user_obj.profile_image = profileImage
            Teacher_user_obj.save()

            branchObj = branch.objects.get(id = int(branchCode))
            
            Teacher_profile_obj.Teacher_FK = Teacher_user_obj
            Teacher_profile_obj.branch_FK = branchObj
            Teacher_profile_obj.Teacher_DOB = TeacherDob
            Teacher_profile_obj.Teacher_gender = TeacherGender
            Teacher_profile_obj.Teacher_fathers_name = TeacherFathers_name
            Teacher_profile_obj.Teacher_address = TeacherAddress
            Teacher_profile_obj.Teacher_pinCode = branchPinCode
            Teacher_profile_obj.Teacher_city = TeacherCity
            Teacher_profile_obj.Teacher_state = TeacherState
            Teacher_profile_obj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def delete_Teacher(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])
        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                teacher_profileObj = Teacher_profile.objects.get(id=int(id))
                teacher_userObj = Teacher_user.objects.get(id=int(teacher_profileObj.teacher_FK.id))
                teacher_userObj.delete()
                return redirect('Teacher_list')

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    teacher_profileObj = Teacher_profile.objects.get(id=int(id))
                    teacher_userObj = Teacher_user.objects.get(id=int(teacher_profileObj.teacher_FK.id))
                    teacher_userObj.delete()
                    return redirect('Teacher_list')
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    teacher_profileObj = Teacher_profile.objects.get(id=int(id))
                    teacher_userObj = Teacher_user.objects.get(id=int(teacher_profileObj.teacher_FK.id))
                    teacher_userObj.delete()
                    return redirect('Teacher_list')

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    teacher_profileObj = Teacher_profile.objects.get(id=int(id))
                    teacher_userObj = Teacher_user.objects.get(id=int(teacher_profileObj.teacher_FK.id))
                    teacher_userObj.delete()
                    return redirect('Teacher_list')

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# delete branch view
# #####################################################################################################################
@login_required(login_url='/')
def change_Teacher_status(request):
    if request.method == 'POST':
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                message = 'success'
                TeacherId = request.POST['teacherId']
                data = request.POST['data']

                if(data == 'true'):
                    data = '1'
                if(data == 'false'):
                    data = '2'

                try:
                    Teacher_profileObj = Teacher_profile.objects.get(id=int(TeacherId))
                    Teacher_userObj = Teacher_user.objects.get(id=int(Teacher_profileObj.teacher_FK.id))

                    Teacher_userObj.active_status = data
                    Teacher_userObj.save()

                except:
                    message = 'failed'
                return JsonResponse({'message':message})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'success'
                    TeacherId = request.POST['teacherId']
                    data = request.POST['data']

                    if(data == 'true'):
                        data = '1'
                    if(data == 'false'):
                        data = '2'

                    try:
                        Teacher_profileObj = Teacher_profile.objects.get(id=int(TeacherId))
                        Teacher_userObj = Teacher_user.objects.get(id=int(Teacher_profileObj.teacher_FK.id))

                        Teacher_userObj.active_status = data
                        Teacher_userObj.save()

                    except:
                        message = 'failed'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'success'
                    TeacherId = request.POST['teacherId']
                    data = request.POST['data']

                    if(data == 'true'):
                        data = '1'
                    if(data == 'false'):
                        data = '2'

                    try:
                        Teacher_profileObj = Teacher_profile.objects.get(id=int(TeacherId))
                        Teacher_userObj = Teacher_user.objects.get(id=int(Teacher_profileObj.teacher_FK.id))

                        Teacher_userObj.active_status = data
                        Teacher_userObj.save()

                    except:
                        message = 'failed'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'success'
                    TeacherId = request.POST['teacherId']
                    data = request.POST['data']

                    if(data == 'true'):
                        data = '1'
                    if(data == 'false'):
                        data = '2'

                    try:
                        Teacher_profileObj = Teacher_profile.objects.get(id=int(TeacherId))
                        Teacher_userObj = Teacher_user.objects.get(id=int(Teacher_profileObj.teacher_FK.id))

                        Teacher_userObj.active_status = data
                        Teacher_userObj.save()

                    except:
                        message = 'failed'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
        

# #####################################################################################################################
# check branch for existing Teacher view
# #####################################################################################################################
@login_required(login_url='/')
def Teacher_checkBranch(request):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])
        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                message = 'not-exist'
                searchStr = request.GET['branchCode']
                branchObj = branch.objects.get(id = int(searchStr))
                try:
                    if(Teacher_profile.objects.filter(branch_FK = branchObj)):
                        message = 'Teacher-branch-exist'
                except:
                    message = 'not-exist'
                return JsonResponse({'message':message})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'not-exist'
                    searchStr = request.GET['branchCode']
                    branchObj = branch.objects.get(id = int(searchStr))
                    try:
                        if(Teacher_profile.objects.filter(branch_FK = branchObj)):
                            message = 'Teacher-branch-exist'
                    except:
                        message = 'not-exist'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'not-exist'
                    searchStr = request.GET['branchCode']
                    branchObj = branch.objects.get(id = int(searchStr))
                    try:
                        if(Teacher_profile.objects.filter(branch_FK = branchObj)):
                            message = 'Teacher-branch-exist'
                    except:
                        message = 'not-exist'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'not-exist'
                    searchStr = request.GET['branchCode']
                    branchObj = branch.objects.get(id = int(searchStr))
                    try:
                        if(Teacher_profile.objects.filter(branch_FK = branchObj)):
                            message = 'Teacher-branch-exist'
                    except:
                        message = 'not-exist'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# Teacher fields check view
# #####################################################################################################################
@login_required(login_url='/')
def Teacher_field_check(request):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'super_admin_login'):
                message = 'not-exist'
                fieldType = request.GET['fieldType']
                searchString = request.GET['searchString']

                if(fieldType == 'teacher_email'):
                    TeacherObj = Teacher_user.objects.filter(teacher_email=searchString)
                    if(TeacherObj):
                        message = 'teacher-email-exist'

                elif(fieldType == 'teacher_contact'):
                    TeacherObj = Teacher_user.objects.filter(teacher_contact=searchString)
                    if(TeacherObj):
                        message = 'teacher-contact-exist'

                return JsonResponse({'message':message})

            elif(request.session['userType'] == 'director_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'not-exist'
                    fieldType = request.GET['fieldType']
                    searchString = request.GET['searchString']

                    if(fieldType == 'teacher_email'):
                        TeacherObj = Teacher_user.objects.filter(teacher_email=searchString)
                        if(TeacherObj):
                            message = 'teacher-email-exist'

                    elif(fieldType == 'teacher_contact'):
                        TeacherObj = Teacher_user.objects.filter(teacher_contact=searchString)
                        if(TeacherObj):
                            message = 'teacher-contact-exist'

                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'principal_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'not-exist'
                    fieldType = request.GET['fieldType']
                    searchString = request.GET['searchString']

                    if(fieldType == 'teacher_email'):
                        TeacherObj = Teacher_user.objects.filter(teacher_email=searchString)
                        if(TeacherObj):
                            message = 'teacher-email-exist'

                    elif(fieldType == 'teacher_contact'):
                        TeacherObj = Teacher_user.objects.filter(teacher_contact=searchString)
                        if(TeacherObj):
                            message = 'teacher-contact-exist'

                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'school_admin_login'):
                if(sub_auth_dict['Teacher'] == True):
                    message = 'not-exist'
                    fieldType = request.GET['fieldType']
                    searchString = request.GET['searchString']

                    if(fieldType == 'teacher_email'):
                        TeacherObj = Teacher_user.objects.filter(teacher_email=searchString)
                        if(TeacherObj):
                            message = 'teacher-email-exist'

                    elif(fieldType == 'teacher_contact'):
                        TeacherObj = Teacher_user.objects.filter(teacher_contact=searchString)
                        if(TeacherObj):
                            message = 'teacher-contact-exist'

                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')

        

# #####################################################################################################################
# GET CLASS LIST with Branch view
# #####################################################################################################################
@login_required(login_url='/')
def add_teacher_get_class(request):
    if request.method == 'GET':
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        classList = []
        branchID = request.GET['branchID']
        branchObj = branch.objects.get(id=int(branchID))
        if(class_master.objects.filter(branch_FK = branchObj)):
            for i in class_master.objects.filter(branch_FK = branchObj):
                context = {}
                context['id'] = i.id
                context['class_name'] = i.class_name
                classList.append(context)

        return JsonResponse({'classList':classList})


# #####################################################################################################################
# GET section and section LIST with class view
# #####################################################################################################################
@login_required(login_url='/')
def get_subject_and_section(request):
    if request.method == 'GET':
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        subjectList = []
        classID = request.GET['classID']
        classObj = class_master.objects.get(id=int(classID))

        for j in eval(classObj.subject_fk):
            context = {}
            context['id'] = subject_master.objects.get(id=int(j)).id
            context['subject_name'] = subject_master.objects.get(id=int(j)).subject_name.title()
            subjectList.append(context)
        
        sectionList = []
        sectionDetailsList = eval(classObj.section_details_fk)
        print(sectionDetailsList,type(sectionList))
        for i in sectionDetailsList:
            context = {}
            context['id'] = section_master.objects.get(id=int(i[0])).id
            context['section_name'] = f"{section_master.objects.get(id=int(i[0])).section_name.title()} - {class_type_master.objects.get(id=int(i[1])).class_subType_name.title()}"
            sectionList.append(context)

        return JsonResponse({'subjectList':subjectList,'sectionList':sectionList})