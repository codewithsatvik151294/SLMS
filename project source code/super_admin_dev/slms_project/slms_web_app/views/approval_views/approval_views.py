from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.paper_models import *
from ...models.exam_models import *
from ...models.studey_material_models import *
from ...models.assignment_models import *

# #####################################################################################################################
# exam approval list view
# #####################################################################################################################
@login_required(login_url='/')
def exam_approval_list(request):
    if request.method == 'GET':
        examObj = exam_model.objects.filter(approved_status='3').order_by('-id')
        print('examObj >>> ',examObj)
        return render(request,'admin_template/approval-management/exam.html',{'examObj':examObj})


@login_required(login_url='/')
def fetch_exam(request):
    if request.method == 'GET':
        examID = request.GET['examID']
        paperList = []
        examDict = {}
        try:
            examObj = exam_model.objects.get(id=int(examID))
            examDict['exam_id'] = examObj.exam_ID
            examDict['exam_name'] = examObj.exam_name
            examDict['class'] = examObj.class_fk.class_name.lower()
            examDict['total_papers'] = examObj.total_papers
            examDict['exam_type'] = examObj.exam_type_fk.exam_type_name
            examDict['branch_FK'] = examObj.branch_FK.branch_name

            for i in exam_paper_detail.objects.filter(exam_fk = examObj):
                context = {}
                context['paper_name'] = i.paper_fk.paper_name
                context['subject'] = i.paper_fk.subject_fk.subject_name
                context['Year'] = i.paper_fk.year_fk.year_name
                context['start'] = i.exam_start_date_time.strftime("%d-%b-%Y")

                context['end'] = i.exam_end_date_time.strftime("%d-%b-%Y")

                context['proctor'] = i.proctor_fk.teacher_FK.teacher_name

                paperList .append(context)
            

        except:
            paperList = []

        return JsonResponse({'examDict':examDict,'paperList':paperList})


@login_required(login_url='/')
def approve_exam(request,id):
    if request.method == 'GET':
        examObj = exam_model.objects.get(id=int(id))
        examObj.approved_status = '1'
        examObj.save()
        return redirect('exam_approval_list')

@login_required(login_url='/')
def reject_exam(request,id):
    if request.method == 'GET':
        examObj = exam_model.objects.get(id=int(id))
        examObj.approved_status = '2'
        examObj.save()
        return redirect('exam_approval_list')

# #####################################################################################################################
# paper approval list view
# #####################################################################################################################
@login_required(login_url='/')
def paper_approval_list(request):
    if request.method == 'GET':
        badgeObj = {}
        return render(request,'admin_template/approval-management/paper.html',{'badgeObj':badgeObj})



# #####################################################################################################################
# assignment approval list view
# #####################################################################################################################
@login_required(login_url='/')
def assignment_approval_list(request):
    if request.method == 'GET':
        badgeObj = {}
        return render(request,'admin_template/approval-management/assignment.html',{'badgeObj':badgeObj})


# #####################################################################################################################
# study_material approval list view
# #####################################################################################################################
@login_required(login_url='/')
def study_material_approval_list(request):
    if request.method == 'GET':
        badgeObj = {}
        return render(request,'admin_template/approval-management/study-material.html',{'badgeObj':badgeObj})






