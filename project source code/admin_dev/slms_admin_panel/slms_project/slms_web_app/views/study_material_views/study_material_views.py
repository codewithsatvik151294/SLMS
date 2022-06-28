from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required

from slms_web_app.models.assignment_models import assignment_model
from ...models.master_models import Authority_master, SubAuthority_master, file_type_master, section_master, subject_master,user_designation_master,year_master,question_type_master,exam_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import class_master,branch,schoolAdmin_profile,director_profile,principal_profile
from ...models.exam_models import exam_model
from ...models.paper_models import question_paper_model
from ...models.studey_material_models import study_material
from ..utils_views import get_auth_dict,get_Subauth_dict
import datetime

# #####################################################################################################################
# Study_Material_List view
# #####################################################################################################################
# @login_required(login_url='/')
def study_material_list(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Study_Material_List'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    study_materialObj = study_material.objects.filter(branch_fk_id=branchObj).order_by('-id')
                    return render(request,'admin_template/study-material/material-list.html',{'branchObj':branchObj,'study_materialObj':study_materialObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Study_Material_List'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    study_materialObj = study_material.objects.filter(branch_fk_id=branchObj).order_by('-id')
                    return render(request,'admin_template/study-material/material-list.html',{'branchObj':branchObj,'study_materialObj':study_materialObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Study_Material_List'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    study_materialObj = study_material.objects.filter(branch_fk_id=branchObj).order_by('-id')
                    return render(request,'admin_template/study-material/material-list.html',{'branchObj':branchObj,'study_materialObj':study_materialObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# add_study_material view
# #####################################################################################################################
# @login_required(login_url='/')
def add_study_material(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Add_Study_Material'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    return render(request,'admin_template/study-material/add-material.html',{'classObj':classObj,'branchObj':branchObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Study_Material'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    return render(request,'admin_template/study-material/add-material.html',{'classObj':classObj,'branchObj':branchObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Study_Material'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    return render(request,'admin_template/study-material/add-material.html',{'classObj':classObj,'branchObj':branchObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
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
                if(sub_auth_dict['Add_Study_Material'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classs_id = request.POST['classs_id']
                    subject_id = request.POST['subject_id']
                    topic = request.POST['topic']
                    file_type_id = request.POST['file_type_id']
                    file_content = request.FILES.get('content')


                    message = 'success'
                    counter = 100
                    try:
                        study_materialObj = study_material.objects.latest('study_material_ID')
                        counter = int(study_materialObj.study_material_ID.split('SM-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classs_id))
                        subjectObj = subject_master.objects.get(id=int(subject_id))
                        fileTypeObj = file_type_master.objects.get(id=int(file_type_id))
                        
                        study_materialObj = study_material(study_material_ID=f"SM-{counter}",
                                                        branch_fk=branchObj,
                                                        class_fk=classObj,
                                                        subject_fk=subjectObj,
                                                        topic=topic,
                                                        file_type_fk=fileTypeObj,
                                                        content=file_content,
                                                        created_by = f"Director - {directorObj.director_FK.director_name}")
                        study_materialObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Study_Material'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classs_id = request.POST['classs_id']
                    subject_id = request.POST['subject_id']
                    topic = request.POST['topic']
                    file_type_id = request.POST['file_type_id']
                    file_content = request.FILES.get('content')


                    message = 'success'
                    counter = 100
                    try:
                        study_materialObj = study_material.objects.latest('study_material_ID')
                        counter = int(study_materialObj.study_material_ID.split('SM-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classs_id))
                        subjectObj = subject_master.objects.get(id=int(subject_id))
                        fileTypeObj = file_type_master.objects.get(id=int(file_type_id))
                        
                        study_materialObj = study_material(study_material_ID=f"SM-{counter}",
                                                        branch_fk=branchObj,
                                                        class_fk=classObj,
                                                        subject_fk=subjectObj,
                                                        topic=topic,
                                                        file_type_fk=fileTypeObj,
                                                        content=file_content,
                                                        created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                        study_materialObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Study_Material'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classs_id = request.POST['classs_id']
                    subject_id = request.POST['subject_id']
                    topic = request.POST['topic']
                    file_type_id = request.POST['file_type_id']
                    file_content = request.FILES.get('content')


                    message = 'success'
                    counter = 100
                    try:
                        study_materialObj = study_material.objects.latest('study_material_ID')
                        counter = int(study_materialObj.study_material_ID.split('SM-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classs_id))
                        subjectObj = subject_master.objects.get(id=int(subject_id))
                        fileTypeObj = file_type_master.objects.get(id=int(file_type_id))
                        
                        study_materialObj = study_material(study_material_ID=f"SM-{counter}",
                                                        branch_fk=branchObj,
                                                        class_fk=classObj,
                                                        subject_fk=subjectObj,
                                                        topic=topic,
                                                        file_type_fk=fileTypeObj,
                                                        content=file_content,
                                                        created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")
                        study_materialObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')



# #####################################################################################################################
# check assignment name view
# #####################################################################################################################
# @login_required(login_url='/')
def check_assignment(request):
    if request.method == 'GET':
        message = 'not-exisit'
        searchString = request.GET['search_string']
        if(assignment_model.objects.filter(assignment_name = searchString.lower())):
            message = 'exist'

        return  JsonResponse({'message':message})


# #####################################################################################################################
# change assignment publish status view
# #####################################################################################################################
# @login_required(login_url='/')
def study_material_status_change(request,id):
    if request.method == 'GET':
        study_materialObj = study_material.objects.get(id=int(id))

        if(study_materialObj.published_status == True):
            study_materialObj.published_status = False
        else:
            study_materialObj.published_status = True
        study_materialObj.save()
        return redirect('study_material_list')


# #####################################################################################################################
# fetch specific study material view
# #####################################################################################################################
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
# @login_required(login_url='/')
def view_study_material(request,id):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    try:
                        study_materialObj = study_material.objects.get(id=int(id),branch_fk_id=branchObj)
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/study-material/material-detail.html',{'study_materialObj':study_materialObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    try:
                        study_materialObj = study_material.objects.get(id=int(id),branch_fk_id=branchObj)
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/study-material/material-detail.html',{'study_materialObj':study_materialObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_login']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    try:
                        study_materialObj = study_material.objects.get(id=int(id),branch_fk_id=branchObj)
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/study-material/material-detail.html',{'study_materialObj':study_materialObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')

    
# #####################################################################################################################
# edit specific study material
# #####################################################################################################################
@xframe_options_exempt
# @login_required(login_url='/')
def edit_study_material(request,id):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    try:
                        study_materialObj = study_material.objects.get(id=int(id),branch_fk_id=branchObj)
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/study-material/edit-material.html',{'study_materialObj':study_materialObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    try:
                        study_materialObj = study_material.objects.get(id=int(id),branch_fk_id=branchObj)
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/study-material/edit-material.html',{'study_materialObj':study_materialObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_login']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    fileTypeObj = file_type_master.objects.all()
                    try:
                        study_materialObj = study_material.objects.get(id=int(id),branch_fk_id=branchObj)
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/study-material/edit-material.html',{'study_materialObj':study_materialObj,'fileTypeObj':fileTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

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
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    file_type_id = request.POST['file_type_id']
                    file_content = request.FILES.get('content')

                    try:
                        message = 'success'
                        study_materialObj = study_material.objects.get(id=int(id))
                        fileTypeObj = file_type_master.objects.get(id=int(file_type_id))

                        study_materialObj.file_type_fk=fileTypeObj
                        study_materialObj.content=file_content
                        study_materialObj.last_updated_by = f"Director - {directorObj.director_FK.director_name}"
                        study_materialObj.last_updated_at = datetime.datetime.now()
                        study_materialObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    file_type_id = request.POST['file_type_id']
                    file_content = request.FILES.get('content')

                    try:
                        message = 'success'
                        study_materialObj = study_material.objects.get(id=int(id))
                        fileTypeObj = file_type_master.objects.get(id=int(file_type_id))

                        study_materialObj.file_type_fk=fileTypeObj
                        study_materialObj.content=file_content
                        study_materialObj.last_updated_by = f"Principal - {directorObj.principal_FK.principal_name}"
                        study_materialObj.last_updated_at = datetime.datetime.now()
                        study_materialObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Edit_Study_Material'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_login']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    file_type_id = request.POST['file_type_id']
                    file_content = request.FILES.get('content')

                    try:
                        message = 'success'
                        study_materialObj = study_material.objects.get(id=int(id))
                        fileTypeObj = file_type_master.objects.get(id=int(file_type_id))

                        study_materialObj.file_type_fk=fileTypeObj
                        study_materialObj.content=file_content
                        study_materialObj.last_updated_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}"
                        study_materialObj.last_updated_at = datetime.datetime.now()
                        study_materialObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')

# #####################################################################################################################
# delete assignment view
# #####################################################################################################################
# @login_required(login_url='/')
def delete_study_material(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                if(sub_auth_dict['Delete_Study_Material'] == True):
                    try:
                        assignmentObj = study_material.objects.get(id=int(id))
                        assignmentObj.delete()
                        return redirect('study_material_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Delete_Study_Material'] == True):
                    try:
                        assignmentObj = study_material.objects.get(id=int(id))
                        assignmentObj.delete()
                        return redirect('study_material_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Delete_Study_Material'] == True):
                    try:
                        assignmentObj = study_material.objects.get(id=int(id))
                        assignmentObj.delete()
                        return redirect('study_material_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')

# #####################################################################################################################
# filter paper
# #####################################################################################################################
# @login_required(login_url='/')
def filter_question(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Study_Material_List'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    class_id = request.GET['class_id']
                    subject_id = request.GET['subject_id']
                    qType_list = request.GET.getlist('qType[]')

                    data_list = []
                    classObj = class_master.objects.get(id=int(class_id))
                    subjectObj = subject_master.objects.get(id=int(subject_id))

                    if(len(qType_list) == 2):
                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj)):
                            for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj):
                                context = {}
                                context['id'] = i.id
                                context['question_text'] = i.question_text
                                context['question_type'] = i.question_type_fk.questionType_name.title()
                                context['question_sub_type'] = i.question_subtype_type.title()
                                if(i.difficulty_type == '1'):
                                    context['difficulty'] = 'Easy'
                                elif(i.difficulty_type == '2'):
                                    context['difficulty'] = 'Moderate'
                                elif(i.difficulty_type == '3'):
                                    context['difficulty'] = 'Hard'
                                    
                                context['correct_mark'] = i.correct_mark
                                context['subject_name'] = i.subject_fk.subject_name.title()
                                context['topic_name'] = i.topic_name.title()
                                context['year_name'] = i.year_fk.year_name
                                data_list.append(context)
                    else:
                        questionType = ''
                        if(qType_list[0] == '1'):
                            questionType = 'objective'
                        elif(qType_list[0] == '2'):
                            questionType = 'subjective'
                        elif(qType_list[0] == '3'):
                            questionType = 'multiple choice objective'
                        elif(qType_list[0] == '4'):
                            questionType = 'diagram upload'
                        
                        qTypeObj = question_type_master.objects.get(questionType_name=questionType)

                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj)):
                            for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj):
                                context = {}
                                context['id'] = i.id
                                context['question_text'] = i.question_text
                                context['question_type'] = i.question_type_fk.questionType_name.title()
                                context['question_sub_type'] = i.question_subtype_type.title()
                                if(i.difficulty_type == '1'):
                                    context['difficulty'] = 'Easy'
                                elif(i.difficulty_type == '2'):
                                    context['difficulty'] = 'Moderate'
                                elif(i.difficulty_type == '3'):
                                    context['difficulty'] = 'Hard'
                                    
                                context['correct_mark'] = i.correct_mark
                                context['subject_name'] = i.subject_fk.subject_name.title()
                                context['topic_name'] = i.topic_name.title()
                                context['year_name'] = i.year_fk.year_name
                                data_list.append(context)
                    
                    return JsonResponse({'data_list':data_list})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Study_Material_List'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    class_id = request.GET['class_id']
                    subject_id = request.GET['subject_id']
                    qType_list = request.GET.getlist('qType[]')

                    data_list = []
                    classObj = class_master.objects.get(id=int(class_id))
                    subjectObj = subject_master.objects.get(id=int(subject_id))

                    if(len(qType_list) == 2):
                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj)):
                            for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj):
                                context = {}
                                context['id'] = i.id
                                context['question_text'] = i.question_text
                                context['question_type'] = i.question_type_fk.questionType_name.title()
                                context['question_sub_type'] = i.question_subtype_type.title()
                                if(i.difficulty_type == '1'):
                                    context['difficulty'] = 'Easy'
                                elif(i.difficulty_type == '2'):
                                    context['difficulty'] = 'Moderate'
                                elif(i.difficulty_type == '3'):
                                    context['difficulty'] = 'Hard'
                                    
                                context['correct_mark'] = i.correct_mark
                                context['subject_name'] = i.subject_fk.subject_name.title()
                                context['topic_name'] = i.topic_name.title()
                                context['year_name'] = i.year_fk.year_name
                                data_list.append(context)
                    else:
                        questionType = ''
                        if(qType_list[0] == '1'):
                            questionType = 'objective'
                        elif(qType_list[0] == '2'):
                            questionType = 'subjective'
                        elif(qType_list[0] == '3'):
                            questionType = 'multiple choice objective'
                        elif(qType_list[0] == '4'):
                            questionType = 'diagram upload'
                        
                        qTypeObj = question_type_master.objects.get(questionType_name=questionType)

                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj)):
                            for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj):
                                context = {}
                                context['id'] = i.id
                                context['question_text'] = i.question_text
                                context['question_type'] = i.question_type_fk.questionType_name.title()
                                context['question_sub_type'] = i.question_subtype_type.title()
                                if(i.difficulty_type == '1'):
                                    context['difficulty'] = 'Easy'
                                elif(i.difficulty_type == '2'):
                                    context['difficulty'] = 'Moderate'
                                elif(i.difficulty_type == '3'):
                                    context['difficulty'] = 'Hard'
                                    
                                context['correct_mark'] = i.correct_mark
                                context['subject_name'] = i.subject_fk.subject_name.title()
                                context['topic_name'] = i.topic_name.title()
                                context['year_name'] = i.year_fk.year_name
                                data_list.append(context)
                    
                    return JsonResponse({'data_list':data_list})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Study_Material_List'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    class_id = request.GET['class_id']
                    subject_id = request.GET['subject_id']
                    qType_list = request.GET.getlist('qType[]')

                    data_list = []
                    classObj = class_master.objects.get(id=int(class_id))
                    subjectObj = subject_master.objects.get(id=int(subject_id))

                    if(len(qType_list) == 2):
                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj)):
                            for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj):
                                context = {}
                                context['id'] = i.id
                                context['question_text'] = i.question_text
                                context['question_type'] = i.question_type_fk.questionType_name.title()
                                context['question_sub_type'] = i.question_subtype_type.title()
                                if(i.difficulty_type == '1'):
                                    context['difficulty'] = 'Easy'
                                elif(i.difficulty_type == '2'):
                                    context['difficulty'] = 'Moderate'
                                elif(i.difficulty_type == '3'):
                                    context['difficulty'] = 'Hard'
                                    
                                context['correct_mark'] = i.correct_mark
                                context['subject_name'] = i.subject_fk.subject_name.title()
                                context['topic_name'] = i.topic_name.title()
                                context['year_name'] = i.year_fk.year_name
                                data_list.append(context)
                    else:
                        questionType = ''
                        if(qType_list[0] == '1'):
                            questionType = 'objective'
                        elif(qType_list[0] == '2'):
                            questionType = 'subjective'
                        elif(qType_list[0] == '3'):
                            questionType = 'multiple choice objective'
                        elif(qType_list[0] == '4'):
                            questionType = 'diagram upload'
                        
                        qTypeObj = question_type_master.objects.get(questionType_name=questionType)

                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj)):
                            for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj):
                                context = {}
                                context['id'] = i.id
                                context['question_text'] = i.question_text
                                context['question_type'] = i.question_type_fk.questionType_name.title()
                                context['question_sub_type'] = i.question_subtype_type.title()
                                if(i.difficulty_type == '1'):
                                    context['difficulty'] = 'Easy'
                                elif(i.difficulty_type == '2'):
                                    context['difficulty'] = 'Moderate'
                                elif(i.difficulty_type == '3'):
                                    context['difficulty'] = 'Hard'
                                    
                                context['correct_mark'] = i.correct_mark
                                context['subject_name'] = i.subject_fk.subject_name.title()
                                context['topic_name'] = i.topic_name.title()
                                context['year_name'] = i.year_fk.year_name
                                data_list.append(context)
                    
                    return JsonResponse({'data_list':data_list})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')




# #####################################################################################################################
# fetch questions
# #####################################################################################################################
# @login_required(login_url='/')
def fetch_questions(request):
    if request.method == 'GET':
        class_id = request.GET['class_id']
        subject_id = request.GET['subject_id']
        qType_list = request.GET.getlist('qType[]')

        print('qType_list >>>> ',qType_list)
        # exit()

        data_list = []
        classObj = class_master.objects.get(id=int(class_id))
        subjectObj = subject_master.objects.get(id=int(subject_id))

        for j in qType_list:
            qTypeObj = question_type_master.objects.get(id=int(j))
            for i in question.objects.filter(class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj):
                context = {}
                context['id'] = i.id
                context['question_text'] = i.question_text
                context['question_type'] = i.question_type_fk.questionType_name.title()
                context['question_sub_type'] = i.question_subtype_type.title()
                if(i.difficulty_type == '1'):
                    context['difficulty'] = 'Easy'
                elif(i.difficulty_type == '2'):
                    context['difficulty'] = 'Moderate'
                elif(i.difficulty_type == '3'):
                    context['difficulty'] = 'Hard'
                    
                context['correct_mark'] = i.correct_mark
                context['subject_name'] = i.subject_fk.subject_name.title()
                context['topic_name'] = i.topic_name.title()
                context['year_name'] = i.year_fk.year_name
                data_list.append(context)
        
        return JsonResponse({'data_list':data_list})


# #####################################################################################################################
# get section questions
# #####################################################################################################################
# @login_required(login_url='/')
def get_questions(request):
    if request.method == 'GET':
        question_array = request.GET.getlist('question_array[]')
        print('question_array >>> ',question_array)
        question_list = []
        for i in question_array:
            questionObj = question.objects.get(id=int(i))
            context = {}
            context['id'] = questionObj.id
            context['question_text'] = questionObj.question_text
            question_list.append(context)
        
        return JsonResponse({'question_list':question_list})



