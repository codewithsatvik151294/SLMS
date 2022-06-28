from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ...models.master_models import section_master, year_master
from ...models.manage_models import branch, class_master, student_profile, student_user
from ...models.attendance_models import attendance_model
from datetime import date
today = date.today()
# #####################################################################################################################
# add_attendance view
# #####################################################################################################################
@login_required(login_url='/')
def add_attendance(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        yearObj = year_master.objects.all().order_by('-id')
        return render(request,'admin_template/attendance-management/make-attendance.html',{'branchObj':branchObj,'yearObj':yearObj})

    if request.method == 'POST':
        message = 'success'
        branchId = request.POST['branch_id']
        year_id = request.POST['year_id']
        class_id = request.POST['class_id']
        section_id = request.POST['section_id']
        attendaceArray = request.POST['attendace_list[]']

        try:
            attendanceList = eval(attendaceArray)

            branchObj = branch.objects.get(id=int(branchId))
            yearObj = year_master.objects.get(id=int(year_id))
            classObj = class_master.objects.get(id=int(class_id))
            sectionObj = section_master.objects.get(id=int(section_id))

            for i in attendanceList:
                studentUserObj = student_user.objects.get(student_registration_number=i['student_reg'])
                studentObj = student_profile.objects.get(student_FK=studentUserObj)
                print('studentObj >>> ',studentObj)
                if(attendance_model.objects.filter(student_fk=studentObj,branch_fk=branchObj,class_fk=classObj,section_fk=sectionObj,attendance_date=today)):
                    attendanceObj = attendance_model.objects.get(student_fk=studentObj,branch_fk=branchObj,class_fk=classObj,section_fk=sectionObj,attendance_date=today)
                    attendanceObj.attendance_status = i['attendance_status']
                    attendanceObj.save()

                else:
                    counter = 100
                    try:
                        attObj = attendance_model.objects.latest('attendance_ID')
                        counter = int(attObj.attendance_ID.split('ATD-')[1]) + 1
                    except:
                        counter = 100
                    attendanceObj = attendance_model(attendance_ID=f"ATD-{counter}",attendance_session=today.year,student_fk=studentObj,branch_fk=branchObj,class_fk=classObj,section_fk=sectionObj,attendance_date=today,attendance_status=i['attendance_status'])
                    attendanceObj.save()

        except:
            message = 'failed'

        return JsonResponse({'message':message})


# #####################################################################################################################
# view_attendance view
# #####################################################################################################################
@login_required(login_url='/')
def view_attendance(request,id):
    if request.method == 'GET':
        studentObj = student_profile.objects.get(id=int(id))
        student_attendance_obj = attendance_model.objects.filter(student_fk = studentObj).count()
        context = {}

        if(student_attendance_obj > 0):
            context['total_attendance'] = student_attendance_obj
            context['total_present'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='1').count()
            context['total_absent'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='2').count()
            context['overall_percent'] = ((attendance_model.objects.filter(student_fk = studentObj).count() - attendance_model.objects.filter(student_fk = studentObj,attendance_status='2').count())/attendance_model.objects.filter(student_fk = studentObj).count())*100
        else:
            context['total_attendance'] = 0
            context['total_present'] = 0
            context['total_absent'] = 0
            context['overall_percent'] = 0

        # current month data
        student_current_attendance_obj = attendance_model.objects.filter(student_fk = studentObj,created_at__year = today.year).count()
        if(student_current_attendance_obj > 0):
            context['total_month_attendance'] = student_current_attendance_obj
            context['total_month_present'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='1').count()
            context['total_month_absent'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='2').count()
        else:
            context['total_month_attendance'] = 0
            context['total_month_present'] = 0
            context['total_month_absent'] = 0

        # calander data
        student_attendanceObj = attendance_model.objects.filter(student_fk = studentObj)
        print('student_attendanceObj >>>> ',student_attendanceObj)
        calanderList = []
        for i in student_attendanceObj:
            calanderDict = {}
            if(i.attendance_status == '1'):
                calanderDict['title'] = 'P'
                calanderDict['backgroundColor'] = '#7fc27c'
            else:
                calanderDict['title'] = 'A'
                calanderDict['backgroundColor'] = '#ea9595'
            calanderDict['start'] = str(i.attendance_date)
            calanderList.append(calanderDict)

        return render(request,'admin_template/attendance-management/attendance-details.html',{'studentObj':studentObj,'context':context,'calanderList':calanderList})


# #####################################################################################################################
# edit_attendance view
# #####################################################################################################################
@login_required(login_url='/')
def edit_attendance(request,id):
    if request.method == 'GET':
        studentObj = student_profile.objects.get(id=int(id))
        student_attendance_obj = attendance_model.objects.filter(student_fk = studentObj).count()
        context = {}

        if(student_attendance_obj > 0):
            context['total_attendance'] = student_attendance_obj
            context['total_present'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='1').count()
            context['total_absent'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='2').count()
            context['overall_percent'] = ((attendance_model.objects.filter(student_fk = studentObj).count() - attendance_model.objects.filter(student_fk = studentObj,attendance_status='2').count())/attendance_model.objects.filter(student_fk = studentObj).count())*100
        else:
            context['total_attendance'] = 0
            context['total_present'] = 0
            context['total_absent'] = 0
            context['overall_percent'] = 0

        # current month data
        student_current_attendance_obj = attendance_model.objects.filter(student_fk = studentObj,created_at__year = today.year).count()
        if(student_current_attendance_obj > 0):
            context['total_month_attendance'] = student_current_attendance_obj
            context['total_month_present'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='1').count()
            context['total_month_absent'] = attendance_model.objects.filter(student_fk = studentObj,attendance_status='2').count()
        else:
            context['total_month_attendance'] = 0
            context['total_month_present'] = 0
            context['total_month_absent'] = 0

        # calander data
        student_attendanceObj = attendance_model.objects.filter(student_fk = studentObj)
        print('student_attendanceObj >>>> ',student_attendanceObj)
        calanderList = []
        for i in student_attendanceObj:
            calanderDict = {}
            if(i.attendance_status == '1'):
                calanderDict['title'] = 'P'
                calanderDict['backgroundColor'] = '#7fc27c'
            else:
                calanderDict['title'] = 'A'
                calanderDict['backgroundColor'] = '#ea9595'
            calanderDict['start'] = str(i.attendance_date)
            calanderList.append(calanderDict)
        return render(request,'admin_template/attendance-management/edit-details.html',{'studentObj':studentObj,'context':context,'calanderList':calanderList})

# #####################################################################################################################
# attendance_list view
# #####################################################################################################################
@login_required(login_url='/')
def attendance_list(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        yearObj = year_master.objects.all().order_by('-id')
        return render(request,'admin_template/attendance-management/attendance-list.html',{'branchObj':branchObj,'yearObj':yearObj})


# #####################################################################################################################
# filter_student
# #####################################################################################################################
@login_required(login_url='/')
def filter_student(request):
    if request.method == 'GET':
        branchId = request.GET['branchId']
        year_id = request.GET['year_id']
        class_id = request.GET['class_id']
        section_id = request.GET['section_id']

        branchObj = branch.objects.get(id=int(branchId))
        yearObj = year_master.objects.get(id=int(year_id))
        classObj = class_master.objects.get(id=int(class_id))
        sectionObj = section_master.objects.get(id=int(section_id))

        studentObj = student_profile.objects.filter(branch_FK = branchObj,
                                                    class_fk = classObj,
                                                    section_fk = sectionObj,
                                                    created_at__year = yearObj.year_name
                                                    )

        data_list = []
        for i in studentObj:
            context = {}
            context['id'] = i.id
            context['student_reg_no'] = i.student_FK.student_registration_number
            context['student_name'] = f"{i.student_FK.student_first_name} {i.student_FK.student_last_name}"

            # calculate overall % for student i
            student_attendance_obj = attendance_model.objects.filter(student_fk = i).count()
            print(student_attendance_obj)
            if(student_attendance_obj > 0):
                context['total_present'] = attendance_model.objects.filter(student_fk = i,attendance_status='1').count()
                context['total_absent'] = attendance_model.objects.filter(student_fk = i,attendance_status='2').count()
                context['overall_percent'] = ((attendance_model.objects.filter(student_fk = i).count() - attendance_model.objects.filter(student_fk = i,attendance_status='2').count())/attendance_model.objects.filter(student_fk = i).count())*100
            else:
                context['total_present'] = 0
                context['total_absent'] = 0
                context['overall_percent'] = 0
            data_list.append(context)
        
        return JsonResponse({'response':data_list})



# #####################################################################################################################
# filter_student_monthwise
# #####################################################################################################################
@login_required(login_url='/')
def filter_student_monthwise(request):
    if request.method == 'GET':
        student_id = request.GET['student_id']
        year = request.GET['year']
        month = request.GET['month']

        studentObj = student_profile.objects.get(id=int(student_id))
        data_list = []
        student_attendance_obj = attendance_model.objects.filter(student_fk = studentObj,attendance_date__year__gte=int(year),attendance_date__month__gte=int(month),attendance_date__year__lte=int(year),attendance_date__month__lte=int(month)).order_by('-id')
        print(student_attendance_obj,len(student_attendance_obj))

        for i in student_attendance_obj:
            context = {}
            context['date'] = str(i.attendance_date.strftime("%d-%b-%Y")) + ' - ' + str(i.attendance_date.strftime("%A"))
            context['attendance_status'] = i.attendance_status
            data_list.append(context)
        return JsonResponse({'response':data_list})

    
# # #####################################################################################################################
# # edit specific paper
# # #####################################################################################################################
# @login_required(login_url='/')
# def edit_question(request,id):
#     if request.method == 'GET':
#         return render(request,'admin_template/paper-bank/edit-paper.html')


# # #####################################################################################################################
# # delete paper view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_paper(request,id):
#     if request.method == 'GET':
#         paperObj = question_paper_model.objects.get(id=int(id))
#         paperObj.delete()
#         return redirect('paper_list')






# # #####################################################################################################################
# # fetch questions
# # #####################################################################################################################
# @login_required(login_url='/')
# def fetch_questions(request):
#     if request.method == 'GET':
#         branchID = request.GET['branch_id']
#         class_id = request.GET['class_id']
#         subject_id = request.GET['subject_id']
#         qType_list = request.GET.getlist('qType[]')

#         data_list = []
#         branchObj = branch.objects.get(id=int(branchID))
#         classObj = class_master.objects.get(id=int(class_id))
#         subjectObj = subject_master.objects.get(id=int(subject_id))

#         if(len(qType_list) == 2):
#             if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj)):
#                 for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj):
#                     context = {}
#                     context['id'] = i.id
#                     context['question_text'] = i.question_text
#                     context['question_type'] = i.question_type_fk.questionType_name.title()
#                     context['question_sub_type'] = i.question_subtype_type.title()
#                     if(i.difficulty_type == '1'):
#                         context['difficulty'] = 'Easy'
#                     elif(i.difficulty_type == '2'):
#                         context['difficulty'] = 'Moderate'
#                     elif(i.difficulty_type == '3'):
#                         context['difficulty'] = 'Hard'
                        
#                     context['correct_mark'] = i.correct_mark
#                     context['subject_name'] = i.subject_fk.subject_name.title()
#                     context['topic_name'] = i.topic_name.title()
#                     context['year_name'] = i.year_fk.year_name
#                     data_list.append(context)
#         else:
#             questionType = ''
#             if(qType_list[0] == '1'):
#                 questionType = 'objective'
#             elif(qType_list[0] == '2'):
#                 questionType = 'subjective'
#             elif(qType_list[0] == '3'):
#                 questionType = 'multiple choice objective'
#             elif(qType_list[0] == '4'):
#                 questionType = 'diagram upload'
            
#             qTypeObj = question_type_master.objects.get(questionType_name=questionType)

#             if(question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj)):
#                 for i in question.objects.filter(branch_fk=branchObj,class_fk=classObj,subject_fk=subjectObj,question_type_fk=qTypeObj):
#                     context = {}
#                     context['id'] = i.id
#                     context['question_text'] = i.question_text
#                     context['question_type'] = i.question_type_fk.questionType_name.title()
#                     context['question_sub_type'] = i.question_subtype_type.title()
#                     if(i.difficulty_type == '1'):
#                         context['difficulty'] = 'Easy'
#                     elif(i.difficulty_type == '2'):
#                         context['difficulty'] = 'Moderate'
#                     elif(i.difficulty_type == '3'):
#                         context['difficulty'] = 'Hard'
                        
#                     context['correct_mark'] = i.correct_mark
#                     context['subject_name'] = i.subject_fk.subject_name.title()
#                     context['topic_name'] = i.topic_name.title()
#                     context['year_name'] = i.year_fk.year_name
#                     data_list.append(context)
        
#         return JsonResponse({'data_list':data_list})


# # #####################################################################################################################
# # delete question
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_question(request,id):
#     if request.method == 'GET':
#         questionObj = question.objects.get(id=int(id))
#         questionObj.delete()
#         return redirect('question_list')



# # #####################################################################################################################
# # get section questions
# # #####################################################################################################################
# @login_required(login_url='/')
# def get_questions(request):
#     if request.method == 'GET':
#         question_array = request.GET.getlist('question_array[]')
#         print('question_array >>> ',question_array)
#         question_list = []
#         for i in question_array:
#             questionObj = question.objects.get(id=int(i))
#             context = {}
#             context['id'] = questionObj.id
#             context['question_text'] = questionObj.question_text
#             question_list.append(context)
        
#         return JsonResponse({'question_list':question_list})



