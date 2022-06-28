# from django.shortcuts import render,redirect
# from django.http import JsonResponse,HttpResponse
# from django.contrib.auth.decorators import login_required
# from ...models.manage_models import branch
# from .resorces import branch_record
# from tablib import Dataset
# from django.contrib import messages

# # #####################################################################################################################
# # branch_list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def branch_list(request):
#     if request.method == 'GET':
#         branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/manage-type/branch/branch.html',{'branchObj':branchObj})

# # #####################################################################################################################
# # add new branch view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_new_branch(request):
#     if request.method == 'GET':
#         return render(request,'admin_template/manage-type/branch/add-branch.html')

#     if request.method == 'POST':
#         message = 'success'
#         branchCode = request.POST.get('branchCode')
#         branchName = request.POST.get('branchName')
#         branchEmail = request.POST.get('branchEmail')
#         branchContact = request.POST.get('branchContact')
#         branchAddress = request.POST.get('branchAddress')
#         branchPinCode = request.POST.get('branchPinCode')
#         branchCity = request.POST.get('branchCity')
#         branchState = request.POST.get('branchState')

#         try:
#             branchObj = branch(branch_code=branchCode,branch_name=branchName,branch_email=branchEmail,branch_contact=branchContact,branch_address=branchAddress,branch_pinCode=branchPinCode,branch_city=branchCity,branch_state=branchState)
#             branchObj.save()
#         except:
#             message = 'failed'

#         return JsonResponse({'message':message})

# # #####################################################################################################################
# # upload branch list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def upload_branch_list(request):
#     if request.method == 'GET':
#         return render(request,'admin_template/manage-type/branch/upload-branch-list.html')

#     if request.method == 'POST':
#         sales_resource = branch()
#         dataSet = Dataset()
#         new_branch_sheet = request.FILES.get('myfile')

#         print('new_branch_sheet >>> ',new_branch_sheet)
#         if(new_branch_sheet == None):
#             messages.info(request,'Select a valid .xlsx file')
#             return render(request,'admin_template/manage-type/branch/upload-branch-list.html')

#         if not new_branch_sheet.name.endswith('.xlsx'):
#             messages.info(request,'wrong file format.')
#             return render(request,'admin_template/manage-type/branch/upload-branch-list.html')

#         imported_data = dataSet.load(new_branch_sheet.read(),format='xlsx')
#         context = {}

#         try:
#             counter = 0
#             for data in imported_data:
#                 latestID = branch.objects.latest('id')
#                 print('latestID >>> ',latestID.id)
#                 value = branch(
#                     int(latestID.id)+1,
#                     data[0],
#                     data[1],
#                     data[2],
#                     data[3],
#                     data[4],
#                     data[5],
#                     data[6],
#                     data[7],
#                 )
#                 try:
#                     value.save()
#                     counter = counter +1
#                 except Exception as e:
#                     s = str(e)
#                     print(s)

#             messages.info(request,'File Uploaded Successfully')
#         except:
#             context['counter'] = counter
#             messages.info(request,'Same file already uploaded.')
            
#         return render(request,'admin_template/manage-type/branch/upload-branch-list.html',{'counter':counter})

# # #####################################################################################################################
# # branch details view
# # #####################################################################################################################
# @login_required(login_url='/')
# def branch_detail(request,id):
#     if request.method == 'GET':
#         branchObj = branch.objects.get(id=int(id))
#         return render(request,'admin_template/manage-type/branch/branch-details.html',{'branchObj':branchObj})

# # #####################################################################################################################
# # branch edit view
# # #####################################################################################################################
# @login_required(login_url='/')
# def edit_branch(request,id):
#     if request.method == 'GET':
#         branchObj = branch.objects.get(id=int(id))
#         return render(request,'admin_template/manage-type/branch/edit-branch-details.html',{'branchObj':branchObj})

#     if request.method == 'POST':
#         message = 'success'
#         branchCode = request.POST.get('branchCode')
#         branchName = request.POST.get('branchName')
#         branchEmail = request.POST.get('branchEmail')
#         branchContact = request.POST.get('branchContact')
#         branchAddress = request.POST.get('branchAddress')
#         branchPinCode = request.POST.get('branchPinCode')
#         branchCity = request.POST.get('branchCity')
#         branchState = request.POST.get('branchState')

#         try:
#             branchObj = branch.objects.get(id=int(id))
#             branchObj.branch_code=branchCode
#             branchObj.branch_name=branchName
#             branchObj.branch_email=branchEmail
#             branchObj.branch_contact=branchContact
#             branchObj.branch_address=branchAddress
#             branchObj.branch_pinCode=branchPinCode
#             branchObj.branch_city=branchCity
#             branchObj.branch_state=branchState
#             branchObj.save()
#         except:
#             message = 'failed'

#         return JsonResponse({'message':message})


# # #####################################################################################################################
# # delete branch view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_branch(request,id):
#     if request.method == 'GET':
#         branchObj = branch.objects.get(id=int(id))
#         branchObj.delete()
#         return redirect('branch_list')


# # #####################################################################################################################
# # branch fields check view
# # #####################################################################################################################
# @login_required(login_url='/')
# def field_check(request):
#     if request.method == 'GET':
#         message = 'not-exist'
#         fieldType = request.GET['fieldType']
#         searchString = request.GET['searchString']

#         if(fieldType == 'branchCode'):
#             branchObj = branch.objects.filter(branch_code=searchString)
#             if(branchObj):
#                 message = 'branch-code-exist'

#         elif(fieldType == 'branchName'):
#             branchObj = branch.objects.filter(branch_name=searchString)
#             if(branchObj):
#                 message = 'branch-name-exist'

#         elif(fieldType == 'branchEmail'):
#             branchObj = branch.objects.filter(branch_email=searchString)
#             if(branchObj):
#                 message = 'branch-email-exist'

#         elif(fieldType == 'branchContact'):
#             branchObj = branch.objects.filter(branch_contact=searchString)
#             if(branchObj):
#                 message = 'branch-contact-exist'

#         return JsonResponse({'message':message})