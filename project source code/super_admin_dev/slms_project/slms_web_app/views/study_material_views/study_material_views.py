from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required

from slms_web_app.models.assignment_models import assignment_model
from ...models.master_models import Authority_master, SubAuthority_master, file_type_master, section_master, subject_master,user_designation_master,year_master,question_type_master,exam_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import class_master,branch
from ...models.exam_models import exam_model
from ...models.paper_models import question_paper_model
from ...models.studey_material_models import study_material
# #####################################################################################################################
# study_material_list view
# #####################################################################################################################
@login_required(login_url='/')
def study_material_list(request):
    if request.method == 'GET':
        study_materialObj = study_material.objects.all().order_by('-id')
        return render(request,'admin_template/study-material/material-list.html',{'study_materialObj':study_materialObj})


# #####################################################################################################################
# add_study_material view
# #####################################################################################################################
@login_required(login_url='/')
def add_study_material(request):
    if request.method == 'GET':
        branchObj = branch.objects.all()
        fileTypeObj = file_type_master.objects.all()
        return render(request,'admin_template/study-material/add-material.html',{'branchObj':branchObj,'fileTypeObj':fileTypeObj})

    if request.method == 'POST':
        branch_id = request.POST['branch_id']
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

        # try:
        branchObj = branch.objects.get(id=int(branch_id))
        classObj = class_master.objects.get(id=int(classs_id))
        subjectObj = subject_master.objects.get(id=int(subject_id))
        fileTypeObj = file_type_master.objects.get(id=int(file_type_id))
        
        study_materialObj = study_material(study_material_ID=f"SM-{counter}",
                                        branch_fk=branchObj,
                                        class_fk=classObj,
                                        subject_fk=subjectObj,
                                        topic=topic,
                                        file_type_fk=fileTypeObj,
                                        content=file_content)
        study_materialObj.save()
        return JsonResponse({'message':message})
        # except:
        #     message = 'failed'
        #     return JsonResponse({'message':message})


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
# fetch specific study material view
# #####################################################################################################################
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
@login_required(login_url='/')
def view_study_material(request,id):
    if request.method == 'GET':
        study_materialObj = study_material.objects.get(id=int(id))
        return render(request,'admin_template/study-material/material-detail.html',{'study_materialObj':study_materialObj})

    
# #####################################################################################################################
# edit specific study material
# #####################################################################################################################
@xframe_options_exempt
@login_required(login_url='/')
def edit_study_material(request,id):
    if request.method == 'GET':
        study_materialObj = study_material.objects.get(id=int(id))
        fileTypeObj = file_type_master.objects.all()
        return render(request,'admin_template/study-material/edit-material.html',{'study_materialObj':study_materialObj,'fileTypeObj':fileTypeObj})

    if request.method == 'POST':
        file_type_id = request.POST['file_type_id']
        file_content = request.FILES.get('content')

        try:
            message = 'success'
            study_materialObj = study_material.objects.get(id=int(id))
            fileTypeObj = file_type_master.objects.get(id=int(file_type_id))

            study_materialObj.file_type_fk=fileTypeObj
            study_materialObj.content=file_content
            study_materialObj.save()
            return JsonResponse({'message':message})
        except:
            message = 'failed'
            return JsonResponse({'message':message})



# #####################################################################################################################
# delete assignment view
# #####################################################################################################################
@login_required(login_url='/')
def delete_study_material(request,id):
    if request.method == 'GET':
        assignmentObj = study_material.objects.get(id=int(id))
        assignmentObj.delete()
        return redirect('study_material_list')

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



