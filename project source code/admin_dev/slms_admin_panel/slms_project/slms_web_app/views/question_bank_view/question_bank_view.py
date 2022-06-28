from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.master_models import Authority_master, SubAuthority_master, subject_master,user_designation_master,year_master,question_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import class_master,topic_master,branch,parent_user,student_profile,student_user,director_profile,principal_profile,schoolAdmin_profile
from django.core import serializers
from ..utils_views import get_auth_dict,get_Subauth_dict
import datetime
# #####################################################################################################################
# question_list view
# #####################################################################################################################
# @login_required(login_url='/')
def question_list(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Question_List'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    questionObj = question.objects.filter(branch_fk=branchObj).order_by('-id')
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    questionTypeObj = question_type_master.objects.all()
                    return render(request,'admin_template/question-bank/question-list.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'questionTypeObj':questionTypeObj,'questionObj':questionObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Question_List'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    questionObj = question.objects.filter(branch_fk=branchObj).order_by('-id')
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    questionTypeObj = question_type_master.objects.all()
                    return render(request,'admin_template/question-bank/question-list.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'questionTypeObj':questionTypeObj,'questionObj':questionObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Question_List'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    questionObj = question.objects.filter(branch_fk=branchObj).order_by('-id')
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    questionTypeObj = question_type_master.objects.all()
                    return render(request,'admin_template/question-bank/question-list.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'questionTypeObj':questionTypeObj,'questionObj':questionObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# add_question view
# #####################################################################################################################
# @login_required(login_url='/')
def add_question(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Add_Question'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.filter(branch_name=directorObj.branch_FK.branch_name)
                    # questionObj = question.objects.filter(branch_fk=branchObj).order_by('-id')
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    questionTypeObj = question_type_master.objects.all()
                    return render(request,'admin_template/question-bank/add-questions.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'questionTypeObj':questionTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Question'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.filter(branch_name=directorObj.branch_FK.branch_name)
                    # questionObj = question.objects.filter(branch_fk=branchObj).order_by('-id')
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    questionTypeObj = question_type_master.objects.all()
                    return render(request,'admin_template/question-bank/add-questions.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'questionTypeObj':questionTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Question'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.filter(branch_name=directorObj.branch_FK.branch_name)
                    # questionObj = question.objects.filter(branch_fk=branchObj).order_by('-id')
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    questionTypeObj = question_type_master.objects.all()
                    return render(request,'admin_template/question-bank/add-questions.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'questionTypeObj':questionTypeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
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
                if(sub_auth_dict['Add_Question'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classID = request.POST['classID']
                    subjectID = request.POST['subjectID']
                    yearID = request.POST['yearID']
                    topic = request.POST['topic']
                    question_typeID = request.POST['question_typeID']
                    question_subtypeID = request.POST['question_sub_type']
                    questionText = request.POST['question']
                    option_count = request.POST['option_count']
                    optionArray = request.POST.getlist('option_array[]')
                    difficulty = request.POST['difficulty']
                    correctMark = request.POST['correct_mark']
                    negativeMark = request.POST['negative_mark']


                    message = 'success'
                    counter = 100
                    try:
                        questioneObj = question.objects.latest('question_ID')
                        counter = int(questioneObj.question_ID.split('QT')[1]) + 1
                    except:
                        counter = 100

                    try:
                        if(option_count == ''):
                            option_count = 0

                        classObj = class_master.objects.get(id=int(classID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        yearObj = year_master.objects.get(id=int(yearID))
                        questionTypeObj = question_type_master.objects.get(id=int(question_typeID))

                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,year_fk=yearObj,topic_name=topic,question_type_fk=questionTypeObj,question_subtype_type=question_subtypeID,question_text=questionText)):
                            message = 'exist'
                            return JsonResponse({'message':message})
                        
                        questionObj = question(question_ID=f"QT{counter}",
                                                branch_fk=branchObj,
                                                class_fk=classObj,
                                                subject_fk=subjectObj,
                                                year_fk=yearObj,
                                                topic_name=topic,
                                                question_type_fk=questionTypeObj,
                                                question_subtype_type=question_subtypeID,
                                                question_text=questionText,
                                                option_count = option_count,
                                                option_array = optionArray,
                                                difficulty_type = difficulty,
                                                correct_mark = correctMark,
                                                negative_mark = negativeMark,
                                                created_by = f"Director - {directorObj.director_FK.director_name}")
                        questionObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Question'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classID = request.POST['classID']
                    subjectID = request.POST['subjectID']
                    yearID = request.POST['yearID']
                    topic = request.POST['topic']
                    question_typeID = request.POST['question_typeID']
                    question_subtypeID = request.POST['question_sub_type']
                    questionText = request.POST['question']
                    option_count = request.POST['option_count']
                    optionArray = request.POST.getlist('option_array[]')
                    difficulty = request.POST['difficulty']
                    correctMark = request.POST['correct_mark']
                    negativeMark = request.POST['negative_mark']


                    message = 'success'
                    counter = 100
                    try:
                        questioneObj = question.objects.latest('question_ID')
                        counter = int(questioneObj.question_ID.split('QT')[1]) + 1
                    except:
                        counter = 100

                    try:
                        if(option_count == ''):
                            option_count = 0

                        classObj = class_master.objects.get(id=int(classID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        yearObj = year_master.objects.get(id=int(yearID))
                        questionTypeObj = question_type_master.objects.get(id=int(question_typeID))

                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,year_fk=yearObj,topic_name=topic,question_type_fk=questionTypeObj,question_subtype_type=question_subtypeID,question_text=questionText)):
                            message = 'exist'
                            return JsonResponse({'message':message})
                        
                        questionObj = question(question_ID=f"QT{counter}",
                                                branch_fk=branchObj,
                                                class_fk=classObj,
                                                subject_fk=subjectObj,
                                                year_fk=yearObj,
                                                topic_name=topic,
                                                question_type_fk=questionTypeObj,
                                                question_subtype_type=question_subtypeID,
                                                question_text=questionText,
                                                option_count = option_count,
                                                option_array = optionArray,
                                                difficulty_type = difficulty,
                                                correct_mark = correctMark,
                                                negative_mark = negativeMark,
                                                created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                        questionObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Question'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classID = request.POST['classID']
                    subjectID = request.POST['subjectID']
                    yearID = request.POST['yearID']
                    topic = request.POST['topic']
                    question_typeID = request.POST['question_typeID']
                    question_subtypeID = request.POST['question_sub_type']
                    questionText = request.POST['question']
                    option_count = request.POST['option_count']
                    optionArray = request.POST.getlist('option_array[]')
                    difficulty = request.POST['difficulty']
                    correctMark = request.POST['correct_mark']
                    negativeMark = request.POST['negative_mark']


                    message = 'success'
                    counter = 100
                    try:
                        questioneObj = question.objects.latest('question_ID')
                        counter = int(questioneObj.question_ID.split('QT')[1]) + 1
                    except:
                        counter = 100

                    try:
                        if(option_count == ''):
                            option_count = 0

                        classObj = class_master.objects.get(id=int(classID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        yearObj = year_master.objects.get(id=int(yearID))
                        questionTypeObj = question_type_master.objects.get(id=int(question_typeID))

                        if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,year_fk=yearObj,topic_name=topic,question_type_fk=questionTypeObj,question_subtype_type=question_subtypeID,question_text=questionText)):
                            message = 'exist'
                            return JsonResponse({'message':message})
                        
                        questionObj = question(question_ID=f"QT{counter}",
                                                branch_fk=branchObj,
                                                class_fk=classObj,
                                                subject_fk=subjectObj,
                                                year_fk=yearObj,
                                                topic_name=topic,
                                                question_type_fk=questionTypeObj,
                                                question_subtype_type=question_subtypeID,
                                                question_text=questionText,
                                                option_count = option_count,
                                                option_array = optionArray,
                                                difficulty_type = difficulty,
                                                correct_mark = correctMark,
                                                negative_mark = negativeMark,
                                                created_by = f"School Admin - {directorObj.schoolAdmin_FK.schoolAdmin_name}")
                        questionObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')
                    
        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# fetch topics view
# #####################################################################################################################
# @login_required(login_url='/')
def fetch_topics(request):
    if request.method == 'GET':
        class_id = request.GET['classID']
        subject_id = request.GET['subjectID']

        classObj = class_master.objects.get(id=int(class_id))
        subjectObj = subject_master.objects.get(id=int(subject_id))
        topicsList = []
        try:
            topicObj = topic_master.objects.get(class_FK=classObj,subject_FK=subjectObj)
            for i in eval(topicObj.topic_name).split(','):
                topicsList.append(i.title())
        except:
            topicsList = []

        return  JsonResponse({'topicsList':topicsList})


# #####################################################################################################################
# fetch specific question view
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
# edit specific question
# #####################################################################################################################
# @login_required(login_url='/')
def edit_question(request,id):
    if request.method == 'GET':
        return render(request,'admin_template/question-bank/edit-question.html')


# #####################################################################################################################
# filter question
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
# delete question
# #####################################################################################################################
# @login_required(login_url='/')
def delete_question(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Delete_Question'] == True):
                    try:
                        questionObj = question.objects.get(id=int(id))
                        questionObj.delete()
                        return redirect('question_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Delete_Question'] == True):
                    try:
                        questionObj = question.objects.get(id=int(id))
                        questionObj.delete()
                        return redirect('question_list')
                    except:
                        return render(request,'403.html')

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Delete_Question'] == True):
                    try:
                        questionObj = question.objects.get(id=int(id))
                        questionObj.delete()
                        return redirect('question_list')
                    except:
                        return render(request,'403.html')

                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')