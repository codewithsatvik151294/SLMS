from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.master_models import Authority_master, SubAuthority_master, subject_master,user_designation_master,year_master,question_type_master,exam_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import Teacher_user, branch, class_master,Teacher_profile
from ...models.exam_models import exam_model,exam_paper_detail
from ...models.paper_models import question_paper_model

# #####################################################################################################################
# exam_list view
# #####################################################################################################################
@login_required(login_url='/')
def exam_list(request):
    if request.method == 'GET':
        examObj = exam_model.objects.all().order_by('-id')
        return render(request,'admin_template/exam-management/exam-list.html',{'examObj':examObj})


# #####################################################################################################################
# add_paper view
# #####################################################################################################################
@login_required(login_url='/')
def add_exam(request):
    if request.method == 'GET':
        branchObj = branch.objects.all()
        yearObj = year_master.objects.all()
        examTypeObj = exam_type_master.objects.all()
        yearObj = year_master.objects.all()
        counter = 100
        try:
            examObj = exam_model.objects.latest('exam_ID')
            counter = int(examObj.exam_ID.split('EX-')[1]) + 1
        except:
            counter = 100
        return render(request,'admin_template/exam-management/create-exam.html',{'branchObj':branchObj,'counter':counter,'examTypeObj':examTypeObj,'yearObj':yearObj})

    if request.method == 'POST':
        exanName = request.POST['examName']
        examType = request.POST['exam_type']
        branchID = request.POST['branchID']
        classID = request.POST['classID']
        negativeEnabled = request.POST['negative_marking_allowed']
        examData = request.POST['exam_data[]']

        if(negativeEnabled == 0):
            negativeEnabled = False
        else:
            negativeEnabled = True

        print('negativeEnabled >> ',negativeEnabled)
        print('examData >> ',eval(examData),type(eval(examData)))

        examData = eval(examData)


        message = 'success'
        counter = 100
        try:
            examObj = exam_model.objects.latest('exam_ID')
            counter = int(examObj.exam_ID.split('EX-')[1]) + 1
        except:
            counter = 100

        # try:
        from datetime import date
        todays_date = date.today()
        classObj = class_master.objects.get(id=int(classID))
        branchObj = branch.objects.get(id=int(branchID))
        exam_typeObj = exam_type_master.objects.get(id=int(examType))

        if(exam_model.objects.filter(class_fk=classObj,branch_FK=branchObj,exam_type_fk=exam_typeObj,exam_name=exanName)):
            message = 'exist'
            return JsonResponse({'message':message})

        examObj = exam_model(exam_ID = 'EX-'+str(counter),
                            exam_name = exanName.lower(),
                            class_fk = classObj,
                            year = todays_date.year,
                            exam_type_fk = exam_typeObj,
                            branch_FK = branchObj,
                            negative_marking_status = negativeEnabled,
                            total_papers = len(examData)
                            )
        examObj.save()
        
        for i in examData:
            paperObj = question_paper_model.objects.get(id=int(i['paper_id']))
            proctorObj = Teacher_profile.objects.get(id=int(i['paper_proctor_id']))
            exam_detailObj = exam_paper_detail(exam_fk = examObj,
                                                paper_fk = paperObj,
                                                exam_start_date_time = i['paper_start_date_time'],
                                                exam_end_date_time = i['paper_end_date_time'],
                                                proctor_fk = proctorObj
                                                )
            exam_detailObj.save()

        return JsonResponse({'message':message})
        # except:
        #     message = 'failed'
        #     return JsonResponse({'message':message})


# #####################################################################################################################
# check exam name view
# #####################################################################################################################
@login_required(login_url='/')
def check_exam(request):
    if request.method == 'GET':
        message = 'not-exisit'
        searchString = request.GET['search_string']
        if(exam_model.objects.filter(exam_name = searchString.lower())):
            message = 'exist'

        return  JsonResponse({'message':message})


# #####################################################################################################################
# get class view
# #####################################################################################################################
@login_required(login_url='/')
def fetch_class(request):
    if request.method == 'GET':
        classList = []
        searchString = request.GET['branchID']
        branchObj = branch.objects.get(id=int(searchString))
        if(class_master.objects.filter(branch_FK = branchObj)):
            for i in class_master.objects.filter(branch_FK = branchObj):
                context = {}
                context['id'] = i.id
                context['class_name'] = i.class_name
                classList.append(context)
        return  JsonResponse({'classList':classList})


# #####################################################################################################################
# get teacher view
# #####################################################################################################################
@login_required(login_url='/')
def fetch_teacher(request):
    if request.method == 'GET':
        teacherList = []
        searchString = request.GET['branchID']
        branchObj = branch.objects.get(id=int(searchString))
        if(Teacher_profile.objects.filter(branch_FK = branchObj)):
            for i in Teacher_profile.objects.filter(branch_FK = branchObj):
                context = {}
                context['id'] = i.id
                context['teacher_name'] = i.teacher_FK.teacher_name
                teacherList.append(context)
        return  JsonResponse({'teacherList':teacherList})


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
# fetch specific exam view
# #####################################################################################################################
@login_required(login_url='/')
def view_exam(request,id):
    if request.method == 'GET':
        paperList = []
        try:
            examObj = exam_model.objects.get(id=int(id))

            for i in exam_paper_detail.objects.filter(exam_fk = examObj):
                context = {}
                context['paper_name'] = i.paper_fk.paper_name
                context['subject'] = i.paper_fk.subject_fk.subject_name
                context['Year'] = i.paper_fk.year_fk.year_name
                context['start'] = i.exam_start_date_time
                context['end'] = i.exam_end_date_time
                context['proctor'] = i.proctor_fk.teacher_FK.teacher_name

                paperList .append(context)
            

        except:
            paperList = []

        return  render(request,'admin_template/exam-management/exam-details.html',{'examObj':examObj,'paperList':paperList})

    
# #####################################################################################################################
# edit specific exam
# #####################################################################################################################
@login_required(login_url='/')
def edit_exam(request,id):
    if request.method == 'GET':
        return render(request,'admin_template/exam-management/edit-details.html')


# #####################################################################################################################
# delete exam view
# #####################################################################################################################
@login_required(login_url='/')
def delete_exam(request,id):
    if request.method == 'GET':
        paperObj = exam_model.objects.get(id=int(id))
        paperObj.delete()
        return redirect('exam_list')

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

        data_list = []
        classObj = class_master.objects.get(id=int(class_id))
        subjectObj = subject_master.objects.get(id=int(subject_id))

        if(len(qType_list) == 2):
            if(question.objects.filter(class_fk=classObj,subject_fk=subjectObj)):
                for i in question.objects.filter(class_fk=classObj,subject_fk=subjectObj):
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

            if(question.objects.filter(class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj)):
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



