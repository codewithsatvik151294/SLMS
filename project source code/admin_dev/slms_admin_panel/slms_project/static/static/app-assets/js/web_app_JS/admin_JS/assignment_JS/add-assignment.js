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


// global flags
var assignment_name_flag = false;
var branchID_flag = false;
var classID_flag = false;
var sectionID_flag = false;
var subjectID_flag = false;
var total_marks_flag = false;
var passing_marks_flag = false;
var start_flag = false;
var end_flag = false;
var question_type_flag = false;
var guideline_flag = false;
var question_flag = false;


// global variables
var assignment_name = '';
var branchID = '';
var classID = '';
var sectionID = '';
var subjectID = '';
var total_mark = '';
var passing_mark = '';
var start_at = '';
var end_at = '';
var question_type = [];
var guidelines = '';
var question_array = [];
var selected_question_array = [];
var topic_array = [];



// get class from branchID
var subject_data = '';
function get_class(thisTxt) {
    $('#subject-id').html('');
    $('#subject-id').append("<option class='d-none' value=''>Select Subject </option>");
    $('#subject-id').selectpicker('refresh');

    $('#section-id').html('');
    $('#section-id').append("<option class='d-none' value=''>Select Section </option>");
    $('#section-id').selectpicker('refresh');

    Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "/exam-management/fetch-class",
        data: { 'branchID': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            // console.log(response['classList']);
            if(response['classList'].length == 0){
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">No Class Available for this branch</option>'+classStr);
                $('#assignment-class-error').removeClass('d-none');
                $('#assignment-class-error').html('');
                $('#assignment-class-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class Available for this branch</strong></small>');
                $('#submit-btn').css('pointer-events', 'none');
                $('#submit-btn').css('opacity', '0.2');
                $('#question-add-btn').css('pointer-events', 'none');
                $('#question-add-btn').css('opacity', '0.2');
            }else{
                var classStr = '';
                for(var i=0;i<response['classList'].length;i++){
                    var data = '<option value="'+response['classList'][i]['id']+'">'+response['classList'][i]['class_name']+'</option>';
                    classStr = classStr + data;
                }
                $('#assignment-branch-error').addClass('d-none');
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">Select Class</option>'+classStr);
                $('#assignment-class-error').removeClass('d-none');
                $('#assignment-class-error').html('');
                $('#submit-btn').css('pointer-events', '');
                $('#submit-btn').css('opacity', '1');
                $('#question-add-btn').css('pointer-events', '');
                $('#question-add-btn').css('opacity', '1');
            }
        }
    });
}


// get subjects and sections from classID
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
                $('#subject-id').html('');
                $('#subject-id').append(subject_data);
                $('#subject-id').selectpicker('refresh');

                $('#modal-subject-id').html('');
                $('#modal-subject-id').append(subject_data);
                $('#modal-subject-id').selectpicker('refresh');

                $('#modal-question-id').val($(thisTxt).val().trim());
                $('#modal-question-id').selectpicker('refresh');
            }else{
                $('#subject-id').html('');
                $('#subject-id').append(subject_data);
                $('#subject-id').selectpicker('refresh');

                $('#modal-subject-id').html('');
                $('#modal-subject-id').append(subject_data);
                $('#modal-subject-id').selectpicker('refresh');
            }

            section_data = '';
            section_data = "<option class='d-none' value=''>Select Section </option>";
            if (response['sectionList'].length > 0) {
                for (var i = 0; i < response['sectionList'].length; i++) {
                    var dataStr = '<option value="' + response['sectionList'][i]['id'] + '">' + response['sectionList'][i]['section_name'] + '</option>';
                    section_data = section_data + dataStr;
                }
                $('#section-id').html('');
                $('#section-id').append(section_data);
                $('#section-id').selectpicker('refresh');
            }else{
                $('#section-id').html('');
                $('#section-id').append(section_data);
                $('#section-id').selectpicker('refresh');
            }
        }
    });
}


var temp_question_array = [];
var temp_question_marks_sum = 0;
var temp_question_count = 0;
var temp_topic_array = []
// validate_parameters and show questions on modal
function validate_parameters(){
    branchID = $('#branch-id').val().trim();
    classID = $('#class-id').val().trim();
    sectionID = $('#section-id').val().trim();
    subjectID = $('#subject-id').val().trim();
    total_mark = $('#total-marks').val().trim();
    question_type = $('#question-type').val();

    // if(branchID == ''){
    //     alert('Select branch to add questions');
    //     $('#branch-id').css('border','2px solid red');
    //     branchID_flag = true;
    //     return false;
    // }else{
    //     $('#branch-id').css('border','');
    //     branchID_flag = false;
    // }
    
    if(classID == ''){
        alert('Select class to add questions');
        $('#class-id').css('border','2px solid red');
        classID_flag = true;
        return false;
    }else{
        $('#class-id').css('border','');
        classID_flag = false;
    }

    if(sectionID == ''){
        alert('Select section to add questions');
        $('#section-id').css('border','2px solid red');
        sectionID_flag = true;
        return false;
    }else{
        $('#section-id').css('border','');
        sectionID_flag = false;
    }

    if(subjectID == ''){
        alert('Select subject to add questions');
        $('#subject-id').css('border','2px solid red');
        subjectID_flag = true;
        return false;
    }else{
        $('#subject-id').css('border','');
        subjectID_flag = false;
    }

    if(total_mark == ''){
        alert('Enter total marks to add questions');
        $('#total-marks').css('border','2px solid red');
        total_marks_flag = true;
        return false;
    }else{
        $('#total-marks').css('border','');
        total_marks_flag = false;
    }

    if(question_type.length == 0){
        alert('Select question type to add questions');
        $('#question-type').css('border','2px solid red');
        question_type_flag = true;
        return false;
    }else{
        $('#question-type').css('border','');
        question_type_flag = false;
    }


    if(branchID_flag == true || classID_flag == true || sectionID_flag == true || subjectID_flag == true || total_marks_flag == true || question_type_flag == true){
        return false;
    }else{
        console.log('classid >> ', classID);
        console.log('subjectid >> ', subjectID);
        console.log('sectionID >> ', sectionID);
        // appending questions into the modal
        // ========================= ajax call ========================================
        $.ajax({
            type: 'GET',
            url: "/assignment-management/fetch-questions",
            data: { 'class_id': classID, 'subject_id': subjectID, 'qType[]': question_type },
            success: function (response) {
                Swal.close();
                console.log('response >>> ', response);
                if (response['data_list'].length > 0) {
                    var questionStr = '';
                    for (var i = 0; i < response['data_list'].length; i++) {
                        if (selected_question_array.includes(response['data_list'][i]['id'])) {
                            var data = '<tr>\
                            <td><p>'+ response['data_list'][i]['question_text'] + '<a href="javascript:;" class="edit float-right ml-1 text-white" style="background-color:darkgrey;" onclick="remove_question_from_section(' + response['data_list'][i]['id'] + ',' + response['data_list'][i]['correct_mark'] + ',this)"><i class="fa fa-times"></i> Remove</a></p>\
                            <div class="q_info">\
                            <ul>\
                            <li><span>QType</span> '+ response['data_list'][i]['question_type'] + '</li>\
                            <li><span>Q-Sub-Type</span> '+ response['data_list'][i]['question_sub_type'] + '</li>\
                            <li><span>Difficulty</span> '+ response['data_list'][i]['difficulty'] + '</li>\
                            <li><span>Marks</span> '+ response['data_list'][i]['correct_mark'] + '</li>\
                            <li class="subj"><span>Subject</span> '+ response['data_list'][i]['subject_name'] + '</li>\
                            <li class="topic"><span>Topic</span> '+ response['data_list'][i]['topic_name'] + '</li>\
                            <li><span>Year</span> '+ response['data_list'][i]['year_name'] + '</li>\
                            </ul>\
                            </div>\
                            </td>\
                            </tr>';
                        } else {
                            var data = '<tr>\
                            <td><p>'+ response['data_list'][i]['question_text'] + '<a href="javascript:;" class="edit float-right ml-1" style="background-color:#118ed7;" onclick="add_question_to_section(' + response['data_list'][i]['id'] + ',' + response['data_list'][i]['correct_mark'] + ',this)" topic_name="' + response['data_list'][i]['topic_name'] + '"><i class="fa fa-plus"></i> Add</a></p>\
                            <div class="q_info">\
                            <ul>\
                            <li><span>QType</span> '+ response['data_list'][i]['question_type'] + '</li>\
                            <li><span>Q-Sub-Type</span> '+ response['data_list'][i]['question_sub_type'] + '</li>\
                            <li><span>Difficulty</span> '+ response['data_list'][i]['difficulty'] + '</li>\
                            <li><span>Marks</span> '+ response['data_list'][i]['correct_mark'] + '</li>\
                            <li class="subj"><span>Subject</span> '+ response['data_list'][i]['subject_name'] + '</li>\
                            <li class="topic"><span>Topic</span> '+ response['data_list'][i]['topic_name'] + '</li>\
                            <li><span>Year</span> '+ response['data_list'][i]['year_name'] + '</li>\
                            </ul>\
                            </div>\
                            </td>\
                            </tr>';
                        }
                        questionStr = questionStr + data;
                    }
                    $('#new-question-append').html('');
                    $('#new-question-append').append(questionStr);
                    $('#no-quest-div').addClass('d-none');
                    $('#example1').removeClass('d-none');
                    $('#total-ques-count').html('');
                    $('#total-ques-count').append(response['data_list'].length);
                } else {
                    $('#no-quest-div').removeClass('d-none');
                    $('#example1').addClass('d-none');
                    $('#total-ques-count').html('');
                    $('#total-ques-count').append('0');
                    $('#new-question-append').html('');
                }
            }
        }).then(function(){
            $('#questions').modal('show');
        });
        // ============================================================================
    }
}


// check assignment name
function check_assignment_name(thisTxt) {
    $.ajax({
        type: 'GET',
        url: "/assignment-management/check-assignment",
        data: { 'search_string': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            console.log('response >>> ',response['message']);
            if (response['message'] == 'exist') {
                $('#assignment-name-error').removeClass('d-none');
                $('#assignment-name-error').html('');
                $('#assignment-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Assignment title already exist</strong></small>");
                assignment_name_flag = true;
            } else {
                $('#assignment-name-error').addClass('d-none');
                assignment_name_flag = false;
            }

            // button enabled/disable
            if (assignment_name_flag == true) {
                $('#submit-btn').css('pointer-events', 'none');
                $('#submit-btn').css('opacity', '0.2');
            } else {
                $('#submit-btn').css('pointer-events', '');
                $('#submit-btn').css('opacity', '1');
            }
        }
    });
}


// compare total marks and passing marks
function compare_marks() {
    total_mark = $('#total-marks').val().trim();
    passing_mark = $('#passing-marks').val().trim();

    if (total_mark != '' && passing_mark != '') {
        if (parseFloat(passing_mark) > parseFloat(total_mark)) {
            alert('Passing marks cannot be greater than total marks!');
            $('#passing-marks').val('');
            $('#assignment-passing-error').removeClass('d-none');
            $('#assignment-passing-error').html('');
            $('#assignment-passing-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Passing marks cannot be greater than total marks</strong></small>");
            passing_marks_flag = true;
            return false;
        }
    }

    if (total_mark == '' && passing_mark != '') {
        alert('Enter total marks!');
        $('#passing-marks').val('');
        $('#assignment-total-error').removeClass('d-none');
        $('#assignment-total-error').html('');
        $('#assignment-total-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Enter total marks</strong></small>");
        passing_marks_flag = true;
        return false;
    }

    else {
        $('#assignment-passing-error').addClass('d-none');
        $('#assignment-passing-error').html('');
        $('#assignment-total-error').addClass('d-none');
        $('#assignment-total-error').html('');
        passing_marks_flag = false;
    }
}


// validate startdate-time and end date-time
function check_exam_date_time(thisTxt){

    var date1 = new Date($('#start-at').val());
    var date2 = new Date($('#end-at').val());

    if($('#start-at').val() != '' && $('#end-at').val()){
        if(date1.getTime() === date2.getTime()){
            alert('Start and End date-time cannot be same!');
            $('#start-at').css('border','2px solid red');
            $('#end-at').css('border','2px solid red');
            $('#submit-btn').css('pointer-events', 'none');
            $('#submit-btn').css('opacity', '0.3');
            $('#question-add-btn').css('pointer-events', 'none');
            $('#question-add-btn').css('opacity', '0.3');
        }else{
            $('#start-at').css('border','');
            $('#end-at').css('border','');
            $('#submit-btn').css('pointer-events', '');
            $('#submit-btn').css('opacity', '1');
            $('#question-add-btn').css('pointer-events', '');
            $('#question-add-btn').css('opacity', '1');
        }
        
        if(date1.getTime() > date2.getTime()){
            alert('Start date-time cannot be End date-time!');
            $('#start-at').css('border','2px solid red');
            $('#end-at').css('border','2px solid red');
            $('#submit-btn').css('pointer-events', 'none');
            $('#submit-btn').css('opacity', '0.3');
            $('#question-add-btn').css('pointer-events', 'none');
            $('#question-add-btn').css('opacity', '0.3');
        }else{
            $('#start-at').css('border','');
            $('#end-at').css('border','');
            $('#submit-btn').css('pointer-events', '');
            $('#submit-btn').css('opacity', '1');
            $('#question-add-btn').css('pointer-events', '');
            $('#question-add-btn').css('opacity', '1');
        }
    }

}



// add question to sections
// temporary_storage
function add_question_to_section(question_id, correct_mark, thisTxt) {
    console.log('temp_question_array >>> ', temp_question_array);
    console.log('temp_question_marks_sum >>> ', temp_question_marks_sum);
    console.log('topic_array >>> ', topic_array);
    // current_section_count = 0;
    var current_section_total_sum = parseFloat(total_mark);

    console.log('current_section_total_sum >>> ', current_section_total_sum);


    // ============== validate fields ======================
    if (selected_question_array.includes(parseInt(question_id))) {
        selected_question_array.pop(parseInt(question_id));
        temp_question_array.pop(question_id);
        temp_question_marks_sum = temp_question_marks_sum - parseFloat(correct_mark);
        selected_question_array.push(parseInt(question_id));
        $(thisTxt).html('');
        $(thisTxt).append('<i class="fa fa-plus"></i> Add');
        $(thisTxt).addClass('text-white');
        $(thisTxt).css('background-color', '#118ed7');
    } else {
        temp_question_marks_sum = temp_question_marks_sum + parseFloat(correct_mark);

        if (temp_question_marks_sum > current_section_total_sum) {
            temp_question_marks_sum = temp_question_marks_sum - parseFloat(correct_mark);
            alert('Max. marks exceeded for this assignment');
            return false;
        } else {
            selected_question_array.push(parseInt(question_id));
            temp_question_array.push(question_id);
            $(thisTxt).html('');
            $(thisTxt).append('<i class="fa fa-check"></i> Remove');
            $(thisTxt).addClass('text-white');
            $(thisTxt).css('background-color', 'darkgrey');
        }
    }

    if (topic_array.includes($(thisTxt).attr('topic_name'))) {
        console.log('exisit');
    } else {
        topic_array.push($(thisTxt).attr('topic_name'));
    }

    console.log('question_id >>> ', question_id);
    console.log('correct_mark >>> ', correct_mark);
    console.log('topic_name >>> ', $(thisTxt).attr('topic_name'));


    console.log('temp_question_array ->>> ', temp_question_array);
    console.log('temp_question_marks_sum ->>> ', temp_question_marks_sum);
    console.log('topic_array ->>> ', topic_array);


    console.log('selected_question_array >>> ', selected_question_array);
}


// delete temperory storage
function delete_temperory_storage() {
    temp_question_array = [];
    temp_question_marks_sum = 0;
    topic_array = [];

    console.log('temp_question_array deleted ->> ', temp_question_array);
    console.log('temp_question_marks_sum deleted ->> ', temp_question_marks_sum);
    console.log('topic_array deleted ->> ', topic_array);
    for (var i = 0; i < temp_question_array.length; i++) {
        if (selected_question_array.includes(parseInt(temp_question_array[i]))) {
            selected_question_array.pop(parseInt(temp_question_array[i]));
        }
    }
    console.log('selected_question_array >> ', selected_question_array);
}


// add to assignment
function add_to_assignment() {
    console.log('temp_question_array >> ', temp_question_array);

    if(temp_question_marks_sum < total_mark){
        alert(parseFloat(total_mark - temp_question_marks_sum ) + ' marks question remaining to add to assignment!' );
        return false;
    }else{
        if(temp_question_array.length == 0){
            alert('select atleast 1 question to add on assignment!');
            return false;
        }else{
            $.ajax({
                type: 'GET',
                url: "/paper-management/get-questions",
                data: { 'question_array[]': selected_question_array },
                success: function (response) {
                    Swal.close();
                    console.log('response >> ',response,response['data_list']);
                    question_array = response['data_list'];
                    
                    var topic_str = '';
                    for(var t=0;t<topic_array.length;t++){
                        var topics = '<small><label>'+topic_array[t]+'</label></small>';
                        topic_str = topic_str + topics;
                    }
    
                    var question_append_str = '';
                    for(var i=0;i<response['data_list'].length;i++){
                        var data = '<div class="ques">\
                                        <h5><span >Q.'+(i+1)+'</span> '+response['data_list'][i]['question_text']+'.</h5>\
                                    </div>';
                        question_append_str = question_append_str + data;
                    }
    
                    $('#collapseOne').html('');
                    $('#collapseOne').append('<div class="added-ques">\
                                        <div class="row">\
                                            <div class="col-md-4 pl-0">\
                                                <div class="card ques_sidebar mt-0">\
                                                    <div class="card-content  ">\
                                                        <div class="card-body   pl-1 pr-1">\
                                                            <div class="head">Topics Covered\
                                                            </div>\
                                                            <div class="filter">\
                                                                <div class="options">'+topic_str+'</div>\
                                                            </div>\
                                                        </div>\
                                                    </div>\
                                                </div>\
                                            </div>\
                                            <div class="col-md-8 pt-1">'+question_append_str+'</div>\
                                        </div>\
                                    </div>');
                }
            }).then(function(){
                $('#questions').modal('hide');
            });
        }
    }

}




// submit assignment data
function submitAssignment(){
    assignment_name = $('#assignment_name').val().trim();
    branchID = $('#branch-id').val().trim();
    classID = $('#class-id').val().trim();
    sectionID = $('#section-id').val().trim();
    subjectID = $('#subject-id').val().trim();
    total_mark = $('#total-marks').val().trim();
    passing_mark = $('#passing-marks').val().trim();
    start_at = $('#start-at').val().trim();
    end_at = $('#end-at').val().trim();
    question_type = $('#question-type').val();
    guidelines = $('#assignment-guideline').val();


    if(assignment_name == ''){
        $('#assignment-name-error').removeClass('d-none');
        $('#assignment-name-error').html('');
        $('#assignment-name-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Assignmet title is required.</strong></small>');
        assignment_name_flag = true;
    }else{
        $('#assignment-name-error').addClass('d-none');
        $('#assignment-name-error').html('');
        assignment_name_flag = false;
    }

    // if(branchID == ''){
    //     $('#assignment-branch-error').removeClass('d-none');
    //     $('#assignment-branch-error').html('');
    //     $('#assignment-branch-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch is required.</strong></small>');
    //     branchID_flag = true;
    // }else{
    //     $('#assignment-branch-error').addClass('d-none');
    //     $('#assignment-branch-error').html('');
    //     branchID_flag = false;
    // }
    
    if(classID == ''){
        $('#assignment-class-error').removeClass('d-none');
        $('#assignment-class-error').html('');
        $('#assignment-class-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Class is required.</strong></small>');
        classID_flag = true;
    }else{
        $('#assignment-class-error').addClass('d-none');
        $('#assignment-class-error').html('');
        classID_flag = false;
    }

    if(sectionID == ''){
        $('#assignment-section-error').removeClass('d-none');
        $('#assignment-section-error').html('');
        $('#assignment-section-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Section is required.</strong></small>');
        sectionID_flag = true;
    }else{
        $('#assignment-section-error').addClass('d-none');
        $('#assignment-section-error').html('');
        sectionID_flag = false;
    }

    if(subjectID == ''){
        $('#assignment-subject-error').removeClass('d-none');
        $('#assignment-subject-error').html('');
        $('#assignment-subject-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Subject is required.</strong></small>');
        subjectID_flag = true;
    }else{
        $('#assignment-subject-error').addClass('d-none');
        $('#assignment-subject-error').html('');
        subjectID_flag = false;
    }

    if(total_mark == ''){
        $('#assignment-total-error').removeClass('d-none');
        $('#assignment-total-error').html('');
        $('#assignment-total-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Total marks is required.</strong></small>');
        total_marks_flag = true;
    }else{
        $('#assignment-total-error').addClass('d-none');
        $('#assignment-total-error').html('');
        total_marks_flag = false;
    }

    if(passing_mark == ''){
        $('#assignment-passing-error').removeClass('d-none');
        $('#assignment-passing-error').html('');
        $('#assignment-passing-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Passing marks is required.</strong></small>');
        passing_marks_flag = true;
    }else{
        $('#assignment-passing-error').addClass('d-none');
        $('#assignment-passing-error').html('');
        passing_marks_flag = false;
    }

    if(start_at == ''){
        $('#assignment-start-error').removeClass('d-none');
        $('#assignment-start-error').html('');
        $('#assignment-start-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Start date & time is required.</strong></small>');
        start_flag = true;
    }else{
        $('#assignment-start-error').addClass('d-none');
        $('#assignment-start-error').html('');
        start_flag = false;
    }

    if(end_at == ''){
        $('#assignment-start-error').removeClass('d-none');
        $('#assignment-start-error').html('');
        $('#assignment-start-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;End date & time is required.</strong></small>');
        end_flag = true;
    }else{
        $('#assignment-start-error').addClass('d-none');
        $('#assignment-start-error').html('');
        end_flag = false;
    }

    if(question_type.length == 0){
        $('#assignment-ques-type-error').removeClass('d-none');
        $('#assignment-ques-type-error').html('');
        $('#assignment-ques-type-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Question type is required.</strong></small>');
        question_type_flag = true;
    }else{
        $('#assignment-ques-type-error').addClass('d-none');
        $('#assignment-ques-type-error').html('');
        question_type_flag = false;
    }

    if(guidelines == ''){
        $('#assignment-guideline-error').removeClass('d-none');
        $('#assignment-guideline-error').html('');
        $('#assignment-guideline-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Guideline is required.</strong></small>');
        guideline_flag = true;
    }else{
        $('#assignment-guideline-error').addClass('d-none');
        $('#assignment-guideline-error').html('');
        guideline_flag = false;
    }

    if(question_array.length == 0){
        Swal.fire({
            icon: 'error',
            title: 'Select atleast 1 question to create assignment',
            showConfirmButton: false,
            timer: 2500
        }).then(function () {
            question_flag = true;

        })
    }else{
        question_flag = false;
    }


    if(assignment_name_flag == true || branchID_flag == true || classID_flag == true || sectionID_flag == true || subjectID_flag == true || total_marks_flag == true || passing_marks_flag == true || start_flag == true || end_flag == true || question_type_flag == true || guideline_flag == true || question_flag == true){
        return false;
    }else{

        var formdata = new FormData();
        formdata.append("assignment_name", assignment_name);
        formdata.append("branchID", branchID);
        formdata.append("classID", classID);
        formdata.append("sectionID", sectionID);
        formdata.append("subjectID", subjectID);
        formdata.append("total_mark", total_mark);
        formdata.append("passing_mark", passing_mark);
        formdata.append("start_at", start_at);
        formdata.append("end_at", end_at);
        formdata.append("question_type[]", JSON.stringify(question_type));
        formdata.append("guidelines", guidelines);
        formdata.append("question_array[]", JSON.stringify(selected_question_array));
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-assignment",
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response['response']);
                $('#alert').modal('hide');
                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'New assignment added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'assignment-list';
                    })
                }else {
                    alert('An Error occured while adding new assignment. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}