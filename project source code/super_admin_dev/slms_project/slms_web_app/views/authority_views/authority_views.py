from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.master_models import Authority_master, SubAuthority_master,user_designation_master
from ...models.authority_models import assign_authority
import json
# #####################################################################################################################
# authority_list view
# #####################################################################################################################
@login_required(login_url='/')
def authority_list(request):
    if request.method == 'GET':
        assignedAuthObj = assign_authority.objects.all().order_by('-id')
        for i in assignedAuthObj:
            data = json.loads(i.authority_fk)
            print('data >> ',data)
            i.assign_auth = data
            
        return render(request,'admin_template/authority/authority-list.html',{'assignedAuthObj':assignedAuthObj})

# #####################################################################################################################
# check designation existance view
# #####################################################################################################################
@login_required(login_url='/')
def check_designation(request):
    if request.method == 'GET':
        designationID = request.GET['designation_id']
        message = 'not-exist'
        designationObj = user_designation_master.objects.get(id=int(designationID))
        if(assign_authority.objects.filter(designation_fk = designationObj)):
            message = 'exist'
        return JsonResponse({'message':message})

# #####################################################################################################################
# add new authority view
# #####################################################################################################################
@login_required(login_url='/')
def add_new_authority(request):
    if request.method == 'GET':
        designationObj = user_designation_master.objects.all().order_by('-id')
        SubAuthorityObj = SubAuthority_master.objects.all().order_by('-id')
        counter = 1
        for i in SubAuthorityObj:
            i.counter = counter
            i.subAuthority_name_list = eval(i.subAuthority_name)[0].split(',')
            counter = counter + 1

        return render(request,'admin_template/authority/assign-authorities.html',{'SubAuthorityObj':SubAuthorityObj,'designationObj':designationObj})

    if request.method == 'POST':
        message = 'success'
        designation_id = request.POST.get('designationID')
        authority_array = request.POST.get('authority_array')

        print('designation_id >>> ',designation_id)
        print('authority_array >>> ',authority_array)

        try:
            designationObj = user_designation_master.objects.get(id=int(designation_id))
            if(assign_authority.objects.filter(designation_fk=designationObj)):
                return JsonResponse({'message':'exist'})
            counter = 100
            try:
                assignObj = assign_authority.objects.latest('assign_authorityID')
                counter = int(assignObj.assign_authorityID.split('AUID')[1]) + 1
                print(assignObj.assign_authorityID.split('AUID'))
            except:
                counter = 100
            assign_authObj = assign_authority(assign_authorityID='AUID'+str(counter),designation_fk=designationObj,authority_fk=authority_array)
            assign_authObj.save()
        except:
            message = 'failed'

        return JsonResponse({'message':message})

# #####################################################################################################################
# authority details view
# #####################################################################################################################
@login_required(login_url='/')
def authority_detail(request,id):
    if request.method == 'GET':
        assignObj = assign_authority.objects.get(id=int(id))
        data = json.loads(assignObj.authority_fk)
        assignObj.assign_auth = data
        return render(request,'admin_template/authority/view-detail.html',{'assignObj':assignObj})

# #####################################################################################################################
# authority edit view
# #####################################################################################################################
@login_required(login_url='/')
def edit_authority(request,id):
    if request.method == 'GET':
        assignObj = assign_authority.objects.get(id=int(id))
        data = json.loads(assignObj.authority_fk)
        counter = 1
        for i in data:
            i['counter'] = counter
            counter = counter + 1
        assignObj.assign_auth = data
        return render(request,'admin_template/authority/edit-detail.html',{'assignObj':assignObj})

    if request.method == 'POST':
        message = 'success'
        authority_array = request.POST.get('authority_array')

        try:
            assignObj = assign_authority.objects.get(id=int(id))
            assignObj.authority_fk = authority_array
            assignObj.save()
        except:
            message = 'failed'

        return JsonResponse({'message':message})


# #####################################################################################################################
# delete authority view
# #####################################################################################################################
@login_required(login_url='/')
def delete_authority(request,id):
    if request.method == 'GET':
        assignObj = assign_authority.objects.get(id=int(id))
        assignObj.delete()
        return redirect('authority_list')


