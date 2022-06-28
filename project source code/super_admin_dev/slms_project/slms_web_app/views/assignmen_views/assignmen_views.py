from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required

from slms_web_app.models.assignment_models import assignment_model
from ...models.master_models import Authority_master, SubAuthority_master, section_master, subject_master,user_designation_master,year_master,question_type_master,exam_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import class_master,branch
from ...models.exam_models import exam_model
from ...models.paper_models import question_paper_model
from ..utils_views import get_auth_dict,get_Subauth_dict
# #####################################################################################################################
# assignment_list view
# #####################################################################################################################
@login_required(login_url='/')
def assignment_list(request):
    if request.method == 'GET':
        assignmentObj = assignment_model.objects.all().order_by('-id')
        return render(request,'admin_template/assignment-management/assignment-list.html',{'assignmentObj':assignmentObj})


# #####################################################################################################################
# add_assignment view
# #####################################################################################################################
@login_required(login_url='/')
def add_assignment(request):
    if request.method == 'GET':
        branchObj = branch.objects.all()
        yearObj = year_master.objects.all()
        questionTypeObj = question_type_master.objects.all()
        yearObj = year_master.objects.all()
        return render(request,'admin_template/assignment-management/add-assignment.html',{'branchObj':branchObj,'questionTypeObj':questionTypeObj,'yearObj':yearObj})

    if request.method == 'POST':
        assignmentName = request.POST['assignment_name']
        branchID = request.POST['branchID']
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
            branchObj = branch.objects.get(id=int(branchID))
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
                                            guidelines = guideline)
            assignmentObj.save()
            return JsonResponse({'message':message})
        except:
            message = 'failed'
            return JsonResponse({'message':message})


# #####################################################################################################################
# check assignment name view
# #####################################################################################################################
@login_required(login_url='/')
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
@login_required(login_url='/')
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
@login_required(login_url='/')
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
@login_required(login_url='/')
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
@login_required(login_url='/')
def edit_question(request,id):
    if request.method == 'GET':
        return render(request,'admin_template/paper-bank/edit-paper.html')


# #####################################################################################################################
# delete assignment view
# #####################################################################################################################
@login_required(login_url='/')
def delete_assignment(request,id):
    if request.method == 'GET':
        assignmentObj = assignment_model.objects.get(id=int(id))
        assignmentObj.delete()
        return redirect('assignment_list')

# #####################################################################################################################
# filter paper
# #####################################################################################################################
@login_required(login_url='/')
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
@login_required(login_url='/')
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
# delete question
# #####################################################################################################################
@login_required(login_url='/')
def delete_question(request,id):
    if request.method == 'GET':
        questionObj = question.objects.get(id=int(id))
        questionObj.delete()
        return redirect('question_list')



# #####################################################################################################################
# get section questions
# #####################################################################################################################
@login_required(login_url='/')
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



