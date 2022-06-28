from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required

from slms_web_app.models.master_models import section_master, subject_master
from ...models.manage_models import branch, class_master, parent_user,student_profile,student_user,director_profile,principal_profile,schoolAdmin_profile
from ...models.master_models import class_type_master

from cryptography.fernet import Fernet
key_data = b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

from ..utils_views import get_auth_dict,get_Subauth_dict
import datetime
# publicKey, privateKey = bytes("005cea8f-da1e-40db-91df-8657e49d3795", 'utf-8'),bytes("005cea8f-da1e-40db-91df-8657e49d3795", 'utf-8')
# #####################################################################################################################
# student_list view
# #####################################################################################################################
# @login_required(login_url='/')
def student_list(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Student_List'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    student_profile_obj = student_profile.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/student/student-list.html',{'branchObj':branchObj,'student_profile_obj':student_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Student_List'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    student_profile_obj = student_profile.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/student/student-list.html',{'branchObj':branchObj,'student_profile_obj':student_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Student_List'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    student_profile_obj = student_profile.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/student/student-list.html',{'branchObj':branchObj,'student_profile_obj':student_profile_obj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')

# #####################################################################################################################
# add new student view
# #####################################################################################################################
# @login_required(login_url='/')
def add_new_student(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/student/add-student.html',{'branchObj':branchObj,'classObj':classObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/student/add-student.html',{'branchObj':branchObj,'classObj':classObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK = branchObj)
                    return render(request,'admin_template/manage-type/student/add-student.html',{'branchObj':branchObj,'classObj':classObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
        

    if request.method == 'POST':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    message = 'success'
                    student_registration_no = request.POST.get('student_registration_number')
                    student_fname = request.POST.get('student_fname')
                    student_lname = request.POST.get('student_lname')
                    studentDob = request.POST.get('student_dob')
                    if(len(str(studentDob)) != 0):
                        import datetime
                        studentDob = datetime.datetime.strptime(str(studentDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        studentDob = None

                    studentGender = request.POST.get('student_gender')
                    student_parent_name = request.POST.get('student_parent_name')
                    student_parentRelation = request.POST.get('student_parent_relation')
                    studentHobbies = request.POST.getlist('student_hobbies[]')

                    studentEmail = request.POST.get('student_email')
                    studentContact = request.POST.get('student_contact')
                    student_parentContact = request.POST.get('student_parent_contact')

                    studentAddress = request.POST.get('student_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    studentCity = request.POST.get('studentCity')
                    studentState = request.POST.get('student_state')
                    # branchCode = request.POST.get('branchCode')

                    student_class = request.POST.get('student_class')
                    student_section = request.POST.get('student_section')
                    student_subject = request.POST.getlist('student_subject[]')

                    profileImage = request.FILES.get('profile_image')

                    list1 = []
                    for i in student_subject[0].split(','):
                        list1.append(int(i))
            
                    try:
                        pwd_str = encrypt(b'123456',key_data)
                        
                        student_user_obj = student_user(student_first_name = student_fname,
                                                        student_last_name = student_lname,
                                                        student_registration_number = student_registration_no,
                                                        student_email = studentEmail,
                                                        student_contact = studentContact,
                                                        student_password = pwd_str,
                                                        profile_image = profileImage,
                                                        created_by = f"Director - {directorObj.director_FK.director_name}")
                        student_user_obj.save()
                        # branchObj = branch.objects.get(id = int(branchCode))
                        classObj = class_master.objects.get(id = int(student_class))
                        sectionObj = section_master.objects.get(id = int(student_section))

                        student_profile_obj = student_profile(student_FK = student_user_obj,
                                                                branch_FK = branchObj,
                                                                student_DOB = studentDob,
                                                                student_gender = studentGender,
                                                                student_fathers_name = student_parent_name,
                                                                student_parent_relation = student_parentRelation,
                                                                student_hobbies = studentHobbies,
                                                                student_parent_contact = student_parentContact,
                                                                student_address = studentAddress,
                                                                student_pinCode = branchPinCode,
                                                                student_city = studentCity,
                                                                student_state = studentState,
                                                                class_fk = classObj,
                                                                section_fk = sectionObj,
                                                                subject_fk = list1,
                                                                created_by = f"Director - {directorObj.director_FK.director_name}"
                                                                )

                        student_profile_obj.save()

                        parent_user_obj = parent_user(student_fk = student_profile_obj,
                                                    parent_name = student_parent_name,
                                                    parent_contact = student_parentContact,
                                                    parent_password = pwd_str,
                                                    created_by = f"Director - {directorObj.director_FK.director_name}"
                                                    )
                        parent_user_obj.save()

                    except:
                        student_user_obj = student_user.objects.latest('id')
                        student_user_obj.delete()
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    message = 'success'
                    student_registration_no = request.POST.get('student_registration_number')
                    student_fname = request.POST.get('student_fname')
                    student_lname = request.POST.get('student_lname')
                    studentDob = request.POST.get('student_dob')
                    if(len(str(studentDob)) != 0):
                        import datetime
                        studentDob = datetime.datetime.strptime(str(studentDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        studentDob = None

                    studentGender = request.POST.get('student_gender')
                    student_parent_name = request.POST.get('student_parent_name')
                    student_parentRelation = request.POST.get('student_parent_relation')
                    studentHobbies = request.POST.getlist('student_hobbies[]')

                    studentEmail = request.POST.get('student_email')
                    studentContact = request.POST.get('student_contact')
                    student_parentContact = request.POST.get('student_parent_contact')

                    studentAddress = request.POST.get('student_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    studentCity = request.POST.get('studentCity')
                    studentState = request.POST.get('student_state')
                    # branchCode = request.POST.get('branchCode')

                    student_class = request.POST.get('student_class')
                    student_section = request.POST.get('student_section')
                    student_subject = request.POST.getlist('student_subject[]')

                    profileImage = request.FILES.get('profile_image')

                    list1 = []
                    for i in student_subject[0].split(','):
                        list1.append(int(i))
            
                    try:
                        pwd_str = encrypt(b'123456',key_data)
                        
                        student_user_obj = student_user(student_first_name = student_fname,
                                                        student_last_name = student_lname,
                                                        student_registration_number = student_registration_no,
                                                        student_email = studentEmail,
                                                        student_contact = studentContact,
                                                        student_password = pwd_str,
                                                        profile_image = profileImage,
                                                        created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                        student_user_obj.save()
                        # branchObj = branch.objects.get(id = int(branchCode))
                        classObj = class_master.objects.get(id = int(student_class))
                        sectionObj = section_master.objects.get(id = int(student_section))

                        student_profile_obj = student_profile(student_FK = student_user_obj,
                                                                branch_FK = branchObj,
                                                                student_DOB = studentDob,
                                                                student_gender = studentGender,
                                                                student_fathers_name = student_parent_name,
                                                                student_parent_relation = student_parentRelation,
                                                                student_hobbies = studentHobbies,
                                                                student_parent_contact = student_parentContact,
                                                                student_address = studentAddress,
                                                                student_pinCode = branchPinCode,
                                                                student_city = studentCity,
                                                                student_state = studentState,
                                                                class_fk = classObj,
                                                                section_fk = sectionObj,
                                                                subject_fk = list1,
                                                                created_by = f"Principal - {directorObj.principal_FK.principal_name}"
                                                                )

                        student_profile_obj.save()

                        parent_user_obj = parent_user(student_fk = student_profile_obj,
                                                    parent_name = student_parent_name,
                                                    parent_contact = student_parentContact,
                                                    parent_password = pwd_str,
                                                    created_by = f"Principal - {directorObj.principal_FK.principal_name}"
                                                    )
                        parent_user_obj.save()

                    except:
                        student_user_obj = student_user.objects.latest('id')
                        student_user_obj.delete()
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    message = 'success'
                    student_registration_no = request.POST.get('student_registration_number')
                    student_fname = request.POST.get('student_fname')
                    student_lname = request.POST.get('student_lname')
                    studentDob = request.POST.get('student_dob')
                    if(len(str(studentDob)) != 0):
                        import datetime
                        studentDob = datetime.datetime.strptime(str(studentDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        studentDob = None

                    studentGender = request.POST.get('student_gender')
                    student_parent_name = request.POST.get('student_parent_name')
                    student_parentRelation = request.POST.get('student_parent_relation')
                    studentHobbies = request.POST.getlist('student_hobbies[]')

                    studentEmail = request.POST.get('student_email')
                    studentContact = request.POST.get('student_contact')
                    student_parentContact = request.POST.get('student_parent_contact')

                    studentAddress = request.POST.get('student_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    studentCity = request.POST.get('studentCity')
                    studentState = request.POST.get('student_state')
                    # branchCode = request.POST.get('branchCode')

                    student_class = request.POST.get('student_class')
                    student_section = request.POST.get('student_section')
                    student_subject = request.POST.getlist('student_subject[]')

                    profileImage = request.FILES.get('profile_image')

                    list1 = []
                    for i in student_subject[0].split(','):
                        list1.append(int(i))
            
                    try:
                        pwd_str = encrypt(b'123456',key_data)
                        
                        student_user_obj = student_user(student_first_name = student_fname,
                                                        student_last_name = student_lname,
                                                        student_registration_number = student_registration_no,
                                                        student_email = studentEmail,
                                                        student_contact = studentContact,
                                                        student_password = pwd_str,
                                                        profile_image = profileImage,
                                                        created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")
                        student_user_obj.save()
                        # branchObj = branch.objects.get(id = int(branchCode))
                        classObj = class_master.objects.get(id = int(student_class))
                        sectionObj = section_master.objects.get(id = int(student_section))

                        student_profile_obj = student_profile(student_FK = student_user_obj,
                                                                branch_FK = branchObj,
                                                                student_DOB = studentDob,
                                                                student_gender = studentGender,
                                                                student_fathers_name = student_parent_name,
                                                                student_parent_relation = student_parentRelation,
                                                                student_hobbies = studentHobbies,
                                                                student_parent_contact = student_parentContact,
                                                                student_address = studentAddress,
                                                                student_pinCode = branchPinCode,
                                                                student_city = studentCity,
                                                                student_state = studentState,
                                                                class_fk = classObj,
                                                                section_fk = sectionObj,
                                                                subject_fk = list1,
                                                                created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}"
                                                                )

                        student_profile_obj.save()

                        parent_user_obj = parent_user(student_fk = student_profile_obj,
                                                    parent_name = student_parent_name,
                                                    parent_contact = student_parentContact,
                                                    parent_password = pwd_str,
                                                    created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}"
                                                    )
                        parent_user_obj.save()

                    except:
                        student_user_obj = student_user.objects.latest('id')
                        student_user_obj.delete()
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')







        

# #####################################################################################################################
# upload student list view
# #####################################################################################################################
# @login_required(login_url='/')
def upload_student_list(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    return render(request,'admin_template/manage-type/student/upload-student-list.html',{'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    return render(request,'admin_template/manage-type/student/upload-student-list.html',{'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Student'] == True):
                    return render(request,'admin_template/manage-type/student/upload-student-list.html',{'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
        

# #####################################################################################################################
# student details view
# #####################################################################################################################
# @login_required(login_url='/')
def student_detail(request,id):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Student_List'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id),branch_FK=branchObj)
                        hobbyList = []
                        for i in eval(student_profile_obj.student_hobbies):
                            hobbyList.append(i)

                        subjectList = []
                        for i in eval(student_profile_obj.subject_fk):
                            subjectList.append(subject_master.objects.get(id=int(i)).subject_name)
                        return render(request,'admin_template/manage-type/student/student-detail.html',{'student_profile_obj':student_profile_obj,'hobbyList':hobbyList,'subjectList':subjectList,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                    except:
                        return render(request,'403.html')

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Student_List'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id),branch_FK=branchObj)
                        hobbyList = []
                        for i in eval(student_profile_obj.student_hobbies):
                            hobbyList.append(i)

                        subjectList = []
                        for i in eval(student_profile_obj.subject_fk):
                            subjectList.append(subject_master.objects.get(id=int(i)).subject_name)
                        return render(request,'admin_template/manage-type/student/student-detail.html',{'student_profile_obj':student_profile_obj,'hobbyList':hobbyList,'subjectList':subjectList,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                    except:
                        return render(request,'403.html')

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Student_List'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id),branch_FK=branchObj)
                        hobbyList = []
                        for i in eval(student_profile_obj.student_hobbies):
                            hobbyList.append(i)

                        subjectList = []
                        for i in eval(student_profile_obj.subject_fk):
                            subjectList.append(subject_master.objects.get(id=int(i)).subject_name)
                        return render(request,'admin_template/manage-type/student/student-detail.html',{'student_profile_obj':student_profile_obj,'hobbyList':hobbyList,'subjectList':subjectList,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                    except:
                        return render(request,'403.html')

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# student edit view
# #####################################################################################################################
# @login_required(login_url='/')
def edit_student(request,id):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id),branch_FK=branchObj)
                    except:
                        return render(request,'403.html')
                    classList = []
                    sujectList = []
                    sectionList = []

                    classObj = class_master.objects.filter(branch_FK = student_profile_obj.branch_FK)
                    for i in classObj:
                        context = {}
                        context['id'] = i.id
                        context['class_name'] = i.class_name
                        if(int(i.id) == int(student_profile_obj.class_fk.id)):
                            context['status'] = 'true'
                        else:
                            context['status'] = 'false'
                        classList.append(context)

                    classObj = class_master.objects.get(id = int(student_profile_obj.class_fk.id))
                    for j in eval(classObj.subject_fk):
                        context = {}
                        context['id'] = subject_master.objects.get(id=int(j)).id
                        context['subject_name'] = subject_master.objects.get(id=int(j)).subject_name.title()
                        sujectList.append(context)

                    sectionList = []
                    sectionDetailsList = eval(classObj.section_details_fk)
                    print(sectionDetailsList,type(sectionList))
                    for i in sectionDetailsList:
                        context = {}
                        context['id'] = section_master.objects.get(id=int(i[0])).id
                        context['section_name'] = f"{section_master.objects.get(id=int(i[0])).section_name} - {class_type_master.objects.get(id=int(i[1])).class_subType_name}"
                        if(int(section_master.objects.get(id=int(i[0])).id) == int(student_profile_obj.section_fk.id)):
                            context['status'] = 'true'
                        else:
                            context['status'] = 'false'
                        sectionList.append(context)

                    return render(request,'admin_template/manage-type/student/edit-student-detail.html',{'branchObj':branchObj,'student_profile_obj':student_profile_obj,'classList':classList,'sujectList':sujectList,'sectionList':sectionList,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id),branch_FK=branchObj)
                    except:
                        return render(request,'403.html')
                    classList = []
                    sujectList = []
                    sectionList = []

                    classObj = class_master.objects.filter(branch_FK = student_profile_obj.branch_FK)
                    for i in classObj:
                        context = {}
                        context['id'] = i.id
                        context['class_name'] = i.class_name
                        if(int(i.id) == int(student_profile_obj.class_fk.id)):
                            context['status'] = 'true'
                        else:
                            context['status'] = 'false'
                        classList.append(context)

                    classObj = class_master.objects.get(id = int(student_profile_obj.class_fk.id))
                    for j in eval(classObj.subject_fk):
                        context = {}
                        context['id'] = subject_master.objects.get(id=int(j)).id
                        context['subject_name'] = subject_master.objects.get(id=int(j)).subject_name.title()
                        sujectList.append(context)

                    sectionList = []
                    sectionDetailsList = eval(classObj.section_details_fk)
                    print(sectionDetailsList,type(sectionList))
                    for i in sectionDetailsList:
                        context = {}
                        context['id'] = section_master.objects.get(id=int(i[0])).id
                        context['section_name'] = f"{section_master.objects.get(id=int(i[0])).section_name} - {class_type_master.objects.get(id=int(i[1])).class_subType_name}"
                        if(int(section_master.objects.get(id=int(i[0])).id) == int(student_profile_obj.section_fk.id)):
                            context['status'] = 'true'
                        else:
                            context['status'] = 'false'
                        sectionList.append(context)

                    return render(request,'admin_template/manage-type/student/edit-student-detail.html',{'branchObj':branchObj,'student_profile_obj':student_profile_obj,'classList':classList,'sujectList':sujectList,'sectionList':sectionList,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id),branch_FK=branchObj)
                    except:
                        return render(request,'403.html')
                    classList = []
                    sujectList = []
                    sectionList = []

                    classObj = class_master.objects.filter(branch_FK = student_profile_obj.branch_FK)
                    for i in classObj:
                        context = {}
                        context['id'] = i.id
                        context['class_name'] = i.class_name
                        if(int(i.id) == int(student_profile_obj.class_fk.id)):
                            context['status'] = 'true'
                        else:
                            context['status'] = 'false'
                        classList.append(context)

                    classObj = class_master.objects.get(id = int(student_profile_obj.class_fk.id))
                    for j in eval(classObj.subject_fk):
                        context = {}
                        context['id'] = subject_master.objects.get(id=int(j)).id
                        context['subject_name'] = subject_master.objects.get(id=int(j)).subject_name.title()
                        sujectList.append(context)

                    sectionList = []
                    sectionDetailsList = eval(classObj.section_details_fk)
                    print(sectionDetailsList,type(sectionList))
                    for i in sectionDetailsList:
                        context = {}
                        context['id'] = section_master.objects.get(id=int(i[0])).id
                        context['section_name'] = f"{section_master.objects.get(id=int(i[0])).section_name} - {class_type_master.objects.get(id=int(i[1])).class_subType_name}"
                        if(int(section_master.objects.get(id=int(i[0])).id) == int(student_profile_obj.section_fk.id)):
                            context['status'] = 'true'
                        else:
                            context['status'] = 'false'
                        sectionList.append(context)

                    return render(request,'admin_template/manage-type/student/edit-student-detail.html',{'branchObj':branchObj,'student_profile_obj':student_profile_obj,'classList':classList,'sujectList':sujectList,'sectionList':sectionList,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')


        


    if request.method == 'POST':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    message = 'success'
                    student_registration_no = request.POST.get('student_registration_number')
                    student_fname = request.POST.get('student_fname')
                    student_lname = request.POST.get('student_lname')
                    studentDob = request.POST.get('student_dob')
                    if(len(str(studentDob)) != 0):
                        import datetime
                        studentDob = datetime.datetime.strptime(str(studentDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        studentDob = None

                    studentGender = request.POST.get('student_gender')
                    student_parent_name = request.POST.get('student_parent_name')
                    student_parentRelation = request.POST.get('student_parent_relation')
                    studentHobbies = request.POST.getlist('student_hobbies[]')

                    studentEmail = request.POST.get('student_email')
                    studentContact = request.POST.get('student_contact')
                    student_parentContact = request.POST.get('student_parent_contact')

                    studentAddress = request.POST.get('student_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    studentCity = request.POST.get('studentCity')
                    studentState = request.POST.get('student_state')
                    branchCode = request.POST.get('branchCode')

                    student_class = request.POST.get('student_class')
                    student_section = request.POST.get('student_section')
                    student_subject = request.POST.getlist('student_subject[]')

                    profileImage = request.FILES.get('profile_image')

                    list1 = []
                    for i in student_subject[0].split(','):
                        list1.append(int(i))

                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id))

                        student_user_obj = student_user.objects.get(id=int(student_profile_obj.student_FK.id))
                        student_user_obj.student_first_name = student_fname
                        student_user_obj.student_last_name = student_lname
                        student_user_obj.student_registration_number = student_registration_no
                        student_user_obj.student_email = studentEmail
                        student_user_obj.student_contact = studentContact
                        student_user_obj.last_updated_by = f"Director - {directorObj.director_FK.director_name}"
                        student_user_obj.last_updated_at = datetime.datetime.now()

                        if(profileImage != None):
                            print('none data')
                            student_user_obj.profile_image = profileImage
                        student_user_obj.save()

                        # branchObj = branch.objects.get(id = int(branchCode))
                        classObj = class_master.objects.get(id = int(student_class))
                        sectionObj = section_master.objects.get(id = int(student_section))
                        student_profile_obj.student_FK = student_user_obj
                        # student_profile_obj.branch_FK = branchObj
                        student_profile_obj.student_DOB = studentDob
                        student_profile_obj.student_gender = studentGender
                        student_profile_obj.student_fathers_name = student_parent_name
                        student_profile_obj.student_parent_relation = student_parentRelation
                        student_profile_obj.student_hobbies = studentHobbies
                        student_profile_obj.student_parent_contact = student_parentContact
                        student_profile_obj.student_address = studentAddress
                        student_profile_obj.student_pinCode = branchPinCode
                        student_profile_obj.student_city = studentCity
                        student_profile_obj.student_state = studentState
                        student_profile_obj.class_fk = classObj
                        student_profile_obj.section_fk = sectionObj
                        student_profile_obj.subject_fk = list1
                        student_profile_obj.last_updated_by = f"Director - {directorObj.director_FK.director_name}"
                        student_profile_obj.last_updated_at = datetime.datetime.now()
                        student_profile_obj.save()

                        parent_user_obj = parent_user.objects.get(student_fk = student_profile_obj)
                        parent_user_obj.student_fk = student_profile_obj
                        parent_user_obj.parent_name = student_parent_name
                        parent_user_obj.parent_contact = student_parentContact
                        parent_user_obj.last_updated_by = f"Director - {directorObj.director_FK.director_name}"
                        parent_user_obj.last_updated_at = datetime.datetime.now()
                        student_profile_obj.save()

                    except:
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    message = 'success'
                    student_registration_no = request.POST.get('student_registration_number')
                    student_fname = request.POST.get('student_fname')
                    student_lname = request.POST.get('student_lname')
                    studentDob = request.POST.get('student_dob')
                    if(len(str(studentDob)) != 0):
                        import datetime
                        studentDob = datetime.datetime.strptime(str(studentDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        studentDob = None

                    studentGender = request.POST.get('student_gender')
                    student_parent_name = request.POST.get('student_parent_name')
                    student_parentRelation = request.POST.get('student_parent_relation')
                    studentHobbies = request.POST.getlist('student_hobbies[]')

                    studentEmail = request.POST.get('student_email')
                    studentContact = request.POST.get('student_contact')
                    student_parentContact = request.POST.get('student_parent_contact')

                    studentAddress = request.POST.get('student_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    studentCity = request.POST.get('studentCity')
                    studentState = request.POST.get('student_state')
                    branchCode = request.POST.get('branchCode')

                    student_class = request.POST.get('student_class')
                    student_section = request.POST.get('student_section')
                    student_subject = request.POST.getlist('student_subject[]')

                    profileImage = request.FILES.get('profile_image')

                    list1 = []
                    for i in student_subject[0].split(','):
                        list1.append(int(i))

                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id))

                        student_user_obj = student_user.objects.get(id=int(student_profile_obj.student_FK.id))
                        student_user_obj.student_first_name = student_fname
                        student_user_obj.student_last_name = student_lname
                        student_user_obj.student_registration_number = student_registration_no
                        student_user_obj.student_email = studentEmail
                        student_user_obj.student_contact = studentContact
                        student_user_obj.last_updated_by = f"Principal - {directorObj.principal_FK.principal_name}"
                        student_user_obj.last_updated_at = datetime.datetime.now()

                        if(profileImage != None):
                            print('none data')
                            student_user_obj.profile_image = profileImage
                        student_user_obj.save()

                        # branchObj = branch.objects.get(id = int(branchCode))
                        classObj = class_master.objects.get(id = int(student_class))
                        sectionObj = section_master.objects.get(id = int(student_section))
                        student_profile_obj.student_FK = student_user_obj
                        # student_profile_obj.branch_FK = branchObj
                        student_profile_obj.student_DOB = studentDob
                        student_profile_obj.student_gender = studentGender
                        student_profile_obj.student_fathers_name = student_parent_name
                        student_profile_obj.student_parent_relation = student_parentRelation
                        student_profile_obj.student_hobbies = studentHobbies
                        student_profile_obj.student_parent_contact = student_parentContact
                        student_profile_obj.student_address = studentAddress
                        student_profile_obj.student_pinCode = branchPinCode
                        student_profile_obj.student_city = studentCity
                        student_profile_obj.student_state = studentState
                        student_profile_obj.class_fk = classObj
                        student_profile_obj.section_fk = sectionObj
                        student_profile_obj.subject_fk = list1
                        student_profile_obj.last_updated_by = f"Principal - {directorObj.principal_FK.principal_name}"
                        student_profile_obj.last_updated_at = datetime.datetime.now()
                        student_profile_obj.save()

                        parent_user_obj = parent_user.objects.get(student_fk = student_profile_obj)
                        parent_user_obj.student_fk = student_profile_obj
                        parent_user_obj.parent_name = student_parent_name
                        parent_user_obj.parent_contact = student_parentContact
                        parent_user_obj.last_updated_by = f"Principal - {directorObj.principal_FK.principal_name}"
                        parent_user_obj.last_updated_at = datetime.datetime.now()
                        student_profile_obj.save()

                    except:
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    message = 'success'
                    student_registration_no = request.POST.get('student_registration_number')
                    student_fname = request.POST.get('student_fname')
                    student_lname = request.POST.get('student_lname')
                    studentDob = request.POST.get('student_dob')
                    if(len(str(studentDob)) != 0):
                        import datetime
                        studentDob = datetime.datetime.strptime(str(studentDob), '%m-%d-%Y').strftime('%Y-%m-%d')
                    else:
                        studentDob = None

                    studentGender = request.POST.get('student_gender')
                    student_parent_name = request.POST.get('student_parent_name')
                    student_parentRelation = request.POST.get('student_parent_relation')
                    studentHobbies = request.POST.getlist('student_hobbies[]')

                    studentEmail = request.POST.get('student_email')
                    studentContact = request.POST.get('student_contact')
                    student_parentContact = request.POST.get('student_parent_contact')

                    studentAddress = request.POST.get('student_address')
                    branchPinCode = request.POST.get('branchPinCode')
                    studentCity = request.POST.get('studentCity')
                    studentState = request.POST.get('student_state')
                    branchCode = request.POST.get('branchCode')

                    student_class = request.POST.get('student_class')
                    student_section = request.POST.get('student_section')
                    student_subject = request.POST.getlist('student_subject[]')

                    profileImage = request.FILES.get('profile_image')

                    list1 = []
                    for i in student_subject[0].split(','):
                        list1.append(int(i))

                    try:
                        student_profile_obj = student_profile.objects.get(id=int(id))

                        student_user_obj = student_user.objects.get(id=int(student_profile_obj.student_FK.id))
                        student_user_obj.student_first_name = student_fname
                        student_user_obj.student_last_name = student_lname
                        student_user_obj.student_registration_number = student_registration_no
                        student_user_obj.student_email = studentEmail
                        student_user_obj.student_contact = studentContact
                        student_user_obj.last_updated_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}"
                        student_user_obj.last_updated_at = datetime.datetime.now()

                        if(profileImage != None):
                            print('none data')
                            student_user_obj.profile_image = profileImage
                        student_user_obj.save()

                        # branchObj = branch.objects.get(id = int(branchCode))
                        classObj = class_master.objects.get(id = int(student_class))
                        sectionObj = section_master.objects.get(id = int(student_section))
                        student_profile_obj.student_FK = student_user_obj
                        # student_profile_obj.branch_FK = branchObj
                        student_profile_obj.student_DOB = studentDob
                        student_profile_obj.student_gender = studentGender
                        student_profile_obj.student_fathers_name = student_parent_name
                        student_profile_obj.student_parent_relation = student_parentRelation
                        student_profile_obj.student_hobbies = studentHobbies
                        student_profile_obj.student_parent_contact = student_parentContact
                        student_profile_obj.student_address = studentAddress
                        student_profile_obj.student_pinCode = branchPinCode
                        student_profile_obj.student_city = studentCity
                        student_profile_obj.student_state = studentState
                        student_profile_obj.class_fk = classObj
                        student_profile_obj.section_fk = sectionObj
                        student_profile_obj.subject_fk = list1
                        student_profile_obj.last_updated_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}"
                        student_profile_obj.last_updated_at = datetime.datetime.now()
                        student_profile_obj.save()

                        parent_user_obj = parent_user.objects.get(student_fk = student_profile_obj)
                        parent_user_obj.student_fk = student_profile_obj
                        parent_user_obj.parent_name = student_parent_name
                        parent_user_obj.parent_contact = student_parentContact
                        parent_user_obj.last_updated_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}"
                        parent_user_obj.last_updated_at = datetime.datetime.now()
                        student_profile_obj.save()

                    except:
                        message = 'failed'

                    return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')

        

# #####################################################################################################################
# delete branch view
# #####################################################################################################################
# @login_required(login_url='/')
def delete_student(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Delete_Student'] == True):
                    student_profileObj = student_profile.objects.get(id=int(id))
                    student_userObj = student_user.objects.get(id=int(student_profileObj.student_FK.id))
                    student_userObj.delete()
                    return redirect('student_list')
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Delete_Student'] == True):
                    student_profileObj = student_profile.objects.get(id=int(id))
                    student_userObj = student_user.objects.get(id=int(student_profileObj.student_FK.id))
                    student_userObj.delete()
                    return redirect('student_list')

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Delete_Student'] == True):
                    student_profileObj = student_profile.objects.get(id=int(id))
                    student_userObj = student_user.objects.get(id=int(student_profileObj.student_FK.id))
                    student_userObj.delete()
                    return redirect('student_list')

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
        


# #####################################################################################################################
# delete branch view
# #####################################################################################################################
# @login_required(login_url='/')
def change_student_status(request):
    if request.method == 'POST':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    message = 'success'
                    studentId = request.POST['studentId']
                    data = request.POST['data']

                    if(data == 'true'):
                        data = '1'
                    if(data == 'false'):
                        data = '2'

                    try:
                        student_profileObj = student_profile.objects.get(id=int(studentId))
                        student_userObj = student_user.objects.get(id=int(student_profileObj.student_FK.id))

                        student_userObj.active_status = data
                        student_userObj.save()

                    except:
                        message = 'failed'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    message = 'success'
                    studentId = request.POST['studentId']
                    data = request.POST['data']

                    if(data == 'true'):
                        data = '1'
                    if(data == 'false'):
                        data = '2'

                    try:
                        student_profileObj = student_profile.objects.get(id=int(studentId))
                        student_userObj = student_user.objects.get(id=int(student_profileObj.student_FK.id))

                        student_userObj.active_status = data
                        student_userObj.save()

                    except:
                        message = 'failed'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Edit_Student'] == True):
                    message = 'success'
                    studentId = request.POST['studentId']
                    data = request.POST['data']

                    if(data == 'true'):
                        data = '1'
                    if(data == 'false'):
                        data = '2'

                    try:
                        student_profileObj = student_profile.objects.get(id=int(studentId))
                        student_userObj = student_user.objects.get(id=int(student_profileObj.student_FK.id))

                        student_userObj.active_status = data
                        student_userObj.save()

                    except:
                        message = 'failed'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')



        

# #####################################################################################################################
# check branch for existing student view
# #####################################################################################################################
# @login_required(login_url='/')
def student_checkBranch(request):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Student_List'] == True):
                    message = 'not-exist'
                    searchStr = request.GET['branchCode']
                    branchObj = branch.objects.get(id = int(searchStr))
                    try:
                        if(student_profile.objects.filter(branch_FK = branchObj)):
                            message = 'student-branch-exist'
                    except:
                        message = 'not-exist'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Student_List'] == True):
                    message = 'not-exist'
                    searchStr = request.GET['branchCode']
                    branchObj = branch.objects.get(id = int(searchStr))
                    try:
                        if(student_profile.objects.filter(branch_FK = branchObj)):
                            message = 'student-branch-exist'
                    except:
                        message = 'not-exist'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Student_List'] == True):
                    message = 'not-exist'
                    searchStr = request.GET['branchCode']
                    branchObj = branch.objects.get(id = int(searchStr))
                    try:
                        if(student_profile.objects.filter(branch_FK = branchObj)):
                            message = 'student-branch-exist'
                    except:
                        message = 'not-exist'
                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')


        


# #####################################################################################################################
# student fields check view
# #####################################################################################################################
# @login_required(login_url='/')
def student_field_check(request):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Student'] == True):
                    message = 'not-exist'
                    fieldType = request.GET['fieldType']
                    searchString = request.GET['searchString']

                    if(fieldType == 'student_registration_no'):
                        studentObj = student_user.objects.filter(student_registration_number=searchString)
                        if(studentObj):
                            message = 'student-registration-exist'

                    elif(fieldType == 'student_email'):
                        studentObj = student_user.objects.filter(student_email=searchString)
                        if(studentObj):
                            message = 'student-email-exist'

                    elif(fieldType == 'student_contact'):
                        studentObj = student_user.objects.filter(student_contact=searchString)
                        if(studentObj):
                            message = 'student-contact-exist'

                    elif(fieldType == 'student_parent_contact'):
                        studentObj = student_profile.objects.filter(student_parent_contact=searchString)
                        if(studentObj):
                            message = 'student-parent-contact-exist'

                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Student'] == True):
                    message = 'not-exist'
                    fieldType = request.GET['fieldType']
                    searchString = request.GET['searchString']

                    if(fieldType == 'student_registration_no'):
                        studentObj = student_user.objects.filter(student_registration_number=searchString)
                        if(studentObj):
                            message = 'student-registration-exist'

                    elif(fieldType == 'student_email'):
                        studentObj = student_user.objects.filter(student_email=searchString)
                        if(studentObj):
                            message = 'student-email-exist'

                    elif(fieldType == 'student_contact'):
                        studentObj = student_user.objects.filter(student_contact=searchString)
                        if(studentObj):
                            message = 'student-contact-exist'

                    elif(fieldType == 'student_parent_contact'):
                        studentObj = student_profile.objects.filter(student_parent_contact=searchString)
                        if(studentObj):
                            message = 'student-parent-contact-exist'

                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Student'] == True):
                    message = 'not-exist'
                    fieldType = request.GET['fieldType']
                    searchString = request.GET['searchString']

                    if(fieldType == 'student_registration_no'):
                        studentObj = student_user.objects.filter(student_registration_number=searchString)
                        if(studentObj):
                            message = 'student-registration-exist'

                    elif(fieldType == 'student_email'):
                        studentObj = student_user.objects.filter(student_email=searchString)
                        if(studentObj):
                            message = 'student-email-exist'

                    elif(fieldType == 'student_contact'):
                        studentObj = student_user.objects.filter(student_contact=searchString)
                        if(studentObj):
                            message = 'student-contact-exist'

                    elif(fieldType == 'student_parent_contact'):
                        studentObj = student_profile.objects.filter(student_parent_contact=searchString)
                        if(studentObj):
                            message = 'student-parent-contact-exist'

                    return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')






        