from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from ...models.badge_models import badge_management,badge_trigger_master

# #####################################################################################################################
# badge_list view
# #####################################################################################################################
@login_required(login_url='/')
def badge_list(request):
    if request.method == 'GET':
        badgeObj = badge_management.objects.all().order_by('-id')
        return render(request,'admin_template/badge-management/badge-list.html',{'badgeObj':badgeObj})


# #####################################################################################################################
# add_badge view
# #####################################################################################################################
@login_required(login_url='/')
def add_badge(request):
    if request.method == 'GET':
        batch_triggetObj = badge_trigger_master.objects.all()
        return render(request,'admin_template/badge-management/add-badges.html',{'batch_triggetObj':batch_triggetObj})

    if request.method == 'POST':
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
                                        badge_desrciption = description
                                        )
            badgeObj.save()

            return JsonResponse({'message':message})
        except:
            message = 'failed'
            return JsonResponse({'message':message})


# #####################################################################################################################
# check badge name view
# #####################################################################################################################
@login_required(login_url='/')
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
@login_required(login_url='/')
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
@login_required(login_url='/')
def edit_badge(request,id):
    if request.method == 'GET':
        batchObj = badge_management.objects.get(id=int(id))
        return render(request,'admin_template/badge-management/edit-badge-detail.html',{'batchObj':batchObj})

    if request.method == 'POST':
        description = request.POST['description']
        image = request.FILES.get('image')
        try:
            message = 'success'
            badge_triggetObj = badge_management.objects.get(id=int(id))
            badge_triggetObj.badge_desrciption = description
            if image != None:
                badge_triggetObj.badge_image = image
            badge_triggetObj.save()
            return JsonResponse({'message':message})
        except:
            message = 'failed'
            return JsonResponse({'message':message})


# #####################################################################################################################
# delete badge view
# #####################################################################################################################
@login_required(login_url='/')
def delete_badge(request,id):
    if request.method == 'GET':
        badgeObj = badge_management.objects.get(id=int(id))
        badgeObj.delete()
        return redirect('badge_list')

# #####################################################################################################################



