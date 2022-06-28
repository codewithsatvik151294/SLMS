from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.master_models import Authority_master, SubAuthority_master, subject_master,user_designation_master,year_master,question_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import class_master,topic_master,branch,director_profile,principal_profile,schoolAdmin_profile
from ...models.paper_models import question_paper_model
from ..utils_views import get_auth_dict,get_Subauth_dict
# #####################################################################################################################
# Paper_List view
# #####################################################################################################################
# @login_required(login_url='/')
def paper_list(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Paper_List'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    paperObj = question_paper_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/paper-management/paper-list.html',{'branchObj':branchObj,'paperObj':paperObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Paper_List'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    paperObj = question_paper_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/paper-management/paper-list.html',{'branchObj':branchObj,'paperObj':paperObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Paper_List'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    paperObj = question_paper_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/paper-management/paper-list.html',{'branchObj':branchObj,'paperObj':paperObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# add_paper view
# #####################################################################################################################
# @login_required(login_url='/')
def add_paper(request):
    if request.method == 'GET':
        if 'admin_userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['admin_userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])

        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Add_Paper'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    try:
                        paperObj = question_paper_model.objects.latest('paper_ID')
                        counter = int(paperObj.paper_ID.split('PAPER-')[1]) + 1
                    except:
                        counter = 100
                    return render(request,'admin_template/paper-management/create-paper.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'counter':counter,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Paper'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    try:
                        paperObj = question_paper_model.objects.latest('paper_ID')
                        counter = int(paperObj.paper_ID.split('PAPER-')[1]) + 1
                    except:
                        counter = 100
                    return render(request,'admin_template/paper-management/create-paper.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'counter':counter,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Paper'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    yearObj = year_master.objects.all()
                    try:
                        paperObj = question_paper_model.objects.latest('paper_ID')
                        counter = int(paperObj.paper_ID.split('PAPER-')[1]) + 1
                    except:
                        counter = 100
                    return render(request,'admin_template/paper-management/create-paper.html',{'branchObj':branchObj,'classObj':classObj,'yearObj':yearObj,'counter':counter,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
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
                if(sub_auth_dict['Add_Paper'] == True):
                    directorObj = director_profile.objects.get(id=int(request.session['director_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    paperObj = question_paper_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    paperName = request.POST['paperName']
                    classID = request.POST['classID']
                    subjectID = request.POST['subjectID']
                    yearID = request.POST['yearID']
                    totalMarks = request.POST['totalMarks']
                    passingMarks = request.POST['passingMarks']
                    sectionCount = request.POST['sectionCount']
                    sectionDetail = request.POST['sectionDetail[]']


                    message = 'success'
                    counter = 100
                    try:
                        paperObj = question_paper_model.objects.latest('paper_ID')
                        counter = int(paperObj.paper_ID.split('PAPER-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        yearObj = year_master.objects.get(id=int(yearID))
                        
                        questionObj = question_paper_model(paper_ID=f"PAPER-{counter}",
                                                            branch_FK = branchObj,
                                                            paper_name=paperName,
                                                            class_fk=classObj,
                                                            subject_fk=subjectObj,
                                                            year_fk=yearObj,
                                                            total_marks=totalMarks,
                                                            passing_marks=passingMarks,
                                                            section_count=sectionCount,
                                                            section_detail = sectionDetail,
                                                            created_by = f"Director - {directorObj.director_FK.director_name}")
                        questionObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Add_Paper'] == True):
                    directorObj = principal_profile.objects.get(id=int(request.session['principal_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    paperObj = question_paper_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    paperName = request.POST['paperName']
                    classID = request.POST['classID']
                    subjectID = request.POST['subjectID']
                    yearID = request.POST['yearID']
                    totalMarks = request.POST['totalMarks']
                    passingMarks = request.POST['passingMarks']
                    sectionCount = request.POST['sectionCount']
                    sectionDetail = request.POST['sectionDetail[]']


                    message = 'success'
                    counter = 100
                    try:
                        paperObj = question_paper_model.objects.latest('paper_ID')
                        counter = int(paperObj.paper_ID.split('PAPER-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        yearObj = year_master.objects.get(id=int(yearID))
                        
                        questionObj = question_paper_model(paper_ID=f"PAPER-{counter}",
                                                            branch_FK = branchObj,
                                                            paper_name=paperName,
                                                            class_fk=classObj,
                                                            subject_fk=subjectObj,
                                                            year_fk=yearObj,
                                                            total_marks=totalMarks,
                                                            passing_marks=passingMarks,
                                                            section_count=sectionCount,
                                                            section_detail = sectionDetail,
                                                            created_by = f"Principal - {directorObj.principal_FK.principal_name}")
                        questionObj.save()
                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Add_Paper'] == True):
                    directorObj = schoolAdmin_profile.objects.get(id=int(request.session['school_admin_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    paperObj = question_paper_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    paperName = request.POST['paperName']
                    classID = request.POST['classID']
                    subjectID = request.POST['subjectID']
                    yearID = request.POST['yearID']
                    totalMarks = request.POST['totalMarks']
                    passingMarks = request.POST['passingMarks']
                    sectionCount = request.POST['sectionCount']
                    sectionDetail = request.POST['sectionDetail[]']


                    message = 'success'
                    counter = 100
                    try:
                        paperObj = question_paper_model.objects.latest('paper_ID')
                        counter = int(paperObj.paper_ID.split('PAPER-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        classObj = class_master.objects.get(id=int(classID))
                        subjectObj = subject_master.objects.get(id=int(subjectID))
                        yearObj = year_master.objects.get(id=int(yearID))
                        
                        questionObj = question_paper_model(paper_ID=f"PAPER-{counter}",
                                                            branch_FK = branchObj,
                                                            paper_name=paperName,
                                                            class_fk=classObj,
                                                            subject_fk=subjectObj,
                                                            year_fk=yearObj,
                                                            total_marks=totalMarks,
                                                            passing_marks=passingMarks,
                                                            section_count=sectionCount,
                                                            section_detail = sectionDetail,
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
# check paper name view
# #####################################################################################################################
# @login_required(login_url='/')
def check_paper_name(request):
    if request.method == 'GET':
        message = 'not-exisit'
        searchString = request.GET['search_string']
        if(question_paper_model.objects.filter(paper_name = searchString.lower())):
            message = 'exist'

        return  JsonResponse({'message':message})


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
# delete paper view
# #####################################################################################################################
# @login_required(login_url='/')
def delete_paper(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['admin_userType'])
        if 'admin_userType' in request.session:
            if(request.session['admin_userType'] == 'director_login'):
                if(sub_auth_dict['Delete_Paper'] == True):
                    try:
                        paperObj = question_paper_model.objects.get(id=int(id))
                        paperObj.delete()
                        return redirect('paper_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'principal_login'):
                if(sub_auth_dict['Delete_Paper'] == True):
                    try:
                        paperObj = question_paper_model.objects.get(id=int(id))
                        paperObj.delete()
                        return redirect('paper_list')
                    except:
                        return render(request,'403.html')

                else:
                    return render(request,'403.html')

            elif(request.session['admin_userType'] == 'school_admin_login'):
                if(sub_auth_dict['Delete_Paper'] == True):
                    try:
                        paperObj = question_paper_model.objects.get(id=int(id))
                        paperObj.delete()
                        return redirect('paper_list')
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
                if(sub_auth_dict['Paper_List'] == True):
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
                if(sub_auth_dict['Paper_List'] == True):
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
                if(sub_auth_dict['Paper_List'] == True):
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
        data_list = []
        for i in question_array:
            questionObj = question.objects.get(id=int(i))
            context = {}
            context['id'] = questionObj.id
            context['question_text'] = questionObj.question_text
            data_list.append(context)
        
        return JsonResponse({'data_list':data_list})



