// flag records
branch_flag = false;
class_flag = false;
subject_flag = false;
topic_flag = false;

// global variables
var branch_id = '';
var class_id = '';
var subject_id = '';
var topic_array = [];

// get cookies for CSRF token
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
    topic_array = [];
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
var status_flag = false;
function get_topic(thisTxt) {
    // Swal.showLoading();
    topic_array = [];
    $.ajax({
        type: 'GET',
        url: "/master/fetch_topics",
        data: { 'branchID': $('#branch-id').val().trim(),'classID': $('#class-id').val().trim(),'subjectID': $(thisTxt).val().trim() },
        success: function (response) {
            // Swal.close();
            console.log(response['topicsList']);
            if(response['topicsList'].length == 0){
                $('#more-topics').html('');
                $('submit_btn').html('');
                $('submit_btn').append('Submit');
                status_flag = false;
            }else{
                var topic_str = '';
                for(var i=0;i<response['topicsList'].length;i++){
                    var data = '<div class="row"><div class="col-lg-11 mt-0 form-group"><input type="text" class="form-control topic-data" placeholder="Enter topic name" value="'+response['topicsList'][i]+'" /></div><div class="text-right col-lg-1  pt-0" ><a style="margin-top:2px" class="btn btn-danger remove-topic  btn-sm " href="javascript:;"><i class="fa fa-minus"></i></a></div></div>';
                    topic_str = topic_str + data;
                }
                $('#more-topics').html('');
                $('#more-topics').append(topic_str);
                $('submit_btn').html('');
                $('submit_btn').append('Update');
                status_flag = true;
            }
            console.log('status_flag >>> ',status_flag);
        }

    });
}




// submit_records
function submit_records(){
    topic_array = [];
    var branch_id = $('#branch-id').val().trim();
    var class_id = $('#class-id').val().trim();
    var subject_id = $('#subject-id').val().trim();

    if (branch_id == '') {
        $('#branch-error').removeClass('d-none');
        $('#branch-error').html('');
        $('#branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#branch-error').addClass('d-none');
        branch_flag = false;
    }

    if (class_id == '') {
        $('#class-error').removeClass('d-none');
        $('#class-error').html('');
        $('#class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Class is required</strong></small>");
        class_flag = true;
    } else {
        $('#class-error').addClass('d-none');
        class_flag = false;
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

    if(status_flag == false){
        $('.topic-data').each(function () { 
            if($(this).val().trim() == ''){
                $(this).css('border','1px solid red');
                topic_flag = true;
            }else{
                $(this).css('border','');
                if(topic_array.includes($(this).val())){
                    console.log('');
                }else{
                    topic_array.push($(this).val());
                    topic_flag = false;
                }
            }
        });
    }else if(status_flag == true){
        var c = 1;
        if(c>=1){
            $('.topic-data').each(function () { 
                if(c==1 && $(this).val().trim() != ''){
                    if(topic_array.includes($(this).val())){
                        console.log('');
                    }else{
                        topic_array.push($(this).val());
                        topic_flag = false;
                    }
                }
                if($(this).val().trim() == ''){
                    $(this).css('border','1px solid red');
                    topic_flag = true;
                }else{
                    $(this).css('border','');
                    if(topic_array.includes($(this).val())){
                        console.log('');
                    }else{
                        topic_array.push($(this).val());
                        topic_flag = false;
                    }
                }
            });
            c=c+1;
        }

    }
    console.log(topic_array);
    console.log('status_flag >> ',status_flag);

    if (branch_flag == true || class_flag == true || subject_flag == true || topic_flag == true) {
        return false;
    } else {
        if(status_flag == true){
            var formdata = new FormData();
            formdata.append("branch_id", branch_id);
            formdata.append("class_id", class_id);
            formdata.append("subject_id", subject_id);
            formdata.append("topic_array", topic_array);
            // ---------------  AJAX CALL  ----------------------------
            Swal.showLoading();
            const csrftoken = getCookie('csrftoken');
            $.ajax({
                type: 'POST',
                url: "add-topic",
                headers: { 'X-CSRFToken': csrftoken },
                data: formdata,
                cache : false,
                processData : false,
                contentType : false,
                encType : 'multipart/form-data',
                success: function (response) {
                    console.log(response['response']);
                    
                    if(response['message'] == 'success'){
                        Swal.fire({
                            icon: 'success',
                            title: 'Topics updated successfully.',
                            showConfirmButton: false,
                            timer: 2000
                        }).then(function () {
                            location.reload();
                        })
                    }else{
                        alert('An Error occured while updating topics. Please try again!');
                        return false;
                    }
                }
            });
            // --------------------------------------------------------
        }else{
            var formdata = new FormData();
            formdata.append("branch_id", branch_id);
            formdata.append("class_id", class_id);
            formdata.append("subject_id", subject_id);
            formdata.append("topic_array", topic_array);
            // ---------------  AJAX CALL  ----------------------------
            Swal.showLoading();
            const csrftoken = getCookie('csrftoken');
            $.ajax({
                type: 'POST',
                url: "add-topic",
                headers: { 'X-CSRFToken': csrftoken },
                data: formdata,
                cache : false,
                processData : false,
                contentType : false,
                encType : 'multipart/form-data',
                success: function (response) {
                    console.log(response['response']);
                    
                    if(response['message'] == 'success'){
                        Swal.fire({
                            icon: 'success',
                            title: 'New topics added successfully.',
                            showConfirmButton: false,
                            timer: 2000
                        }).then(function () {
                            location.reload();
                        })
                    }else{
                        alert('An Error occured while adding new topics. Please try again!');
                        return false;
                    }
                }
            });
            // --------------------------------------------------------
        }
    }

}