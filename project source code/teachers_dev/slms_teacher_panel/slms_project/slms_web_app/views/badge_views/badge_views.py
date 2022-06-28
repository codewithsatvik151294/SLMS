from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.badge_models import badge_management,badge_trigger_master
from ..utils_views import get_auth_dict,get_Subauth_dict
import datetime
from ...models.manage_models import branch,schoolAdmin_profile,Teacher_profile,Teacher_profile
import datetime
# #####################################################################################################################
# badge_list view
# #####################################################################################################################
# @login_required(login_url='/')
def badge_list(request):
    if request.method == 'GET':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Badge_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    badgeObj = badge_management.objects.all().order_by('-id')
                    return render(request,'admin_template/badge-management/badge-list.html',{'branchObj':branchObj,'badgeObj':badgeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Badge_List'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    branchObj = branch.objects.get(id=int(directorObj.branch_FK.id))
                    badgeObj = badge_management.objects.all().order_by('-id')
                    return render(request,'admin_template/badge-management/badge-list.html',{'branchObj':branchObj,'badgeObj':badgeObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# add_badge view
# #####################################################################################################################
# @login_required(login_url='/')
def add_badge(request):
    if request.method == 'GET':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])

        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Add_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    batch_triggetObj = badge_trigger_master.objects.all()
                    return render(request,'admin_template/badge-management/add-badges.html',{'batch_triggetObj':batch_triggetObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Add_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    batch_triggetObj = badge_trigger_master.objects.all()
                    return render(request,'admin_template/badge-management/add-badges.html',{'batch_triggetObj':batch_triggetObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
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
                if(sub_auth_dict['Add_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    title = request.POST['title']
                    trigger = request.POST['trigger']
                    description = request.POST['description']
                    image = request.FILES.get('image')

                    message = 'success'
                    counter = 100
                    try:
                        badgeObj = badge_management.objects.latest('badge_ID')
                        counter = int(badgeObj.badge_ID.split('BDG-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        badge_triggetObj = badge_trigger_master.objects.get(id=int(trigger))
                        badgeObj = badge_management(badge_ID = 'BDG-'+str(counter),
                                                    badge_title = title.lower(),
                                                    badge_trigger_fk = badge_triggetObj,
                                                    badge_image = image,
                                                    badge_desrciption = description,
                                                    created_by = f"Director - {directorObj.director_FK.director_name}"
                                                    )
                        badgeObj.save()

                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})

                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Add_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    title = request.POST['title']
                    trigger = request.POST['trigger']
                    description = request.POST['description']
                    image = request.FILES.get('image')

                    message = 'success'
                    counter = 100
                    try:
                        badgeObj = badge_management.objects.latest('badge_ID')
                        counter = int(badgeObj.badge_ID.split('BDG-')[1]) + 1
                    except:
                        counter = 100

                    try:
                        badge_triggetObj = badge_trigger_master.objects.get(id=int(trigger))
                        badgeObj = badge_management(badge_ID = 'BDG-'+str(counter),
                                                    badge_title = title.lower(),
                                                    badge_trigger_fk = badge_triggetObj,
                                                    badge_image = image,
                                                    badge_desrciption = description,
                                                    created_by = f"Principal - {directorObj.principal_FK.principal_name}"
                                                    )
                        badgeObj.save()

                        return JsonResponse({'message':message})
                    except:
                        message = 'failed'
                        return JsonResponse({'message':message})
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
        

# #####################################################################################################################
# check badge name view
# #####################################################################################################################
# @login_required(login_url='/')
def check_badge_title(request):
    if request.method == 'GET':
        message = 'not-exisit'
        searchString = request.GET['search_string']
        if(badge_management.objects.filter(badge_title = searchString.lower())):
            message = 'exist'

        return  JsonResponse({'message':message})


# #####################################################################################################################
# check badge trigger view
# #####################################################################################################################
# @login_required(login_url='/')
def check_badge_trigger(request):
    if request.method == 'GET':
        message = 'not-exisit'
        searchString = request.GET['search_string']
        badge_triggetObj = badge_trigger_master.objects.get(id=int(searchString))
        if(badge_management.objects.filter(badge_trigger_fk = badge_triggetObj)):
            message = 'exist'

        return  JsonResponse({'message':message})


# #####################################################################################################################
# edit specific badge
# #####################################################################################################################
# @login_required(login_url='/')
def edit_badge(request,id):
    if request.method == 'GET':
        if 'userType' not in request.session:
            return redirect('logout')
        auth_dict = get_auth_dict(request,request.session['userType'])
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])
        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Edit_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    try:
                        batchObj = badge_management.objects.get(id=int(id))
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/badge-management/edit-badge-detail.html',{'batchObj':batchObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Edit_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    try:
                        batchObj = badge_management.objects.get(id=int(id))
                    except:
                        return render(request,'403.html')
                    return render(request,'admin_template/badge-management/edit-badge-detail.html',{'batchObj':batchObj,'auth_dict':auth_dict,'sub_auth_dict':sub_auth_dict})

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
                if(sub_auth_dict['Edit_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    try:
                        batchObj = badge_management.objects.get(id=int(id))
                        description = request.POST['description']
                        image = request.FILES.get('image')
                        try:
                            message = 'success'
                            badge_triggetObj = badge_management.objects.get(id=int(id))
                            badge_triggetObj.badge_desrciption = description
                            if image != None:
                                badge_triggetObj.badge_image = image
                            badge_triggetObj.last_updated_by = f"Director - {directorObj.director_FK.director_name}"
                            badge_triggetObj.last_updated_at = datetime.datetime.now()
                            badge_triggetObj.save()
                            return JsonResponse({'message':message})
                        except:
                            message = 'failed'
                            return JsonResponse({'message':message})
                    except:
                        return render(request,'403.html')
                    
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Edit_Badge'] == True):
                    directorObj = Teacher_profile.objects.get(id=int(request.session['teacher_id']))
                    try:
                        batchObj = badge_management.objects.get(id=int(id))
                        description = request.POST['description']
                        image = request.FILES.get('image')
                        try:
                            message = 'success'
                            badge_triggetObj = badge_management.objects.get(id=int(id))
                            badge_triggetObj.badge_desrciption = description
                            if image != None:
                                badge_triggetObj.badge_image = image
                            badge_triggetObj.last_updated_by = f"Principal - {directorObj.principal_FK.principal_name}"
                            badge_triggetObj.last_updated_at = datetime.datetime.now()
                            badge_triggetObj.save()
                            return JsonResponse({'message':message})
                        except:
                            message = 'failed'
                            return JsonResponse({'message':message})
                    except:
                        return render(request,'403.html')
                    
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')


# #####################################################################################################################
# delete badge view
# #####################################################################################################################
# @login_required(login_url='/')
def delete_badge(request,id):
    if request.method == 'GET':
        sub_auth_dict = get_Subauth_dict(request,request.session['userType'])
        if 'userType' in request.session:
            if(request.session['userType'] == 'teacher_login'):
                if(sub_auth_dict['Delete_Badge'] == True):
                    try:
                        badgeObj = badge_management.objects.get(id=int(id))
                        badgeObj.delete()
                        return redirect('badge_list')  
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')

            elif(request.session['userType'] == 'class_teacher_login'):
                if(sub_auth_dict['Delete_Badge'] == True):
                    try:
                        badgeObj = badge_management.objects.get(id=int(id))
                        badgeObj.delete()
                        return redirect('badge_list')  
                    except:
                        return render(request,'403.html')
                else:
                    return render(request,'403.html')
        else:
            return render(request,'admin_template/auth/login.html')
# #####################################################################################################################



