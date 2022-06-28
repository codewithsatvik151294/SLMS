# from django.shortcuts import render,redirect
# from django.http import JsonResponse,HttpResponse
# from django.contrib.auth.decorators import login_required
# from ...models.master_models import class_type_master,subject_master,section_master,Authority_master,SubAuthority_master,user_designation_master,year_master,question_type_master,badge_trigger_master,file_type_master,exam_type_master
# from ...models.manage_models import branch,class_master,topic_master
# '''CLASS TYPE MASTER VIEWS'''
# # #####################################################################################################################
# # classType master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def classType_list(request):
#     if request.method == 'GET':
#         classTypeObj = class_type_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/class-type-list.html',{'classTypeObj':classTypeObj})

# # #####################################################################################################################
# # delete class_type view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_classType(request,id):
#     if request.method == 'GET':
#         class_typeObj = class_type_master.objects.get(id=int(id))
#         class_typeObj.delete()
#         return redirect('classType_list')

# # #####################################################################################################################
# # add classType master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_classType(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             classTypeObj = class_type_master.objects.latest('classTypeID')
#             counter = int(classTypeObj.classTypeID.split('CT')[1]) + 1
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-class-type.html',{'counter':counter})


#     if request.method == 'POST':
#         classTypeName = request.POST['classTypeName']
#         class_subTypeName = request.POST['classSubTypeName']

#         message = 'success'
#         counter = 100
#         try:
#             classTypeObj = class_type_master.objects.latest('classTypeID')
#             counter = int(classTypeObj.classTypeID.split('CT')[1]) + 1
#         except:
#             counter = 100

#         try:
#             if(class_type_master.objects.filter(classType_name=classTypeName.lower(),class_subType_name=class_subTypeName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             class_typeObj = class_type_master(classTypeID=f"CT{counter}",classType_name=classTypeName.lower(),class_subType_name=class_subTypeName.lower())
#             class_typeObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# '''CLASS MASTER VIEWS'''
# # #####################################################################################################################
# # class master list view
# # #####################################################################################################################
# # @login_required(login_url='/')
# def class_list(request):
#     if request.method == 'GET':
#         branchObj = branch.objects.all().order_by('-id')
#         sectionObj = section_master.objects.all().order_by('-id')
#         classObj = class_master.objects.all().order_by('-id')

#         for i in classObj:
#             i.sectionCount = len(eval(i.section_details_fk))
#             subject_array = []
#             for j in eval(i.subject_fk):
#                 subjectObj = subject_master.objects.get(id=int(j))
#                 subject_array.append(subjectObj.subject_name.title())
#             # print(i.subject_fk.all())
#             i.subjectArray = subject_array


#         return render(request,'admin_template/masters/class-list.html',{'branchObj':branchObj,'classObj':classObj,'sectionObj':sectionObj})


# # #####################################################################################################################
# # add class master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_class(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             classObj = class_master.objects.latest('classID')
#             counter = int(classObj.classID.split('CLS')[1]) + 1
#             print(classObj.classID.split('CLS'))
#         except:
#             counter = 100
#         subjectObj = subject_master.objects.all()
#         sectionObj = section_master.objects.all()
#         classTypeObj = class_type_master.objects.all()
#         branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/add-class.html',{'counter':counter,'subjectObj':subjectObj,'sectionObj':sectionObj,'classTypeObj':classTypeObj,'branchObj':branchObj})

#     if request.method == 'POST':
#         branchID = request.POST['branch']
#         className = request.POST['class_name']
#         subject_array = request.POST.getlist('subject_array[]')[0].split(',')
#         section_array = request.POST.getlist('section_array[]')[0].split(',')
#         class_type_array = request.POST.getlist('class_type_array[]')[0].split(',')
#         classDescription = request.POST['class_description']

#         branchObj = branch.objects.get(id=int(branchID))
#         if(class_master.objects.filter(branch_FK=branchObj,class_name = className)):
#             return JsonResponse({"message":'Class already exist'})

#         message = 'success'
#         counter = 100
#         try:
#             classObj = class_master.objects.latest('classID')
#             counter = int(classObj.classID.split('CLS')[1]) + 1
#             print(classObj.classID.split('CLS'))
#         except:
#             counter = 100

#         try:
#             sectionDetails = []
#             for i in range(len(section_array)):
#                 list1 = []
#                 list1.append(section_array[i])
#                 list1.append(class_type_array[i])
#                 sectionDetails.append(list1)
            
#             class_typeObj = class_master(classID=f"CLS{counter}",class_name=className,branch_FK=branchObj,class_description=classDescription,subject_fk=subject_array,section_details_fk=sectionDetails)
#             class_typeObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})
        
# # #####################################################################################################################
# # delete class master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_class(request,id):
#     if request.method == 'GET':
#         classObj = class_master.objects.get(id=int(id))
#         classObj.delete()
#         return redirect('class_list')

# # #####################################################################################################################
# # edit class master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def edit_class_details(request):
#     if request.method == 'GET':
#         # branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/edit-class-details.html',{})


# # #####################################################################################################################
# # view class master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def view_class_details(request,id):
#     if request.method == 'GET':
#         classObj = class_master.objects.get(id=int(id))
#         subject_array = []
#         for j in eval(classObj.subject_fk):
#             subjectObj = subject_master.objects.get(id=int(j))
#             subject_array.append(subjectObj.subject_name.title())
#         classObj.subjectArray = subject_array
#         return render(request,'admin_template/masters/class-details.html',{'classObj':classObj})


# '''section MASTER VIEWS'''
# # #####################################################################################################################
# # section master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def section_list(request):
#     if request.method == 'GET':
#         sectionObj = section_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/section-list.html',{'sectionObj':sectionObj})


# # #####################################################################################################################
# # delete section view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_section(request,id):
#     if request.method == 'GET':
#         sectionObj = section_master.objects.get(id=int(id))
#         sectionObj.delete()
#         return redirect('section_list')

# # #####################################################################################################################
# # add section master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_section(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             sectionObj = section_master.objects.latest('sectionID')
#             counter = int(sectionObj.sectionID.split('SC')[1]) + 1
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-section.html',{"counter":counter})


#     if request.method == 'POST':
#         sectionName = request.POST['sectionName']
#         message = 'success'
#         counter = 100
#         try:
#             sectionObj = section_master.objects.latest('sectionID')
#             counter = int(sectionObj.sectionID.split('SC')[1]) + 1
#             print(sectionObj.sectionID.split('SC'))
#         except:
#             counter = 100

#         try:
#             if(section_master.objects.filter(section_name=sectionName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             sectionObj = section_master(sectionID=f"SC{counter}",section_name=sectionName.lower())
#             sectionObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})

# '''subject MASTER VIEWS'''
# # #####################################################################################################################
# # subject master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def subject_list(request):
#     if request.method == 'GET':
#         subjectObj = subject_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/subject-list.html',{'subjectObj':subjectObj})


# # #####################################################################################################################
# # add subject master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_subject(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             subjectObj = subject_master.objects.latest('subjectID')
#             counter = int(subjectObj.subjectID.split('SUB')[1]) + 1
#             print(subjectObj.subjectID.split('SUB'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-subjects.html',{'counter':counter})

#     if request.method == 'POST':
#         subjectName = request.POST['subjectName']
#         message = 'success'
#         counter = 100
#         try:
#             subjectObj = subject_master.objects.latest('subjectID')
#             counter = int(subjectObj.subjectID.split('SUB')[1]) + 1
#             print(subjectObj.subjectID.split('SUB'))
#         except:
#             counter = 100

#         try:
#             if(subject_master.objects.filter(subject_name=subjectName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             subjectObj = subject_master(subjectID=f"SUB{counter}",subject_name=subjectName.lower())
#             subjectObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # delete subject view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_subject(request,id):
#     if request.method == 'GET':
#         subjectObj = subject_master.objects.get(id=int(id))
#         subjectObj.delete()
#         return redirect('subject_list')


# '''topic MASTER VIEWS'''
# # #####################################################################################################################
# # topic master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def topic_list(request):
#     if request.method == 'GET':
#         branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/topic-list.html',{'branchObj':branchObj})


# # #####################################################################################################################
# # add topic master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_topic(request):
#     if request.method == 'GET':
#         branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/add-topic.html',{'branchObj':branchObj})

#     if request.method == 'POST':
#         branch_id = request.POST['branch_id']
#         class_id = request.POST['class_id']
#         subject_id = request.POST['subject_id']
#         topic_array = request.POST['topic_array']

#         message = 'success'
#         counter = 100
#         try:
#             topicObj = topic_master.objects.latest('topicID')
#             counter = int(topicObj.topicID.split('TP-')[1]) + 1
#         except:
#             counter = 100
        

#         try:
#             branchObj = branch.objects.get(id=int(branch_id))
#             classObj = class_master.objects.get(id=int(class_id))
#             subjectObj = subject_master.objects.get(id=int(subject_id))
            
#             try:
#                 try:
#                     if(topic_master.objects.get(branch_FK=branchObj,class_FK=classObj,subject_FK=subjectObj)):
#                         topicObj = topic_master.objects.get(branch_FK=branchObj,class_FK=classObj,subject_FK=subjectObj)
#                         topicObj.topic_name = "'"+topic_array+"'"
#                         topicObj.save()
#                         return JsonResponse({'message':message})
#                 except:
#                     topicObj = topic_master(topicID=f"TP-{counter}",branch_FK=branchObj,class_FK=classObj,subject_FK=subjectObj,topic_name = "'"+topic_array+"'")
#                     topicObj.save()
#                     return JsonResponse({'message':message})

#             except:
#                 message = 'failed'
#                 return JsonResponse({'message':message})
                    
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # fetch topics view
# # #####################################################################################################################
# @login_required(login_url='/')
# def fetch_topics(request):
#     if request.method == 'GET':
#         branch_id = request.GET['branchID']
#         class_id = request.GET['classID']
#         subject_id = request.GET['subjectID']

#         branchObj = branch.objects.get(id=int(branch_id))
#         classObj = class_master.objects.get(id=int(class_id))
#         subjectObj = subject_master.objects.get(id=int(subject_id))
#         topicsList = []
#         try:
#             topicObj = topic_master.objects.get(branch_FK=branchObj,class_FK=classObj,subject_FK=subjectObj)
#             for i in eval(topicObj.topic_name).split(','):
#                 topicsList.append(i.title())
#         except:
#             topicsList = []

#         return  JsonResponse({'topicsList':topicsList})

# # #####################################################################################################################
# # edit topic master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def edit_topic_details(request):
#     if request.method == 'GET':
#         # branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/edit-topic-details.html',{})


# # #####################################################################################################################
# # view topic master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def view_topic_details(request):
#     if request.method == 'GET':
#         # branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/topic-details.html',{})



# '''authority MASTER VIEWS'''
# # #####################################################################################################################
# # authority master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def authorityList(request):
#     if request.method == 'GET':
#         authorityObj = Authority_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/authority-list.html',{'authorityObj':authorityObj})


# # #####################################################################################################################
# # add authority master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_authority(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             questionTypeObj = Authority_master.objects.latest('authorityID')
#             counter = int(questionTypeObj.authorityID.split('AUTH')[1]) + 1
#             print(questionTypeObj.authorityID.split('AUTH'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-authority.html',{'counter':counter})


#     if request.method == 'POST':
#         authorityName = request.POST['authorityName']
#         message = 'success'
#         counter = 100
#         try:
#             authorityObj = Authority_master.objects.latest('authorityID')
#             counter = int(authorityObj.authorityID.split('AUTH')[1]) + 1
#             print(authorityObj.authorityID.split('AUTH'))
#         except:
#             counter = 100

#         try:
#             if(Authority_master.objects.filter(authority_name=authorityName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             authorityObj = Authority_master(authorityID=f"AUTH{counter}",authority_name=authorityName.lower())
#             authorityObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # delete authority view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_authority(request,id):
#     if request.method == 'GET':
#         authorityObj = Authority_master.objects.get(id=int(id))
#         authorityObj.delete()
#         return redirect('authorityList')

# # #####################################################################################################################
# # check authority view
# # #####################################################################################################################
# @login_required(login_url='/')
# def check_authority(request):
#     authorityID = request.GET['Auth_ID']
#     message = 'not-exist'
    
#     if(SubAuthority_master.objects.filter(authority_FK=Authority_master.objects.get(id=int(authorityID)))):
#         message = 'exist'
#     return JsonResponse({'message':message})


# '''sub-authority MASTER VIEWS'''
# # #####################################################################################################################
# # sub-authority master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def sub_authority_list(request):
#     if request.method == 'GET':
#         subAuthorityObj = SubAuthority_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/sub-authority-list.html',{'subAuthorityObj':subAuthorityObj})

# # #####################################################################################################################
# # delete sub_authority view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_sub_authority(request,id):
#     if request.method == 'GET':
#         sub_authorityObj = SubAuthority_master.objects.get(id=int(id))
#         sub_authorityObj.delete()
#         return redirect('sub_authority_list')

# # #####################################################################################################################
# # add sub-authority master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_sub_authority(request):
#     if request.method == 'GET':
#         authorityObj = Authority_master.objects.all()
#         counter = 100
#         try:
#             authority_Obj = SubAuthority_master.objects.latest('subAuthorityID')
#             counter = int(authority_Obj.subAuthorityID.split('S-AUTH')[1]) + 1
#             print(authority_Obj.subAuthorityID.split('S-AUTH'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-sub-authority.html',{'counter':counter,'authorityObj':authorityObj})


#     if request.method == 'POST':
#         authority_id = request.POST['authorityID']
#         sub_auth_array = request.POST.getlist('sub_auth_array[]')

#         message = 'success'
#         counter = 100
#         try:
#             authorityObj = SubAuthority_master.objects.latest('subAuthorityID')
#             counter = int(authorityObj.subAuthorityID.split('S-AUTH')[1]) + 1
#             print(authorityObj.subAuthorityID.split('S-AUTH'))
#         except:
#             counter = 100

#         try:
#             try:
#                 if(SubAuthority_master.objects.filter(authority_FK=Authority_master.objects.get(id=int(authority_id)))):
#                     message = 'data exist'
#                     return JsonResponse({'message':message})
#             except:
#                 pass
            
#             subAuthorityObj = SubAuthority_master(subAuthorityID=f"S-AUTH{counter}",subAuthority_name=sub_auth_array,authority_FK=Authority_master.objects.get(id=int(authority_id)))
#             subAuthorityObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # edit sub-authority master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def edit_sub_authority_details(request,id):
#     if request.method == 'GET':
#         SubAuthorityObj = SubAuthority_master.objects.get(id=int(id))
#         return render(request,'admin_template/masters/edit-sub-authority.html',{'SubAuthorityObj':SubAuthorityObj})

#     if request.method == 'POST':
#         sub_auth_array = request.POST.getlist('sub_auth_array[]')
#         message = 'success'
#         try:
#             subAuth_obj = SubAuthority_master.objects.get(id=int(id))
#             subAuth_obj.subAuthority_name=sub_auth_array
#             subAuth_obj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # view sub-authority master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def view_sub_authority_details(request):
#     if request.method == 'GET':
#         # branchObj = branch.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/sub-authority-details.html',{})


# '''designation MASTER VIEWS'''
# # #####################################################################################################################
# # designation master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def designation_list(request):
#     if request.method == 'GET':
#         designationObj = user_designation_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/designation-list.html',{'designationObj':designationObj})


# # #####################################################################################################################
# # add designation master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_designation(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             designationObj = user_designation_master.objects.latest('designationID')
#             counter = int(designationObj.designationID.split('DG')[1]) + 1
#             print(designationObj.designationID.split('DG'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-designation.html',{'counter':counter})


#     if request.method == 'POST':
#         designationName = request.POST['designationName']
#         message = 'success'
#         counter = 100
#         try:
#             designationObj = user_designation_master.objects.latest('designationID')
#             counter = int(designationObj.designationID.split('DG')[1]) + 1
#             print(designationObj.designationID.split('DG'))
#         except:
#             counter = 100

#         try:
#             if(user_designation_master.objects.filter(designation_name=designationName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             designationObj = user_designation_master(designationID=f"DG{counter}",designation_name=designationName.lower())
#             designationObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})

# # #####################################################################################################################
# # delete sub_authority view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_designation(request,id):
#     if request.method == 'GET':
#         designationObj = user_designation_master.objects.get(id=int(id))
#         designationObj.delete()
#         return redirect('designation_list')

# '''year MASTER VIEWS'''
# # #####################################################################################################################
# # year master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def year_list(request):
#     if request.method == 'GET':
#         yearObj = year_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/year-list.html',{'yearObj':yearObj})


# # #####################################################################################################################
# # add year master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_year(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             yearObj = year_master.objects.latest('yearID')
#             counter = int(yearObj.yearID.split('YR')[1]) + 1
#             print(yearObj.yearID.split('YR'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-year.html',{'counter':counter})


#     if request.method == 'POST':
#         year = request.POST['year']
#         message = 'success'
#         counter = 100
#         try:
#             yearObj = year_master.objects.latest('yearID')
#             counter = int(yearObj.yearID.split('YR')[1]) + 1
#             print(yearObj.yearID.split('YR'))
#         except:
#             counter = 100

#         try:
#             if(year_master.objects.filter(year_name=year.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             yearObj = year_master(yearID=f"YR{counter}",year_name=year.lower())
#             yearObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # delete year type view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_year(request,id):
#     if request.method == 'GET':
#         yearObj = year_master.objects.get(id=int(id))
#         yearObj.delete()
#         return redirect('year_list')


# '''Question type MASTER VIEWS'''
# # #####################################################################################################################
# # question_type master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def question_type_list(request):
#     if request.method == 'GET':
#         question_typeObj = question_type_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/question-type-list.html',{'question_typeObj':question_typeObj})


# # #####################################################################################################################
# # add question_type master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_question_type(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             questionTypeObj = question_type_master.objects.latest('questionTypeID')
#             counter = int(questionTypeObj.questionTypeID.split('QT')[1]) + 1
#             print(questionTypeObj.questionTypeID.split('QT'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-question-type.html',{'counter':counter})

#     if request.method == 'POST':
#         questionTypeName = request.POST['questionTypeName']
#         message = 'success'
#         counter = 100
#         try:
#             questionTypeObj = question_type_master.objects.latest('questionTypeID')
#             counter = int(questionTypeObj.questionTypeID.split('QT')[1]) + 1
#             print(questionTypeObj.questionTypeID.split('QT'))
#         except:
#             counter = 100

#         try:
#             if(question_type_master.objects.filter(questionType_name=questionTypeName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             questionTypeObj = question_type_master(questionTypeID=f"QT{counter}",questionType_name=questionTypeName.lower())
#             questionTypeObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})

# # #####################################################################################################################
# # delete question type view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_questionType(request,id):
#     if request.method == 'GET':
#         questionTypeObj = question_type_master.objects.get(id=int(id))
#         questionTypeObj.delete()
#         return redirect('question_type_list')


# '''Badge_trigger MASTER VIEWS'''
# # #####################################################################################################################
# # badge_trigger master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def badge_trigger_list(request):
#     if request.method == 'GET':
#         badge_triggerObj = badge_trigger_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/badge-trigger-list.html',{'badge_triggerObj':badge_triggerObj})


# # #####################################################################################################################
# # add badge_trigger master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_badge_trigger(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             badge_triggerObj = badge_trigger_master.objects.latest('badge_triggerID')
#             counter = int(badge_triggerObj.badge_triggerID.split('BDG')[1]) + 1
#             print(badge_triggerObj.badge_triggerID.split('BDG'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-badge-trigger.html',{'counter':counter})


#     if request.method == 'POST':
#         badge_triggerName = request.POST['badgeName']
#         message = 'success'
#         counter = 100
#         try:
#             badge_triggerObj = badge_trigger_master.objects.latest('badge_triggerID')
#             counter = int(badge_triggerObj.badge_triggerID.split('BDG')[1]) + 1
#             print(badge_triggerObj.badge_triggerID.split('BDG'))
#         except:
#             counter = 100

#         try:
#             if(badge_trigger_master.objects.filter(badge_trigger_name=badge_triggerName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             badge_triggerObj = badge_trigger_master(badge_triggerID=f"BDG{counter}",badge_trigger_name=badge_triggerName.lower())
#             badge_triggerObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})

# # #####################################################################################################################
# # delete delete_badge_trigger view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_badge_trigger(request,id):
#     if request.method == 'GET':
#         badge_triggerObj = badge_trigger_master.objects.get(id=int(id))
#         badge_triggerObj.delete()
#         return redirect('badge_trigger_list')
        

# '''file_type MASTER VIEWS'''
# # #####################################################################################################################
# # file_type master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def file_type_list(request):
#     if request.method == 'GET':
#         file_typeObj = file_type_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/file-type-list.html',{'file_typeObj':file_typeObj})



# # #####################################################################################################################
# # add file_type master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_file_type(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             fileTypeObj = file_type_master.objects.latest('file_typeID')
#             counter = int(fileTypeObj.file_typeID.split('FT')[1]) + 1
#             print(fileTypeObj.file_typeID.split('FT'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-file-type.html',{'counter':counter})


#     if request.method == 'POST':
#         fileTypeName = request.POST['fileTypeName']
#         message = 'success'
#         counter = 100
#         try:
#             fileTypeObj = file_type_master.objects.latest('file_typeID')
#             counter = int(fileTypeObj.file_typeID.split('FT')[1]) + 1
#             print(fileTypeObj.file_typeID.split('FT'))
#         except:
#             counter = 100

#         try:
#             if(file_type_master.objects.filter(file_type_name=fileTypeName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             fileTypeObj = file_type_master(file_typeID=f"FT{counter}",file_type_name=fileTypeName.lower())
#             fileTypeObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # delete file_type view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_file_type(request,id):
#     if request.method == 'GET':
#         fileTypeObj = file_type_master.objects.get(id=int(id))
#         fileTypeObj.delete()
#         return redirect('file_type_list')



# # #####################################################################################################################
# # get sections & class type view
# # #####################################################################################################################
# @login_required(login_url='/')
# def get_section_and_class_type(request):
#     if request.method == 'GET':
#         sectionList = []
#         class_typeList = []
#         sectionObj = section_master.objects.all()
#         classTypeObj = class_type_master.objects.all()

#         for i in sectionObj:
#             context = {}
#             context['id'] = i.id
#             context['section_name'] = i.section_name.title()
#             sectionList.append(context)

#         for i in classTypeObj:
#             context = {}
#             context['id'] = i.id
#             context['class_type_name'] = f"{i.classType_name.title()} - {i.class_subType_name.title()}"
#             class_typeList.append(context)

#         return JsonResponse({'sectionData':sectionList,'class_typeData':class_typeList})

# '''Questio  type master'''
# # question_type master list view
# # #####################################################################################################################
# @login_required(login_url='/')
# def exam_type_list(request):
#     if request.method == 'GET':
#         exam_typeObj = exam_type_master.objects.all().order_by('-id')
#         return render(request,'admin_template/masters/exam-type-list.html',{'exam_typeObj':exam_typeObj})


# # #####################################################################################################################    
# # add file_type master view
# # #####################################################################################################################
# @login_required(login_url='/')
# def add_exam_type(request):
#     if request.method == 'GET':
#         counter = 100
#         try:
#             examTypeObj = exam_type_master.objects.latest('exam_typeID')
#             counter = int(examTypeObj.exam_typeID.split('ET')[1]) + 1
#             print(examTypeObj.exam_typeID.split('ET'))
#         except:
#             counter = 100
#         return render(request,'admin_template/masters/add-exam-type.html',{'counter':counter})


#     if request.method == 'POST':
#         examTypeName = request.POST['examTypeName']
#         message = 'success'
#         counter = 100
#         try:
#             examTypeObj = exam_type_master.objects.latest('exam_typeID')
#             counter = int(examTypeObj.exam_typeID.split('ET')[1]) + 1
#             print(examTypeObj.exam_typeID.split('ET'))
#         except:
#             counter = 100

#         try:
#             if(exam_type_master.objects.filter(exam_type_name=examTypeName.lower())):
#                 message = 'data exist'
#                 return JsonResponse({'message':message})
            
#             examTypeObj = exam_type_master(exam_typeID=f"ET{counter}",exam_type_name=examTypeName.lower())
#             examTypeObj.save()
#             return JsonResponse({'message':message})
#         except:
#             message = 'failed'
#             return JsonResponse({'message':message})


# # #####################################################################################################################
# # delete file_type view
# # #####################################################################################################################
# @login_required(login_url='/')
# def delete_exam_type(request,id):
#     if request.method == 'GET':
#         examTypeObj = exam_type_master.objects.get(id=int(id))
#         examTypeObj.delete()
#         return redirect('exam_type_list')



# # #####################################################################################################################