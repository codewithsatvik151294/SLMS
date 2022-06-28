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

// render question type
function question_type(thisTxt){
    if($(thisTxt).find('option:selected').text() == 'Objective' || $(thisTxt).find('option:selected').text() == 'Multiple Choice Objective'){
        $('#option_count_div').removeClass('d-none');
        $('#options-1').addClass('d-none');
        $('#options-1').html('');
    }else{
        $('#option_count_div').addClass('d-none');
        $('#options-1').addClass('d-none');
        $('#options-1').html('');
    }
}


// render options according to selected count
function option_count(thisTxt){
    var count = $(thisTxt).val();
    if(count > 1){
        $('#options-1').removeClass('d-none');
        $('#options-1').html('');
        var data_str = '';
        if($('#question-type').find('option:selected').text() == 'Objective'){
            for(var i=1;i<=count;i++){
                if(i==1){
                    var data = ' <div class="col-lg-2  mt-1  form-group opt_radio"><label><input type="radio" name="opt" class="option-name" checked> Option '+i+'</label>\
                            </div><div class="col-lg-10 mt-1  form-group"><input type="text" class="form-control option-value" placeholder="Type Options" value="" /></div>';
                data_str = data_str + data;
                }else{
                    var data = ' <div class="col-lg-2  mt-1  form-group opt_radio"><label><input type="radio" name="opt" class="option-name"> Option '+i+'</label>\
                    </div><div class="col-lg-10 mt-1  form-group"><input type="text" class="form-control option-value" placeholder="Type Options" value="" /></div>';
                    data_str = data_str + data;
                }
            }
        }else{
            for(var i=1;i<=count;i++){
                if(i==1){
                    var data = ' <div class="col-lg-2  mt-1  form-group opt_radio"><label><input type="checkbox" name="opt_'+i+'" class="option-name" checked> Option '+i+'</label>\
                            </div><div class="col-lg-10 mt-1  form-group"><input type="text" class="form-control option-value" placeholder="Type Options" value="" /></div>';
                data_str = data_str + data;
                }else{
                    var data = ' <div class="col-lg-2  mt-1  form-group opt_radio"><label><input type="checkbox" name="opt_'+i+'" class="option-name"> Option '+i+'</label>\
                    </div><div class="col-lg-10 mt-1  form-group"><input type="text" class="form-control option-value" placeholder="Type Options" value="" /></div>';
                    data_str = data_str + data;
                }
            }
        }
        var optionStr = '<div class="row">'+data_str+'</div>';
        $('#options-1').append(optionStr);
    }else{
        $('#options-1').html('');
        $('#options-1').removeClass('d-none');
    }
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

// get sections and subjects from classID
var subject_data = '';
function get_subject(thisTxt) {
    Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "/manage/get-subject-and-section",
        data: { 'classID': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            console.log(response);
            subject_data = '';
            subject_data = "<option class='d-none' value=''>Select Subject </option>";
            if (response['subjectList'].length > 0) {
                for (var i = 0; i < response['subjectList'].length; i++) {
                    var dataStr = '<option value="' + response['subjectList'][i]['id'] + '">' + response['subjectList'][i]['subject_name'] + '</option>';
                    subject_data = subject_data + dataStr;
                }
                $('#question_subject').html('');
                $('#question_subject').append(subject_data);
                $('#question_subject').selectpicker('refresh');
            }
        }
    });
}



// get stopics from classID and subjectID
var topic_data = '';
function get_topic(thisTxt) {
    Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "fetch-topics",
        data: { 'classID': $('#class-id').val().trim(),'subjectID': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            console.log(response['topicsList']);
            topic_data = '';
            topic_data = "<option class='d-none' value=''>Select Topic </option>";
            if (response['topicsList'].length > 0) {
                for (var i = 0; i < response['topicsList'].length; i++) {
                    var dataStr = '<option value="' + response['topicsList'][i] + '">' + response['topicsList'][i]+ '</option>';
                    topic_data = topic_data + dataStr;
                }
                $('#question_topic').html('');
                $('#question_topic').append(topic_data);
                $('#question_topic').selectpicker('refresh');
            }else{
                $('#question_topic').html('');
                $('#question_topic').selectpicker('refresh');
            }
        }
    });
}


// global flags for field validation
var branch_flag = false;
var class_flag = false;
var subject_flag = false;
var year_flag = false;
var topic_flag = false;
var question_type_flag = false;
var question_sub_type_flag = false;
var question_flag = false;
var option_count_flag = false;
var option_array_flag = false;
var difficulty_flag = false;
var correct_mark_flag = false;
var negative_mark_flag = false;

// add new question
function add_new_question() {
    var branchID = $('#branch-id').val().trim();
    var classID = $('#class-id').val().trim();
    var subjectID = $('#question_subject').val().trim();
    var yearID = $('#question-year').val().trim();
    var topic = $('#question_topic').val().trim();
    var question_typeID = $('#question-type').find('option:selected').text();
    var question_sub_type = $('#question-sub-type').val().trim();
    var question = $(".Editor-editor").html().trim();

    var option_count = ''
    var option_array = [];
    
    var option_name_array = [];
    var option_value_array = [];

    if(question_typeID == 'Objective'){
        option_count = $('#option-1').val();
        $('.option-name').each(function () { 
            if($(this).prop("checked") == true){
                option_name_array.push('true');
            }
            else if($(this).prop("checked") == false){
                option_name_array.push('false');
            }
        });
        
        $('.option-value').each(function () { 
            option_value_array.push($(this).val());
            if($(this).val().trim() == ''){
                $(this).css('border','1px solid red');
                option_array_flag = true;
            }else{
                $(this).css('border','');
                option_array_flag = false;
            } 
        });
        
    }else if(question_typeID == 'Multiple Choice Objective'){
        option_count = $('#option-1').val();
        $('.option-name').each(function () { 
            if($(this).prop("checked") == true){
                option_name_array.push('true');
            }
            else if($(this).prop("checked") == false){
                option_name_array.push('false');
            }
        });
        
        $('.option-value').each(function () { 
            option_value_array.push($(this).val());
            if($(this).val().trim() == ''){
                $(this).css('border','1px solid red');
                option_array_flag = true;
            }else{
                $(this).css('border','');
                option_array_flag = false;
            } 
        });
    }else{
        option_array_flag = false;
    }
    console.log(option_name_array);
    console.log(option_value_array);

    if(option_name_array.length == option_value_array.length && option_value_array.length > 1){
        for(var i=0;i<option_name_array.length;i++){
            var dataDict = {}
            dataDict['option'+(i+1)+''] = option_value_array[i];
            dataDict['status'] = option_name_array[i];
            option_array.push(dataDict);
        }
    }
    console.log(option_array);

    console.log(question);


    var difficulty = $('#question-difficulty').val().trim();
    var correct_mark = $('#correct-mark').val().trim();
    var negative_mark = $('#negative-mark').val().trim();

    // field validation
    if (branchID == '') {
        $('#branch-error').removeClass('d-none');
        $('#branch-error').html('');
        $('#branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#branch-error').addClass('d-none');
        branch_flag = false;
    }

    if (classID == '') {
        $('#class-error').removeClass('d-none');
        $('#class-error').html('');
        $('#class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Class is required</strong></small>");
        class_flag = true;
    } else {
        $('#class-error').addClass('d-none');
        class_flag = false;
    }

    if (subjectID == '') {
        $('#subject-error').removeClass('d-none');
        $('#subject-error').html('');
        $('#subject-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Subject is required</strong></small>");
        subject_flag = true;
    } else {
        $('#subject-error').addClass('d-none');
        subject_flag = false;
    }

    if (yearID == '') {
        $('#year-error').removeClass('d-none');
        $('#year-error').html('');
        $('#year-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Year is required</strong></small>");
        year_flag = true;
    } else {
        $('#year-error').addClass('d-none');
        year_flag = false;
    }

    if (topic == '') {
        $('#topic-error').removeClass('d-none');
        $('#topic-error').html('');
        $('#topic-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Topic is required</strong></small>");
        topic_flag = true;
    } else {
        $('#topic-error').addClass('d-none');
        topic_flag = false;
    }

    if ($('#question-type').val().trim() == '') {
        $('#question-type-error').removeClass('d-none');
        $('#question-type-error').html('');
        $('#question-type-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Question Type is required</strong></small>");
        question_type_flag = true;
    } else {
        $('#question-type-error').addClass('d-none');
        question_type_flag = false;
    }

    if (question_sub_type == '') {
        $('#question-sub-type-error').removeClass('d-none');
        $('#question-sub-type-error').html('');
        $('#question-sub-type-error').append('<small><strong>&nbsp;&nbsp;&nbsp;Question Sub Type is required</strong></small>');
        question_sub_type_flag = true;
    } else {
        $('#question-sub-type-error').addClass('d-none');
        question_sub_type_flag = false;
    }

    if (question == '') {
        $('#question-error').removeClass('d-none');
        $('#question-error').html('');
        $('#question-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Question is required</strong></small>");
        question_flag = true;
    } else {
        $('#question-error').addClass('d-none');
        $('#question-error').html('');
        question_flag = false;
    }

    if(question_typeID == 'Objective' || question_typeID == 'Multiple Choice Objective'){
        if (option_count == '') {
            $('#no-of-options-error').removeClass('d-none');
            $('#no-of-options-error').html('');
            $('#no-of-options-error').append("<small><strong> &nbsp;&nbsp;&nbsp;No. of Options is required</strong></small>");
            option_count_flag = true;
        } else {
            $('#no-of-options-error').addClass('d-none');
            $('#no-of-options-error').html('');
            option_count_flag = false;
        }
    }
    
    if (difficulty == '') {
        $('#difficulty-error').removeClass('d-none');
        $('#difficulty-error').html('');
        $('#difficulty-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Difficulty is required</strong></small>");
        difficulty_flag = true;
    } else {
        $('#difficulty-error').addClass('d-none');
        $('#difficulty-error').html('');
        difficulty_flag = false;
    }

    if (correct_mark == '') {
        $('#correct-marks-error').removeClass('d-none');
        $('#correct-marks-error').html('');
        $('#correct-marks-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Correct Marks is required</strong></small>");
        correct_mark_flag = true;
    } else {
        $('#correct-marks-error').addClass('d-none');
        $('#correct-marks-error').html('');
        correct_mark_flag = false;
    }

    if (negative_mark == '') {
        $('#negaative-marks-error').removeClass('d-none');
        $('#negaative-marks-error').html('');
        $('#negaative-marks-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Negative Marks is required</strong></small>");
        negative_mark_flag = true;
    } else {
        $('#negaative-marks-error').addClass('d-none');
        $('#negaative-marks-error').html('');
        negative_mark_flag = false;
    }


    if (branch_flag == true || class_flag == true || subject_flag == true || year_flag == true || topic_flag == true || question_type_flag == true || question_sub_type_flag == true || question_flag == true || option_count_flag == true || option_array_flag == true || difficulty_flag == true || correct_mark_flag == true || negative_mark_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("branchID",branchID)
        formdata.append("classID", classID);
        formdata.append("subjectID", subjectID);
        formdata.append("yearID", yearID);
        formdata.append("topic", topic);
        formdata.append("question_typeID", $('#question-type').val().trim());
        formdata.append("question_sub_type", question_sub_type);
        formdata.append("question", question);
        formdata.append("option_count", option_count);
        formdata.append("option_array[]", JSON.stringify(option_array));
        formdata.append("difficulty", difficulty);
        formdata.append("correct_mark", correct_mark);
        formdata.append("negative_mark", negative_mark);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-question",
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response['response']);

                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'New question added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'add-question';
                    })
                } else if(response['message'] == 'exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Question already exist with selected parameters',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else {
                    alert('An Error occured while adding new student. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}




// save and add more questions
// global flags for field validation
var class_save_more_flag = false;
var subject_save_more_flag = false;
var year_save_more_flag = false;
var topic_save_more_flag = false;
var question_type_save_more_flag = false;
var question_sub_type_save_more_flag = false;
var question_save_more_flag = false;
var option_count_save_more_flag = false;
var option_array_save_more_flag = false;
var difficulty_save_more_flag = false;
var correct_mark_save_more_flag = false;
var negative_mark_save_more_flag = false;
function save_more_question(){
    // reinitializing the flags
    class_save_more_flag = false;
    subject_save_more_flag = false;
    year_save_more_flag = false;
    topic_save_more_flag = false;
    question_type_save_more_flag = false;
    question_sub_type_save_more_flag = false;
    question_save_more_flag = false;
    option_count_save_more_flag = false;
    option_array_save_more_flag = false;
    difficulty_save_more_flag = false;
    correct_mark_save_more_flag = false;
    negative_mark_save_more_flag = false;

    var classID = $('#class-id').val().trim();
    var subjectID = $('#question_subject').val().trim();
    var yearID = $('#question-year').val().trim();
    var topic = $('#question_topic').val().trim();
    var question_typeID = $('#question-type').val().trim();
    var question_sub_type = $('#question-sub-type').val().trim();
    var question = $(".Editor-editor").html().trim();
    
    var option_count = ''
    var option_array = [];
    
    var option_name_array = [];
    var option_value_array = [];

    if(question_typeID == '2'){
        option_count = $('#option-1').val();
        $('.option-name').each(function () { 
            if($(this).prop("checked") == true){
                option_name_array.push('true');
            }
            else if($(this).prop("checked") == false){
                option_name_array.push('false');
            }
        });
        
        $('.option-value').each(function () { 
            option_value_array.push($(this).val());
            if($(this).val().trim() == ''){
                $(this).css('border','1px solid red');
                option_array_save_more_flag = true;
            }else{
                $(this).css('border','');
                option_array_save_more_flag = false;
            } 
        });
        
    }else{
        option_array_save_more_flag = false;
    }
    console.log(option_name_array);
    console.log(option_value_array);

    

    var difficulty = $('#question-difficulty').val().trim();
    var correct_mark = $('#correct-mark').val().trim();
    var negative_mark = $('#negative-mark').val().trim();

    // field validation
    if (classID == '') {
        $('#class-error').removeClass('d-none');
        $('#class-error').html('');
        $('#class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Class is required</strong></small>");
        class_save_more_flag = true;
    } else {
        $('#class-error').addClass('d-none');
        class_save_more_flag = false;
    }

    if (subjectID == '') {
        $('#subject-error').removeClass('d-none');
        $('#subject-error').html('');
        $('#subject-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Subject is required</strong></small>");
        subject_save_more_flag = true;
    } else {
        $('#subject-error').addClass('d-none');
        subject_save_more_flag = false;
    }

    if (yearID == '') {
        $('#year-error').removeClass('d-none');
        $('#year-error').html('');
        $('#year-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Year is required</strong></small>");
        year_save_more_flag = true;
    } else {
        $('#year-error').addClass('d-none');
        year_save_more_flag = false;
    }

    if (topic == '') {
        $('#topic-error').removeClass('d-none');
        $('#topic-error').html('');
        $('#topic-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Topic is required</strong></small>");
        topic_save_more_flag = true;
    } else {
        $('#topic-error').addClass('d-none');
        topic_save_more_flag = false;
    }

    if (question_typeID == '') {
        $('#question-type-error').removeClass('d-none');
        $('#question-type-error').html('');
        $('#question-type-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Question Type is required</strong></small>");
        question_type_save_more_flag = true;
    } else {
        $('#question-type-error').addClass('d-none');
        question_type_save_more_flag = false;
    }

    if (question_sub_type == '') {
        $('#question-sub-type-error').removeClass('d-none');
        $('#question-sub-type-error').html('');
        $('#question-sub-type-error').append('<small><strong>&nbsp;&nbsp;&nbsp;Question Sub Type is required</strong></small>');
        question_sub_type_save_more_flag = true;
    } else {
        $('#question-sub-type-error').addClass('d-none');
        question_sub_type_save_more_flag = false;
    }

    if (question == '') {
        $('#question-error').removeClass('d-none');
        $('#question-error').html('');
        $('#question-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Question is required</strong></small>");
        question_save_more_flag = true;
    } else {
        $('#question-error').addClass('d-none');
        $('#question-error').html('');
        question_save_more_flag = false;
    }

    if(question_typeID == '2'){
        if (option_count == '') {
            $('#no-of-options-error').removeClass('d-none');
            $('#no-of-options-error').html('');
            $('#no-of-options-error').append("<small><strong> &nbsp;&nbsp;&nbsp;No. of Options is required</strong></small>");
            option_count_save_more_flag = true;
        } else {
            $('#no-of-options-error').addClass('d-none');
            $('#no-of-options-error').html('');
            option_count_save_more_flag = false;
        }
    }
    
    if (difficulty == '') {
        $('#difficulty-error').removeClass('d-none');
        $('#difficulty-error').html('');
        $('#difficulty-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Difficulty is required</strong></small>");
        difficulty_save_more_flag = true;
    } else {
        $('#difficulty-error').addClass('d-none');
        $('#difficulty-error').html('');
        difficulty_save_more_flag = false;
    }

    if (correct_mark == '') {
        $('#correct-marks-error').removeClass('d-none');
        $('#correct-marks-error').html('');
        $('#correct-marks-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Correct Marks is required</strong></small>");
        correct_mark_save_more_flag = true;
    } else {
        $('#correct-marks-error').addClass('d-none');
        $('#correct-marks-error').html('');
        correct_mark_save_more_flag = false;
    }

    if (negative_mark == '') {
        $('#negaative-marks-error').removeClass('d-none');
        $('#negaative-marks-error').html('');
        $('#negaative-marks-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Negative Marks is required</strong></small>");
        negative_mark_save_more_flag = true;
    } else {
        $('#negaative-marks-error').addClass('d-none');
        $('#negaative-marks-error').html('');
        negative_mark_save_more_flag = false;
    }


    if (class_save_more_flag == true || subject_save_more_flag == true || year_save_more_flag == true || topic_save_more_flag == true || question_type_save_more_flag == true || question_sub_type_save_more_flag == true || question_save_more_flag == true || option_count_save_more_flag == true || option_array_save_more_flag == true || difficulty_save_more_flag == true || correct_mark_save_more_flag == true || negative_mark_save_more_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("classID", classID);
        formdata.append("subjectID", subjectID);
        formdata.append("yearID", yearID);
        formdata.append("topic", topic);
        formdata.append("question_typeID", question_typeID);
        formdata.append("question_sub_type", question_sub_type);
        formdata.append("question", question);
        formdata.append("option_count", option_count);
        formdata.append("option_array[]", option_array);
        formdata.append("difficulty", difficulty);
        formdata.append("correct_mark", correct_mark);
        formdata.append("negative_mark", negative_mark);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-more-question",
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response['response']);

                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'New question added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'add-question';
                    })
                } else if(response['message'] == 'exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Question already exist with selected parameters',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else {
                    alert('An Error occured while adding new student. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}