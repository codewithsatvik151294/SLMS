// global variables
var subject_data = '';
var subject_count = 0;



// get class from branch-id
function get_class(thisTxt) {
    topic_array = [];
    $('#class-id').html('');
    $('#class-id').append("<option class='d-none' value=''>Select Class </option>");
    $('#class-id').selectpicker('refresh');

    $('#section-id').html('');
    $('#section-id').append("<option class='d-none' value=''>Select Section </option>");
    $('#section-id').selectpicker('refresh');

    $('#tt-table').css('opacity','0.3');
    // $('#tt-add-more').css('opacity','0.3');
    $('#tt-table').css('pointer-events','none');
    // $('#tt-add-more').css('pointer-events','none');

    $.ajax({
        type: 'GET',
        url: "/exam-management/fetch-class",
        data: { 'branchID': $(thisTxt).val().trim() },
        success: function (response) {
            if(response['classList'].length == 0){
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">No Class Available for this branch</option>'+classStr);
                $('#branch-error').removeClass('d-none');
                $('#branch-error').html('');
                $('#branch-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class Available for this branch</strong></small>');
                $('#submit_btn').css('pointer-events', 'none');
                $('#submit_btn').css('opacity', '0.2');
            }else{
                var classStr = '';
                for(var i=0;i<response['classList'].length;i++){
                    var data = '<option value="'+response['classList'][i]['id']+'">'+response['classList'][i]['class_name']+'</option>';
                    classStr = classStr + data;
                }
                $('#assignment-branch-error').addClass('d-none');
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">Select Class</option>'+classStr);
                $('#branch-error').removeClass('d-none');
                $('#branch-error').html('');
                $('#submit_btn').css('pointer-events', '');
                $('#submit_btn').css('opacity', '1');
            }
        }
    });
}




// get subjects and sections of selected class
function get_subject_and_sections(thisTxt) {
    $('#tt-table').css('opacity','0.3');
    // $('#tt-add-more').css('opacity','0.3');
    $('#tt-table').css('pointer-events','none');
    // $('#tt-add-more').css('pointer-events','none');

    $.ajax({
        type: 'GET',
        url: "/manage/get-subject-and-section",
        data: { 'classID': $(thisTxt).val().trim() },
        success: function (response) {
            section_data = '';
            section_data = "<option class='d-none' value=''>Select Section </option>";
            subject_data = '';
            subject_data = "<option class='d-none' value=''>Select Subject </option>";
            subject_count = response['subjectList'].length;
            if (response['sectionList'].length > 0) {
                for (var i = 0; i < response['sectionList'].length; i++) {
                    var dataStr = '<option value="' + response['sectionList'][i]['id'] + '">' + response['sectionList'][i]['section_name'] + '</option>';
                    section_data = section_data + dataStr;
                }
                $('#section-id').html('');
                $('#section-id').append(section_data);
                $('#section-id').selectpicker('refresh');
                for (var i = 0; i < response['subjectList'].length; i++) {
                    var dataStr = '<option value="' + response['subjectList'][i]['id'] + '">' + response['subjectList'][i]['subject_name'] + '</option>';
                    subject_data = subject_data + dataStr;
                }
            }
        }
    });
}



// onchange section view hidden sections
function show_slots(thisTxt){
    if($(thisTxt).val() != ''){
        $('#tt-table').css('opacity','1');
        // $('#tt-add-more').css('opacity','1');
        $('#tt-table').css('pointer-events','');
        // $('#tt-add-more').css('pointer-events','');
    }else{
        $('#tt-table').css('opacity','0.3');
        // $('#tt-add-more').css('opacity','0.3');
        $('#tt-table').css('pointer-events','none');
        // $('#tt-add-more').css('pointer-events','none');
    }

    var data = '';
    for(var i=0;i<subject_count;i++){
        var slotData = '<tr>\
                            <td> \
                            <input type="time" placeholder="Select time" class="timepicker1 form-control" id="start-time-slot-'+i+'" name="" placeholder="From">\
                            <input type="time" placeholder="Select time" class="timepicker1 form-control" id="end-time-slot-'+i+'" name="" placeholder="From">\
                            </td>\
                            <td> \
                            <select class="select2 form-control select2-placeholder8" onchange="get_teacher(this)" id="monday-subject-slot-'+i+'">'+subject_data+'</select>\
                            <span class="d-block sep"></span>\
                            <select class="select2  form-control select2-placeholder26 add-teachers"  id="monday-teacher-slot-'+i+'"><option class="d-none" value="">Select Teacher</option></select>\
                            </td>\
                            <td>\
                            <select class="select2 form-control select2-placeholder8" onchange="get_teacher(this)" id="tuesday-subject-slot-'+i+'">'+subject_data+'</select>\
                            <span class="d-block sep"></span>\
                            <select class="select2  form-control select2-placeholder26 add-teachers"  id="tuesday-teacher-slot-'+i+'"><option class="d-none" value="">Select Teacher</option></select>\
                            </td>\
                            <td>\
                            <select class="select2 form-control select2-placeholder8" onchange="get_teacher(this)" id="wednesday-subject-slot-'+i+'">'+subject_data+'</select>\
                            <span class="d-block sep"></span>\
                            <select class="select2  form-control select2-placeholder26 add-teachers"  id="wednesday-teacher-slot-'+i+'"><option class="d-none" value="">Select Teacher</option></select>\
                            </td>\
                            <td>\
                            <select class="select2 form-control select2-placeholder8" onchange="get_teacher(this)" id="thursday-subject-slot-'+i+'">'+subject_data+'</select>\
                            <span class="d-block sep"></span>\
                            <select class="select2  form-control select2-placeholder26 add-teachers"  id="thursday-teacher-slot-'+i+'"><option class="d-none" value="">Select Teacher</option></select>\
                            </td>\
                            <td>\
                            <select class="select2 form-control select2-placeholder8" onchange="get_teacher(this)" id="friday-subject-slot-'+i+'">'+subject_data+'</select>\
                            <span class="d-block sep"></span>\
                            <select class="select2  form-control select2-placeholder26 add-teachers"  id="friday-teacher-slot-'+i+'"><option class="d-none" value="">Select Teacher</option></select>\
                            </td>\
                            <td>\
                            <select class="select2 form-control select2-placeholder8" onchange="get_teacher(this)" id="saturday-subject-slot-'+i+'">'+subject_data+'</select>\
                            <span class="d-block sep"></span>\
                            <select class="select2  form-control select2-placeholder26 add-teachers"  id="saturday-teacher-slot-'+i+'"><option class="d-none" value="">Select Teacher</option></select>\
                            </td>\
                        </tr>';
        data = data + slotData;
    }

    $('#time-table-slot-data').html('');
    $('#time-table-slot-data').append(data);
}


var teacherData = '';
// get tecaher according to subjects ,branch , class and sections
function get_teacher(thisTxt){
    var branch_id = $('#branch-id').val().trim();
    var class_id = $('#class-id').val().trim();
    var section_id = $('#section-id').val().trim();
    var subject_id = $(thisTxt).val().trim();

    $.ajax({
        type: 'GET',
        url: "/time-table-management/get-teacher",
        data: { 'branch_id': branch_id,'class_id': class_id,'section_id': section_id,'subject_id': subject_id },
        success: function (response) {
            console.log('response >> ',response);
            teacherData = '';
            teacherData = "<option class='d-none' value=''>No Teacher Available</option>";
            if(response['response'].length == 0){
                alert('No Teacher available for this subject!');
                $(thisTxt).parent().find('.add-teachers').html('').append(teacherData);
                return false;
            }else{
                teacherData = "<option class='d-none' value=''>Select Teacher</option>";
                for (var i = 0; i < response['response'].length; i++) {
                    var dataStr = '<option value="' + response['response'][i]['id'] + '">' + response['response'][i]['teacher_name'] + '</option>';
                    teacherData = teacherData + dataStr;
                }
                $(thisTxt).parent().find('.add-teachers').html('').append(teacherData);
            }
        }
    });


}