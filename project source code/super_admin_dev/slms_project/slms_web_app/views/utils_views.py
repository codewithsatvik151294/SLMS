from django.shortcuts import redirect
from ..models.authority_models import assign_authority
from ..models.master_models import user_designation_master
import json

def get_auth_dict(request,userType):
    auth_dict = {}
    user_authDict = {}
    if(userType == 'director_login'):
        try:
            designObj = user_designation_master.objects.get(designation_name = 'director')
            userAuthObj = assign_authority.objects.get(designation_fk = designObj)
            user_authDict = json.loads(userAuthObj.authority_fk)
        except:
            auth_dict = {}
        for i in user_authDict:
            auth_dict[i['auth_name'].replace(' ','_')] = i['auth_selected']
        
    elif(userType == 'principal_login'):
        try:
            designObj = user_designation_master.objects.get(designation_name = 'principal')
            userAuthObj = assign_authority.objects.get(designation_fk = designObj)
            user_authDict = json.loads(userAuthObj.authority_fk)
        except:
            auth_dict = {}
        for i in user_authDict:
            auth_dict[i['auth_name'].replace(' ','_')] = i['auth_selected']
        
    elif(userType == 'school_admin_login'):
        try:
            designObj = user_designation_master.objects.get(designation_name = 'school admin')
            userAuthObj = assign_authority.objects.get(designation_fk = designObj)
            user_authDict = json.loads(userAuthObj.authority_fk)
        except:
            auth_dict = {}
        for i in user_authDict:
            auth_dict[i['auth_name'].replace(' ','_')] = i['auth_selected']
        
    return auth_dict


def get_Subauth_dict(request,userType):
    sub_auth_dict = {}
    user_authDict = {}

    if(userType == 'director_login'):
        try:
            designObj = user_designation_master.objects.get(designation_name = 'director')
            userAuthObj = assign_authority.objects.get(designation_fk = designObj)
            user_authDict = json.loads(userAuthObj.authority_fk)
        except:
            auth_dict = {}
        for i in user_authDict:
            for j,k in i['sub_auth'].items():
                sub_auth_dict[j.replace(' ','_')] = k
        
    elif(userType == 'principal_login'):
        try:
            designObj = user_designation_master.objects.get(designation_name = 'principal')
            userAuthObj = assign_authority.objects.get(designation_fk = designObj)
            user_authDict = json.loads(userAuthObj.authority_fk)
        except:
            auth_dict = {}
        for i in user_authDict:
            for j,k in i['sub_auth'].items():
                sub_auth_dict[j.replace(' ','_')] = k
        
    elif(userType == 'school_admin_login'):
        try:
            designObj = user_designation_master.objects.get(designation_name = 'school admin')
            userAuthObj = assign_authority.objects.get(designation_fk = designObj)
            user_authDict = json.loads(userAuthObj.authority_fk)
        except:
            auth_dict = {}
        for i in user_authDict:
            for j,k in i['sub_auth'].items():
                sub_auth_dict[j.replace(' ','_')] = k

    return sub_auth_dict



def check_user_key(request,key):
    if key not in request.session:
        return redirect('logout')