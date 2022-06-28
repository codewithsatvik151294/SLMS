from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.master_models import Authority_master, SubAuthority_master, subject_master,user_designation_master,year_master,question_type_master,exam_type_master
from ...models.authority_models import assign_authority
from ...models.question_management_models import question
from ...models.manage_models import Teacher_user, branch, class_master,Teacher_profile,Teacher_profile,schoolAdmin_profile,Teacher_profile
from ...models.exam_models import exam_model,exam_paper_detail
from ...models.paper_models import question_paper_model
from ..utils_views import get_auth_dict,get_Subauth_dict
# #####################################################################################################################
# exam_list view
# #####################################################################################################################
# @login_required(login_url='/')
def exam_list(request):
    if request.method == 'GET':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Exam_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    examObj = exam_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/exam-management/exam-list.html',{'branchObj':branchObj,'examObj':examObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Exam_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    examObj = exam_model.objects.filter(branch_FK=branchObj).order_by('-id')
                    return render(request,'admin_template/exam-management/exam-list.html',{'branchObj':branchObj,'examObj':examObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# add_paper view
# #####################################################################################################################
# @login_required(login_url='/')
def add_exam(request):
    if request.method == 'GET':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Add_Exam'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    yearObj = year_master.objects.all()
                    examTypeObj = exam_type_master.objects.all()
                    yearObj = year_master.objects.all()
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    counter = 100
                    try:
                        examObj = exam_model.objects.latest('exam_ID')
                        counter = int(examObj.exam_ID.split('EX-')[1]) + 1
                    except:
                        counter = 100
                    return render(request,'admin_template/exam-management/create-exam.html',{'classObj':classObj,'branchObj':branchObj,'counter':counter,'examTypeObj':examTypeObj,'yearObj':yearObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Add_Exam'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    yearObj = year_master.objects.all()
                    examTypeObj = exam_type_master.objects.all()
                    yearObj = year_master.objects.all()
                    classObj = class_master.objects.filter(branch_FK=branchObj)
                    counter = 100
                    try:
                        examObj = exam_model.objects.latest('exam_ID')
                        counter = int(examObj.exam_ID.split('EX-')[1]) + 1
                    except:
                        counter = 100
                    return render(request,'admin_template/exam-management/create-exam.html',{'classObj':classObj,'branchObj':branchObj,'counter':counter,'examTypeObj':examTypeObj,'yearObj':yearObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')


    if request.method == 'POST':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Add_Exam'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    exanName = request.POST['examName']
                    examType = request.POST['exam_type']
                    classID = request.POST['classID']
                    negativeEnabled = request.POST['negative_marking_allowed']
                    examData = request.POST['exam_data[]']

                    if(negativeEnabled == 0):
                        negativeEnabled = False
                    else:
                        negativeEnabled = True

                    examData = eval(examData)


                    message = 'success'
                    counter = 100
                    try:
                        examObj = exam_model.objects.latest('exam_ID')
                        counter = int(examObj.exam_ID.split('EX-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        from datetime import date
                        todays_date = date.today()
                        classObj = class_master.objects.get(id=int(classID))
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
                                                                proctor_fk = proctorObj,
                                                                created_by = f"Director - {directorObj.director_FK.director_name}"
                                                                )
                            exam_detailObj.save()

                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Add_Exam'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    exanName = request.POST['examName']
                    examType = request.POST['exam_type']
                    classID = request.POST['classID']
                    negativeEnabled = request.POST['negative_marking_allowed']
                    examData = request.POST['exam_data[]']

                    if(negativeEnabled == 0):
                        negativeEnabled = False
                    else:
                        negativeEnabled = True

                    examData = eval(examData)


                    message = 'success'
                    counter = 100
                    try:
                        examObj = exam_model.objects.latest('exam_ID')
                        counter = int(examObj.exam_ID.split('EX-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        from datetime import date
                        todays_date = date.today()
                        classObj = class_master.objects.get(id=int(classID))
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
                                                                proctor_fk = proctorObj,
                                                                created_by = f"Principal - {directorObj.principal_FK.principal_name}"
                                                                )
                            exam_detailObj.save()

                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')

        


# #####################################################################################################################
# check exam name view
# #####################################################################################################################
# @login_required(login_url='/')
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
# @login_required(login_url='/')
def fetch_class(request):
    if request.method == 'GET':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Exam_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    classList = []
                    if(class_master.objects.filter(branch_FK = branchObj)):
                        for i in class_master.objects.filter(branch_FK = branchObj):
                            context = {}
                            context['id'] = i.id
                            context['class_name'] = i.class_name
                            classList.append(context)
                    return  JsonResponse({'classList':classList})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Exam_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    if(class_master.objects.filter(branch_FK = branchObj)):
                        for i in class_master.objects.filter(branch_FK = branchObj):
                            context = {}
                            context['id'] = i.id
                            context['class_name'] = i.class_name
                            classList.append(context)
                    return  JsonResponse({'classList':classList})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')
        


# #####################################################################################################################
# get teacher view
# #####################################################################################################################
# @login_required(login_url='/')
def fetch_teacher(request):
    if request.method == 'GET':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Exam_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    teacherList = []
                    if(Teacher_profile.objects.filter(branch_FK = branchObj)):
                        for i in Teacher_profile.objects.filter(branch_FK = branchObj):
                            context = {}
                            context['id'] = i.id
                            context['teacher_name'] = i.teacher_FK.teacher_name
                            teacherList.append(context)
                    return  JsonResponse({'teacherList':teacherList})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Exam_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    teacherList = []
                    if(Teacher_profile.objects.filter(branch_FK = branchObj)):
                        for i in Teacher_profile.objects.filter(branch_FK = branchObj):
                            context = {}
                            context['id'] = i.id
                            context['teacher_name'] = i.teacher_FK.teacher_name
                            teacherList.append(context)
                    return  JsonResponse({'teacherList':teacherList})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')

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
# fetch specific exam view
# #####################################################################################################################
# @login_required(login_url='/')
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
# @login_required(login_url='/')
def edit_exam(request,id):
    if request.method == 'GET':
        return render(request,'admin_template/exam-management/edit-details.html')


# #####################################################################################################################
# delete exam view
# #####################################################################################################################
# @login_required(login_url='/')
def delete_exam(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])
        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Delete_Exam'] == True):
                    try:
                        examObj = exam_model.objects.get(id=int(id))
                        examObj.delete()
                        return redirect('exam_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Delete_Exam'] == True):
                    try:
                        examObj = exam_model.objects.get(id=int(id))
                        examObj.delete()
                        return redirect('exam_list')
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
        




