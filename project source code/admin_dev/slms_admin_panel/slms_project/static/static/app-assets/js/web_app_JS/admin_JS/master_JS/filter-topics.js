// get class from branch-id
function get_class(thisTxt) {
    topic_array = [];
    $('#class-id').html('');
    $('#class-id').append("<option class='d-none' value=''>Select Class </option>");
    $('#class-id').selectpicker('refresh');

    $('#subject-id').html('');
    $('#subject-id').append("<option class='d-none' value=''>Select Subject </option>");
    $('#subject-id').selectpicker('refresh');

    $('#topic-id').html('');
    $('#topic-id').append("<option class='d-none' value=''>Select Topic </option>");
    $('#topic-id').selectpicker('refresh');

    // Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "/exam-management/fetch-class",
        data: { 'branchID': $(thisTxt).val().trim() },
        success: function (response) {
            if (response['classList'].length == 0) {
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">No Class Available for this branch</option>' + classStr);
                $('#branch-error').removeClass('d-none');
                $('#branch-error').html('');
                $('#branch-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class Available for this branch</strong></small>');
                $('#submit-btn').css('pointer-events', 'none');
                $('#submit-btn').css('opacity', '0.2');
            } else {
                var classStr = '';
                for (var i = 0; i < response['classList'].length; i++) {
                    var data = '<option value="' + response['classList'][i]['id'] + '">' + response['classList'][i]['class_name'] + '</option>';
                    classStr = classStr + data;
                }
                $('#assignment-branch-error').addClass('d-none');
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">Select Class</option>' + classStr);
                $('#branch-error').removeClass('d-none');
                $('#branch-error').html('');
                $('#submit-btn').css('pointer-events', '');
                $('#submit-btn').css('opacity', '1');
            }
        }
    });
}


// get subjects from classID
var subject_data = '';
function get_subject(thisTxt) {
    topic_array = [];
    $.ajax({
        type: 'GET',
        url: "/manage/get-subject-and-section",
        data: { 'classID': $(thisTxt).val().trim() },
        success: function (response) {
            subject_data = '';
            subject_data = "<option class='d-none' value=''>Select Subject </option>";
            if (response['subjectList'].length > 0) {
                for (var i = 0; i < response['subjectList'].length; i++) {
                    var dataStr = '<option value="' + response['subjectList'][i]['id'] + '">' + response['subjectList'][i]['subject_name'] + '</option>';
                    subject_data = subject_data + dataStr;
                }
                $('#subject-id').html('');
                $('#subject-id').append(subject_data);
                $('#subject-id').selectpicker('refresh');
            } else {
                $('#subject-id').html('');
                $('#subject-id').append(subject_data);
                $('#subject-id').selectpicker('refresh');
            }
        }
    });
}


// get topics from classID and subjectID
var status_flag = false;
function get_topic(thisTxt) {
    if ($('#branch-id').val().trim() != '' && $('#class-id').val().trim() != '' && $('#subject-id').val().trim() != '') {
        $.ajax({
            type: 'GET',
            url: "/master/fetch_topics",
            data: { 'branchID': $('#branch-id').val().trim(), 'classID': $('#class-id').val().trim(), 'subjectID': $('#subject-id').val().trim() },
            success: function (response) {
                if(response['topicsList'].length == 0){
                    $('#append-topics-array').html('');
                    $('#append-topics-array').append('<tr><td class="text-center" > <strong>No topis available!</strong></td></tr>');
                }else{
                    var topic_str = '';
                    for(var i=0;i<response['topicsList'].length;i++){
                        var data = '<tr><td class="text-left" > <strong>'+response['topicsList'][i]+'</strong></td></tr>';
                        topic_str = topic_str + data;
                    }
                    $('#append-topics-array').html('');
                    $('#append-topics-array').append(topic_str);
                }
            }
        });
    }else{
        alert('select all parameters!');
        return false;
    }

}