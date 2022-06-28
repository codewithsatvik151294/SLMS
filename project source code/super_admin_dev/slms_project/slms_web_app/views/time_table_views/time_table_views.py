from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.master_models import *
from ...models.manage_models import *
from ...models.time_table_models import time_table_model
import json
# #####################################################################################################################
# time table list view
# #####################################################################################################################
@login_required(login_url='/')
def add_time_table(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        yearObj = year_master.objects.all().order_by('-id')
        return render(request,'admin_template/time-table-management/add-timetable.html',{'branchObj':branchObj,'yearObj':yearObj})

    if request.method == 'POST':
        message = 'success'
        branch_id =  request.POST["branch_id"]
        session =  request.POST["session"]
        year_id =  request.POST["year_id"]
        effective_from =  request.POST["effective_from"]
        class_id =  request.POST["class_id"]
        section_id =  request.POST["section_id"]
        mondaySlot =  request.POST["monday_slot[]"]
        tuesdaySlot =  request.POST["tuesday_slot[]"]
        wednesdaySlot =  request.POST["wednesday_slot[]"]
        thursdaySlot =  request.POST["thursday_slot[]"]
        fridaySlot =  request.POST["friday_slot[]"]
        saturdaySlot =  request.POST["saturday_slot[]"]

        print('branch_id >>> ',branch_id)
        print('session >>> ',session)
        print('year_id >>> ',year_id)
        print('effective_from >>> ',effective_from)
        print('class_id >>> ',class_id)
        print('section_id >>> ',section_id)
        print('monday_slot >>> ',mondaySlot)
        print('tuesday_slot >>> ',tuesdaySlot)
        print('wednesday_slot >>> ',wednesdaySlot)
        print('thursday_slot >>> ',thursdaySlot)
        print('friday_slot >>> ',fridaySlot)
        print('saturday_slot >>> ',saturdaySlot)

        try:
            counter = 100
            try:
                timetableObj = time_table_model.objects.latest('time_table_ID')
                counter = int(time_table_model.time_table_ID.split('TT-')[1]) + 1
            except:
                counter = 100
            time_tableObj = time_table_model(time_table_ID = f"TT-{counter}",
                                            time_table_session = session,
                                            time_table_effective_from = str(effective_from),
                                            year_fk = year_master.objects.get(id=int(year_id)),
                                            branch_fk = branch.objects.get(id=int(branch_id)),
                                            class_fk = class_master.objects.get(id=int(class_id)),
                                            section_fk = section_master.objects.get(id=int(section_id)),
                                            monday_slot = mondaySlot,
                                            tuesday_slot = tuesdaySlot,
                                            wednesday_slot = wednesdaySlot,
                                            thursday_slot = thursdaySlot,
                                            friday_slot = fridaySlot,
                                            saturday_slot = saturdaySlot,
                                        )
            time_tableObj.save()
        except:
            message = 'failed'


        return JsonResponse({'message':message})

# #####################################################################################################################
# view_time_table view
# #####################################################################################################################
@login_required(login_url='/')
def view_time_table(request):
    if request.method == 'GET':
        branchObj = branch.objects.all().order_by('-id')
        yearObj = year_master.objects.all().order_by('-id')
        return render(request,'admin_template/time-table-management/timetable-list.html',{'branchObj':branchObj,'yearObj':yearObj})



# # #####################################################################################################################
# # get teacher view
# # #####################################################################################################################
@login_required(login_url='/')
def get_teacher(request):
    if request.method == 'GET':
        responseList = []
        branch_id  = request.GET['branch_id']
        class_id  = request.GET['class_id']
        section_id  = request.GET['section_id']
        subject_id  = request.GET['subject_id']

        branchObj = branch.objects.get(id=int(branch_id))
        substring = str([int(class_id),int(section_id),int(subject_id)])
        teacherObj = Teacher_profile.objects.filter(branch_FK=branchObj,class_section_subject_detail_fk__icontains=substring)
        for i in teacherObj:
            context = {}
            context['id'] = i.id
            context['teacher_name'] = i.teacher_FK.teacher_name.title()
            responseList.append(context)

        return JsonResponse({'response':responseList})


# # #####################################################################################################################
# filter_time_table view
# #####################################################################################################################
@login_required(login_url='/')
def filter_time_table(request):
    if request.method == 'GET':
        responseList = []
        branch_id =  request.GET["branchId"]
        session =  request.GET["session"]
        year_id =  request.GET["year_id"]
        effective_from =  request.GET["effective_from"]
        class_id =  request.GET["class_id"]
        section_id =  request.GET["section_id"]

        timeTableObj = time_table_model.objects.filter(time_table_session = session,
                                                        time_table_effective_from = str(effective_from),
                                                        year_fk = year_master.objects.get(id=int(year_id)),
                                                        branch_fk = branch.objects.get(id=int(branch_id)),
                                                        class_fk = class_master.objects.get(id=int(class_id)),
                                                        section_fk = section_master.objects.get(id=int(section_id)))

        for i in timeTableObj:
            context = {}
            context['id'] = i.id
            context['monday_slot'] = json.loads(i.monday_slot)
            context['tuesday_slot'] = json.loads(i.tuesday_slot)
            context['wednesday_slot'] = json.loads(i.wednesday_slot)
            context['thursday_slot'] = json.loads(i.thursday_slot)
            context['friday_slot'] = json.loads(i.friday_slot)
            context['saturday_slot'] = json.loads(i.saturday_slot)
            context['slots_count'] = len(json.loads(i.saturday_slot))

            responseList.append(context)

        print('responseList >>> ',responseList)
        


        return JsonResponse({'response':responseList})






