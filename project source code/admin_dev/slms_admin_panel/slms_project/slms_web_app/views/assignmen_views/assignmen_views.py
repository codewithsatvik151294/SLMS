from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required

from slms_web_app.models.assignment_models import assignment_model
from ...models.master_models import Authority_master, SubAuthority_master, section_master, subject_master,user_designation_master,year_master,question_type_master,exam_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import class_master,branch,principal_profile,schoolAdmin_profile,director_profile
from ...models.exam_models import exam_model
from ...models.paper_models import question_paper_model
from ..utils_views import get_auth_dict,get_Subauth_dict
# #####################################################################################################################
# assignment_list view
# #####################################################################################################################
# @login_required(login_url='/')
def assignment_list(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Assignment_List'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    assignmentObj = assignment_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/assignment-management/assignment-list.html',{'branchObj':branchObj,'assignmentObj':assignmentObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Assignment_List'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    assignmentObj = assignment_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/assignment-management/assignment-list.html',{'branchObj':branchObj,'assignmentObj':assignmentObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Assignment_List'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    assignmentObj = assignment_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/assignment-management/assignment-list.html',{'branchObj':branchObj,'assignmentObj':assignmentObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# add_assignment view
# #####################################################################################################################
# @login_required(login_url='/')
def add_assignment(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Add_Assignment'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    questionTypeObj = question_type_master.objects.all()
                    yearObj = year_master.objects.all()
                    return render(request,'admin_template/assignment-management/add-assignment.html',{'classObj':classObj,'branchObj':branchObj,'questionTypeObj':questionTypeObj,'yearObj':yearObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Assignment'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    questionTypeObj = question_type_master.objects.all()
                    yearObj = year_master.objects.all()
                    return render(request,'admin_template/assignment-management/add-assignment.html',{'classObj':classObj,'branchObj':branchObj,'questionTypeObj':questionTypeObj,'yearObj':yearObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Assignment'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    questionTypeObj = question_type_master.objects.all()
                    yearObj = year_master.objects.all()
                    return render(request,'admin_template/assignment-management/add-assignment.html',{'classObj':classObj,'branchObj':branchObj,'questionTypeObj':questionTypeObj,'yearObj':yearObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
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
                if(sub_auth_dict['Add_Assignment'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    assignmentName = request.POST['assignment_name']
                    classID = request.POST['classID']
                    sectionID = request.POST['sectionID']
                    subjectID = request.POST['subjectID']
                    totalMark = request.POST['total_mark']
                    passingMark = request.POST['passing_mark']
                    startAt = request.POST['start_at']
                    endAt = request.POST['end_at']
                    questionType = request.POST['question_type[]']
                    guideline = request.POST['guidelines']
                    questions = request.POST['question_array[]']


                    message = 'success'
                    counter = 100
                    try:
                        assignObj = assignment_model.objects.latest('assignment_ID')
                        counter = int(assignObj.assignment_ID.split('ASSIGNMENT-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classID))
                        sectionObj = section_master.objects.get(id=int(sectionID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        
                        assignmentObj = assignment_model(assignment_ID=f"ASSIGNMENT-{counter}",
                                                        assignment_name=assignmentName,
                                                        branch_FK=branchObj,
                                                        class_fk=classObj,
                                                        section_fk=sectionObj,
                                                        subject_fk=subjectObj,
                                                        total_marks=totalMark,
                                                        passing_marks=passingMark,
                                                        starts_at=startAt,
                                                        ends_at=endAt,
                                                        questionType=questionType,
                                                        question_array=questions,
                                                        guidelines = guideline,
                                                        created_by = f"Director - {directorObj.director_FK.director_name}")
                        assignmentObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Assignment'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    assignmentName = request.POST['assignment_name']
                    classID = request.POST['classID']
                    sectionID = request.POST['sectionID']
                    subjectID = request.POST['subjectID']
                    totalMark = request.POST['total_mark']
                    passingMark = request.POST['passing_mark']
                    startAt = request.POST['start_at']
                    endAt = request.POST['end_at']
                    questionType = request.POST['question_type[]']
                    guideline = request.POST['guidelines']
                    questions = request.POST['question_array[]']


                    message = 'success'
                    counter = 100
                    try:
                        assignObj = assignment_model.objects.latest('assignment_ID')
                        counter = int(assignObj.assignment_ID.split('ASSIGNMENT-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classID))
                        sectionObj = section_master.objects.get(id=int(sectionID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        
                        assignmentObj = assignment_model(assignment_ID=f"ASSIGNMENT-{counter}",
                                                        assignment_name=assignmentName,
                                                        branch_FK=branchObj,
                                                        class_fk=classObj,
                                                        section_fk=sectionObj,
                                                        subject_fk=subjectObj,
                                                        total_marks=totalMark,
                                                        passing_marks=passingMark,
                                                        starts_at=startAt,
                                                        ends_at=endAt,
                                                        questionType=questionType,
                                                        question_array=questions,
                                                        guidelines = guideline,
                                                        created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                        assignmentObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Assignment'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    assignmentName = request.POST['assignment_name']
                    classID = request.POST['classID']
                    sectionID = request.POST['sectionID']
                    subjectID = request.POST['subjectID']
                    totalMark = request.POST['total_mark']
                    passingMark = request.POST['passing_mark']
                    startAt = request.POST['start_at']
                    endAt = request.POST['end_at']
                    questionType = request.POST['question_type[]']
                    guideline = request.POST['guidelines']
                    questions = request.POST['question_array[]']


                    message = 'success'
                    counter = 100
                    try:
                        assignObj = assignment_model.objects.latest('assignment_ID')
                        counter = int(assignObj.assignment_ID.split('ASSIGNMENT-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classID))
                        sectionObj = section_master.objects.get(id=int(sectionID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        
                        assignmentObj = assignment_model(assignment_ID=f"ASSIGNMENT-{counter}",
                                                        assignment_name=assignmentName,
                                                        branch_FK=branchObj,
                                                        class_fk=classObj,
                                                        section_fk=sectionObj,
                                                        subject_fk=subjectObj,
                                                        total_marks=totalMark,
                                                        passing_marks=passingMark,
                                                        starts_at=startAt,
                                                        ends_at=endAt,
                                                        questionType=questionType,
                                                        question_array=questions,
                                                        guidelines = guideline,
                                                        created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")
                        assignmentObj.save()
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
def assignment_status_change(request,id):
    if request.method == 'GET':
        assignmentObj = assignment_model.objects.get(id=int(id))

        if(assignmentObj.published_status == True):
            assignmentObj.published_status = False
        else:
            assignmentObj.published_status = True
        assignmentObj.save()
        return redirect('assignment_list')


# #####################################################################################################################
# get exam papers view
# #####################################################################################################################
# @login_required(login_url='/')
def get_exam_papers(request):
    if request.method == 'GET':
        classID = request.GET['classID']
        paperList = []
        if(question_paper_model.objects.filter(class_fk = class_master.objects.get(id=int(classID)))):
            counter = 1
            for i in question_paper_model.objects.filter(class_fk = class_master.objects.get(id=int(classID))):
                context = {}
                context['id'] = i.id
                context['paper_id'] = i.paper_ID.title()
                context['paper_name'] = i.paper_name.title()
                context['subject'] = i.subject_fk.subject_name.title()
                context['year'] = i.year_fk.year_name.title()
                context['total_marks'] = i.total_marks
                context['counter'] = counter
                counter = counter + 1
                paperList.append(context)
        return  JsonResponse({'paperList':paperList})


# #####################################################################################################################
# fetch specific paper view
# #####################################################################################################################
# from bs4 import BeautifulSoup
# @login_required(login_url='/')
def view_question(request,id):
    if request.method == 'GET':
        questionList = []
        question_dict = {}
        try:
            questionObj = question.objects.get(id=int(id))

            question_dict['id'] = questionObj.id
            question_dict['class_name'] = questionObj.class_fk.class_name
            question_dict['subject_name'] = questionObj.subject_fk.subject_name.title()
            question_dict['topic_name'] = questionObj.topic_name.title()
            question_dict['year_name'] = questionObj.year_fk.year_name
            question_dict['question_type'] = questionObj.question_type_fk.questionType_name.title()
            question_dict['question_sub_type'] = questionObj.question_subtype_type.title()
            question_dict['difficulty'] = questionObj.difficulty_type
            question_dict['correct_mark'] = questionObj.correct_mark
            question_dict['negative_mark'] = questionObj.negative_mark
            question_dict['question_text'] = questionObj.question_text
            

            if(int(questionObj.option_count) > 1):
                question_dict['option_count'] = int(questionObj.option_count)
                data = questionObj.option_array
                context = []
                for i in eval(data):
                    question_dict['option_array'] = eval(i)

                # ['[{"option1":"216","status":"false"},{"option2":"48","status":"true"},{"option3":"8","status":"false"},{"option4":"None of the above","status":"false"}]']
            else:
                question_dict['option_count'] = int(questionObj.option_count)
                question_dict['option_array'] = {}
        except:
            topicsList = []

        return  JsonResponse({'question_dict':question_dict})

    
# #####################################################################################################################
# edit specific paper
# #####################################################################################################################
# @login_required(login_url='/')
def edit_question(request,id):
    if request.method == 'GET':
        return render(request,'admin_template/paper-bank/edit-paper.html')


# #####################################################################################################################
# delete assignment view
# #####################################################################################################################
# @login_required(login_url='/')
def delete_assignment(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Delete_Assignment'] == True):
                    try:
                        assignmentObj = assignment_model.objects.get(id=int(id))
                        assignmentObj.delete()
                        return redirect('assignment_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Delete_Assignment'] == True):
                    try:
                        assignmentObj = assignment_model.objects.get(id=int(id))
                        assignmentObj.delete()
                        return redirect('assignment_list')
                    except:
                        return render(request,'403.html')

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Delete_Assignment'] == True):
                    try:
                        assignmentObj = assignment_model.objects.get(id=int(id))
                        assignmentObj.delete()
                        return redirect('assignment_list')
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
        year_filter = request.GET['year_filter']
        print('year_filter >>> ',year_filter)
        data_list = []
        yearObj = year_master.objects.get(id=int(year_filter))
        if(question.objects.filter(year_fk = yearObj)):
            for i in question.objects.filter(year_fk = yearObj):
                context = {}
                context['id'] = i.id
                context['question_text'] = i.question_text
                context['question_type'] = i.question_type_fk.questionType_name.title()
                context['difficulty'] = i.difficulty_type
                context['correct_mark'] = i.correct_mark
                context['subject_name'] = i.subject_fk.subject_name.title()
                context['topic_name'] = i.topic_name.title()
                context['year_name'] = i.year_fk.year_name
                data_list.append(context)
        
        return JsonResponse({'data_list':data_list})




# #####################################################################################################################
# fetch questions
# #####################################################################################################################
# @login_required(login_url='/')
def fetch_questions(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Assignment_List'] == True):
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
                if(sub_auth_dict['Assignment_List'] == True):
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
                if(sub_auth_dict['Assignment_List'] == True):
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



