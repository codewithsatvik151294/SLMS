import imp
from django.urls import path
from ..views.master_views.master_views import *


urlpatterns = [
    # manage class-type-master URLS
    path('class-type-list', classType_list,name='classType_list'),
    path('add-class-type', add_classType,name='add_classType'),
    path('delete-class-type/<int:id>', delete_classType,name='delete_classType'),


    # manage class-master URLS
    path('class-list', class_list,name='class_list'),
    path('add-class', add_class,name='add_class'),
    path('edit-class', edit_class_details,name='edit_class_details'),
    path('class-details/<int:id>', view_class_details,name='view_class_details'),
    path('get-section-and-class-type',get_section_and_class_type,name="get_section_and_class_type"),
    path('delete_class/<int:id>',delete_class,name='delete_class'),


    # manage section-master URLS
    path('section-list', section_list,name='section_list'),
    path('add-section', add_section,name='add_section'),
    path('delete-section/<int:id>', delete_section,name='delete_section'),


    # manage subject-master URLS
    path('subject-list', subject_list,name='subject_list'),
    path('add-subject', add_subject,name='add_subject'),
    path('delete-subject/<int:id>', delete_subject,name='delete_subject'),


    # manage topic-master URLS
    path('topic-list', topic_list,name='topic_list'),
    path('add-topic', add_topic,name='add_topic'),
    path('edit-topic', edit_topic_details,name='edit_topic_details'),
    path('topic-details', view_topic_details,name='view_topic_details'),
    path('fetch_topics', fetch_topics,name='fetch_topics'),


    # manage authority-master URLS
    path('authority-list', authorityList,name='authorityList'),
    path('add-authority', add_authority,name='add_authority'),
    path('delete-authority/<int:id>', delete_authority,name='delete_authority'),
    path('check-authority',check_authority,name='check_authority'),


    # manage sub-authority-master URLS
    path('sub-authority-list', sub_authority_list,name='sub_authority_list'),
    path('add-sub-authority', add_sub_authority,name='add_sub_authority'),
    path('edit-sub-authority/<int:id>', edit_sub_authority_details,name='edit_sub_authority_details'),
    path('sub-authority-details', view_sub_authority_details,name='view_sub_authority_details'),
    path('delete-sub-authority/<int:id>', delete_sub_authority,name='delete_sub_authority'),


    # manage designation-master URLS
    path('designation-list', designation_list,name='designation_list'),
    path('add-designation', add_designation,name='add_designation'),
    path('delete-designation/<int:id>', delete_designation,name='delete_designation'),


    # manage year-master URLS
    path('year-list', year_list,name='year_list'),
    path('add-year', add_year,name='add_year'),
    path('delete-year/<int:id>', delete_year,name='delete_year'),


    # manage question-type-master URLS
    path('question-type-list', question_type_list,name='question_type_list'),
    path('add-question-type', add_question_type,name='add_question_type'),
    path('delete-question-type/<int:id>', delete_questionType,name='delete_questionType'),


    # manage badge-trigger-master URLS
    path('badge-trigger-list', badge_trigger_list,name='badge_trigger_list'),
    path('add-badge-trigger', add_badge_trigger,name='add_badge_trigger'),
    path('delete-badge-trigger/<int:id>', delete_badge_trigger,name='delete_badge_trigger'),


    # manage file_type-master URLS
    path('file-type-list', file_type_list,name='file_type_list'),
    path('add-file-type', add_file_type,name='add_file_type'),
    path('delete-file-type/<int:id>', delete_file_type,name='delete_file_type'),

    # manage exam_type-master URLS
    path('exam-type-list', exam_type_list,name='exam_type_list'),
    path('add-exam-type', add_exam_type,name='add_exam_type'),
    path('delete-exam-type/<int:id>', delete_exam_type,name='delete_exam_type'),

]