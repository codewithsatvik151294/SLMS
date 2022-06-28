function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// global flags for field validation
var branch_flag = false;
var classs_flag = false;
var subject_flag = false;
var topic_flag = false;
var file_type_flag = false;
var content_flag = false;


// global variales
var branch_id = '';
var classs_id = '';
var subject_id = '';
var topic = '';
var file_type_id = '';
var content = '';


// submit_study_material
function submit_study_material(){
    branch_id = $('#branch-id').val().trim();
    classs_id = $('#class-id').val().trim();
    subject_id = $('#subject-id').val().trim();
    topic = $('#topic').val().trim();
    file_type_id = $('#file-type-id').val().trim();

    // field validation
    // if (branch_id == '') {
    //     $('#branch-error').removeClass('d-none');
    //     $('#branch-error').html('');
    //     $('#branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
    //     branch_flag = true;
    // } else {
    //     $('#branch-error').addClass('d-none');
    //     branch_flag = false;
    // }

    if (classs_id == '') {
        $('#class-error').removeClass('d-none');
        $('#class-error').html('');
        $('#class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Class is required</strong></small>");
        classs_flag = true;
    } else {
        $('#class-error').addClass('d-none');
        classs_flag = false;
    }

    if (subject_id == '') {
        $('#subject-error').removeClass('d-none');
        $('#subject-error').html('');
        $('#subject-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Subject is required</strong></small>");
        subject_flag = true;
    } else {
        $('#subject-error').addClass('d-none');
        subject_flag = false;
    }

    if (topic == '') {
        $('#topic-error').removeClass('d-none');
        $('#topic-error').html('');
        $('#topic-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Topic is required</strong></small>");
        topic_flag = true;
    } else {
        $('#topic-error').addClass('d-none');
        topic_flag = false;
    }

    if (file_type_id == '') {
        $('#file-type-error').removeClass('d-none');
        $('#file-type-error').html('');
        $('#file-type-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;File type is required</strong></small>");
        file_type_flag = true;
    } else {
        $('#file-type-error').addClass('d-none');
        file_type_flag = false;
    }


    let content = document.getElementById('content').files[0];
    if (typeof content != 'undefined') {
        $('#content-error').addClass('d-none');
        $('#content-error').html('');
        content_flag = false;
    } else {
        $('#content-error').removeClass('d-none');
        $('#content-error').html('');
        $('#content-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Study material is required</strong></small>");
        content_flag = true;
    }


    if(branch_flag == true || classs_flag == true || subject_flag == true || topic_flag == true || file_type_flag == true || content_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("branch_id", branch_id);
        formdata.append("classs_id", classs_id);
        formdata.append("subject_id", subject_id);
        formdata.append("topic", topic);
        formdata.append("file_type_id", file_type_id);

        let content = document.getElementById('content').files[0];
        if (typeof content != 'undefined') {
            formdata.append('content', content, content['name']);
        }
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-study-material",
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response,response['message']);

                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'New study material added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'study-material-list'
                    })
                } else {
                    alert('An Error occured while adding new study material. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }

}


// get class from branch-id
function get_class(thisTxt) {
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
            // Swal.close();
            // console.log(response['classList']);
            if(response['classList'].length == 0){
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">No Class Available for this branch</option>'+classStr);
                $('#branch-error').removeClass('d-none');
                $('#branch-error').html('');
                $('#branch-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class Available for this branch</strong></small>');
                $('#submit-btn').css('pointer-events', 'none');
                $('#submit-btn').css('opacity', '0.2');
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
                $('#submit-btn').css('pointer-events', '');
                $('#submit-btn').css('opacity', '1');
            }
        }
    });
}


// get subjects from classID
var subject_data = '';
function get_subject(thisTxt) {
    // Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "/manage/get-subject-and-section",
        data: { 'classID': $(thisTxt).val().trim() },
        success: function (response) {
            // Swal.close();
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
            }else{
                $('#subject-id').html('');
                $('#subject-id').append(subject_data);
                $('#subject-id').selectpicker('refresh');
            }
        }
    });
}





// get topics from classID and subjectID
var topic_data = '';
function get_topic(thisTxt) {
    // Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "/question-bank-management/fetch-topics",
        data: { 'classID': $('#class-id').val().trim(),'subjectID': $(thisTxt).val().trim() },
        success: function (response) {
            // Swal.close();
            console.log(response['topicsList']);
            topic_data = '';
            topic_data = "<option class='d-none' value=''>Select Topic </option>";
            if (response['topicsList'].length > 0) {
                for (var i = 0; i < response['topicsList'].length; i++) {
                    var dataStr = '<option value="' + response['topicsList'][i] + '">' + response['topicsList'][i]+ '</option>';
                    topic_data = topic_data + dataStr;
                }
                $('#topic').html('');
                $('#topic').append(topic_data);
                $('#topic').selectpicker('refresh');
                $('#topic-error').html('');
                $('#topic-error').addClass('d-none');
            }else{
                $('#topic').html('');
                $('#topic').append(topic_data);
                $('#topic').selectpicker('refresh');
                $('#topic-error').html('');
                $('#topic-error').removeClass('d-none');
                $('#topic-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No topic available for this subject</strong></small>');
            }
        }
    });
}