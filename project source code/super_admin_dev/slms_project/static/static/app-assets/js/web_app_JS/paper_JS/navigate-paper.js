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
var paper_name_flag = false;
var paper_name_exist_flag = false;
var branch_flag = false;
var class_flag = false;
var subject_flag = false;
var year_flag = false;
var total_mark_flag = false;
var passing_mark_flag = false;
var marks_compare_flag = false;


// section variables
var current_section_count = 0;
var selected_question_array = [];
var temporary_storage = [];

// global vaiables
var paper_name = '';
var branchID = '';
var classID = '';
var subjectID = '';
var yearID = '';
var total_mark = '';
var passing_mark = '';
var guidelines = '';

var no_of_sections = '';
var section_details = [];
var sectionalRenderedQuestions = {}

// navigate_to_page_1
function navigate_to_page_1() {
    $('#create-div-section-2').addClass('d-none');
    $('#create-div-section-3').addClass('d-none');
    $('#create-div-section-4').addClass('d-none');
    $('#create-div-section-1').removeClass('d-none');

}

// navigate_to_page_2
function navigate_to_page_2() {
    if (paper_name_exist_flag == true) {
        alert('Paper name already exisit');
        return;
    }

    paper_name = $('#paper-name').val().trim();
    branchID = $('#paper-branch').val().trim();
    classID = $('#paper-class').val().trim();
    subjectID = $('#paper-subject').val().trim();
    yearID = $('#paper-year').val().trim();
    total_mark = $('#paper-total-marks').val().trim();
    passing_mark = $('#paper-passing-marks').val().trim();
    guidelines = $('#paper-guidelines').val().trim();

    if (paper_name == '') {
        $('#paper-name-error').removeClass('d-none');
        $('#paper-name-error').html('');
        $('#paper-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Paper name is required</strong></small>");
        paper_name_flag = true;
    } else {
        $('#paper-name-error').addClass('d-none');
        paper_name_flag = false;
    }

    if (branchID == '') {
        $('#paper-branch-error').removeClass('d-none');
        $('#paper-branch-error').html('');
        $('#paper-branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#paper-branch-error').addClass('d-none');
        branch_flag = false;
    }

    if (classID == '') {
        $('#paper-class-error').removeClass('d-none');
        $('#paper-class-error').html('');
        $('#paper-class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Class is required</strong></small>");
        class_flag = true;
    } else {
        $('#paper-class-error').addClass('d-none');
        class_flag = false;
    }

    if (subjectID == '') {
        $('#paper-subject-error').removeClass('d-none');
        $('#paper-subject-error').html('');
        $('#paper-subject-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Subject is required</strong></small>");
        subject_flag = true;
    } else {
        $('#paper-subject-error').addClass('d-none');
        subject_flag = false;
    }

    if (yearID == '') {
        $('#paper-year-error').removeClass('d-none');
        $('#paper-year-error').html('');
        $('#paper-year-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Year is required</strong></small>");
        year_flag = true;
    } else {
        $('#paper-year-error').addClass('d-none');
        year_flag = false;
    }

    if (total_mark == '') {
        $('#paper-total-marks-error').removeClass('d-none');
        $('#paper-total-marks-error').html('');
        $('#paper-total-marks-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Total marks is required</strong></small>");
        total_mark_flag = true;
    } else {
        $('#paper-total-marks-error').addClass('d-none');
        total_mark_flag = false;
    }

    if (passing_mark == '') {
        $('#paper-passing-marks-error').removeClass('d-none');
        $('#paper-passing-marks-error').html('');
        $('#paper-passing-marks-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Passing marks is required</strong></small>");
        passing_mark_flag = true;
    } else {
        $('#paper-passing-marks-error').addClass('d-none');
        passing_mark_flag = false;
    }


    if (paper_name_flag == true || branch_flag == true || class_flag == true || subject_flag == true || year_flag == true || total_mark_flag == true || passing_mark_flag == true) {
        return false;
    } else {
        $('#create-div-section-1').addClass('d-none');
        $('#create-div-section-3').addClass('d-none');
        $('#create-div-section-4').addClass('d-none');
        $('#create-div-section-2').removeClass('d-none');

        $('#total-mark-second').val('');
        $('#total-mark-second').val(total_mark);
    }
}


// navigate_to_page_3
var section_question_flag = false;
var section_mandatory_question_flag = false;
var section_marks_flag = false;

function navigate_to_page_3() {

    var questionType = [];
    no_of_sections = $('#no-of-section').val().trim();
    for (var i = 0; i < parseInt(no_of_sections); i++) {
        if ($('#section_' + (i + 1) + '_section_type').val().length == 0) {
            $('#section_' + (i + 1) + '_section_type').css('border', '2px solid red');
            alert('Select Question types for Section ' + (i + 1) + '');
            section_details[i]['question_type'] = [];
            return false;
        } else {
            $('#section_' + (i + 1) + '_section_type').css('border', '');
            questionType.push($('#section_' + (i + 1) + '_section_type').val());
            section_details[i]['question_type'] = [];
            section_details[i]['question_type'] = $('#section_' + (i + 1) + '_section_type').val();
        }

    }

    var section_marks_sum = 0;
    $('.total_marks').each(function () {
        if ($(this).val().trim() == '') {
            $(this).css('border', '1px solid red');
            section_marks_flag = true;
        } else {
            $(this).css('border', '');
            section_marks_sum = section_marks_sum + parseInt($(this).val().trim());
            section_marks_flag = false;
            if (parseFloat(total_mark) < parseFloat(section_marks_sum)) {
                section_marks_flag = true;
                alert('Total marks cannot be less than section total marks');
                $(this).css('border', '1px solid red');
                return false;
            } else {
                $(this).css('border', '');
                section_marks_flag = false;
            }

        }
    });

    if (parseFloat(total_mark) > parseFloat(section_marks_sum)) {
        section_marks_flag = true;
        alert('Total marks cannot be greater than section total marks');
        $(this).css('border', '1px solid red');
        return false;
    } else {
        $(this).css('border', '');
        section_marks_flag = false;
    }

    $('.qno').each(function () {
        if ($(this).val().trim() == '') {
            $(this).css('border', '1px solid red');
            section_question_flag = true;
        } else {
            $(this).css('border', '');
            section_question_flag = false;
        }
    });

    $('.mandatory').each(function () {
        if ($(this).val().trim() == '') {
            $(this).css('border', '1px solid red');
            section_mandatory_question_flag = true;
        } else {
            $(this).css('border', '');
            section_mandatory_question_flag = false;
        }
    });

    if (section_question_flag == true || section_mandatory_question_flag == true || section_marks_flag == true) {
        return false;
    } else {
        console.log('section_details >>> ', section_details);
        // =================  render sectional area  =============================================
        var section_div_str = '';
        for (var i = 0; i < parseInt(no_of_sections); i++) {
            var data = '<div class="card-header"  data-parent="#accordion" href="#collapse_' + (i + 1) + '">\
                            <a class="card-title">\
                            Section '+ (i + 1) + ' <span class="float-right">Max. Marks: ' + section_details[i]['section_total_marks'] + '</span>\
                            </a>\
                        </div>\
                        <div id="collapse_'+ (i + 1) + '" class="">\
                            <div id="collapse_append_'+ (i + 1) + '"></div>\
                            <a data-toggle="modal" data-target="#questions" href="javascript:;" data-keyboard="false" data-backdrop="static" class="add-ques-btn" onclick="get_modal_question('+ i + ')">+ Add Questions</a>\
                        </div>';
            section_div_str = section_div_str + data;
        }
        $('#sections-div-append').html('');
        $('#sections-div-append').append(section_div_str);
        $('#total-add-question-div-marks').html('');
        $('#total-add-question-div-marks').append(total_mark);
        $('#add-question-div-name').html('');
        $('#add-question-div-name').append(paper_name);
        // =======================================================================================
        $('#create-div-section-1').addClass('d-none');
        $('#create-div-section-2').addClass('d-none');
        $('#create-div-section-4').addClass('d-none');
        $('#create-div-section-3').removeClass('d-none');
    }
}


// navigate_to_page_4
function navigate_to_page_4() {
    console.log('temp_question_array >> ', section_details);
    // validate sectional marks and sectional total questions data
    // ------------------------------------------------------------

    // ============================================================
    // render data to the paper preview page
    // ------------------------------------------------------------
    $('#unique_paper_name').html('');
    $('#unique_paper_name').append(paper_name);

    $('#confirm-modal-paper-name').html('');
    $('#confirm-modal-paper-name').append(paper_name);

    $('#class_name').html('');
    $('#class_name').append(classID);

    $('#subject_name').html('');
    $('#subject_name').append(subjectID);

    $('#year_name').html('');
    $('#year_name').append(yearID);

    $('#totalMarks').html('');
    $('#totalMarks').append(total_mark);

    $('#passingMarks').html('');
    $('#passingMarks').append(passing_mark);

    $('#guideLines').html('');
    $('#guideLines').append($('#paper-guidelines').val());

    $('#totalSections').html('');
    $('#totalSections').append(section_details.length);

    // append sectional details
    var secDetailString = '';
    for(var s=0;s<section_details.length;s++){
        var qtypeStr = '';
        for(var q=0;q<section_details[s]['question_type'].length;q++){
            if(section_details[s]['question_type'][q] == '1'){
                qtypeStr = qtypeStr + 'Objective, ';
            }
            if(section_details[s]['question_type'][q] == '2'){
                qtypeStr = qtypeStr + 'Subjective, ';
            }
            if(section_details[s]['question_type'][q] == '3'){
                qtypeStr = qtypeStr + 'MCQ, ';
            }
            if(section_details[s]['question_type'][q] == '4'){
                qtypeStr = qtypeStr + 'Diagram Upload, ';
            }
        }
        var data = '<div class="row">\
                        <div class="col-lg-2    form-group">\
                        <p class="value">Section '+(s+1)+'</p>\
                    </div>\
                        <div class="col-lg-2    form-group">\
                        <p class="value">'+section_details[s]['no_of_questions']+'</p>\
                    </div>\
                        <div class="col-lg-2    form-group">\
                        <p class="value">'+section_details[s]['mandatory_questions']+'</p>\
                    </div>\
                    <div class="col-lg-3    form-group">\
                        <p class="value"><small>'+qtypeStr+'</small></p>\
                    </div>\
                    <div class="col-lg-3    form-group">\
                        <p class="value">'+section_details[s]['section_total_marks']+'</p>\
                    </div>\
                </div>';
        secDetailString = secDetailString + data;
    }
    $('#sectionRowDataAppend').html('');
    $('#sectionRowDataAppend').append('<div class="row">\
                                            <div class="col-lg-2    form-group">\
                                            <label>Section </label>\
                                        </div>\
                                            <div class="col-lg-2   form-group">\
                                            <label>No. of Questions </label>\
                                        </div>\
                                            <div class="col-lg-2  form-group">\
                                            <label>Mandatory   Questions </label>\
                                        </div>\
                                        <div class="col-lg-3    form-group">\
                                            <label>Question  Type </label>\
                                        </div>\
                                        <div class="col-lg-3   form-group">\
                                            <label>Total Marks Per Section </label>\
                                        </div>\
                                        </div>'+secDetailString+'');

    // append question details
    var questionStr = '';
    console.log('dict no_of_sections >>>',no_of_sections);
    console.log('sectionalRenderedQuestions >>> ',sectionalRenderedQuestions);

    for(var k=0;k<parseInt(no_of_sections);k++){
        var questionStrData = '';
        console.log('sec data >>> ',sectionalRenderedQuestions['Section_'+(k+1)+''],sectionalRenderedQuestions['Section_'+(k+1)+''].length);

        for(var q=0;q<sectionalRenderedQuestions['Section_'+(k+1)+''].length;q++){
            var qdata = '<div class="ques">\
                            <h5><span>Q.'+(q+1)+'</span> '+sectionalRenderedQuestions['Section_'+(k+1)+''][q]['question_text']+'  </h5>\
                        </div>';
            questionStrData = questionStrData + qdata;
        }
        var data = '<div class="col-lg-12 mt-1 mb-0 form-group">\
                        <h5 class="font-weight-bold" style="border: 1px solid #e5e5e5;border-radius: 5px;padding: 3px;background: #a4a4c7;color: white;padding-left: 5px;">Section '+(k+1)+' </h5>'+questionStrData+'\
                    </div>\
                    <div class="col-lg-12 mt-0   pl-0  form-group  added-ques d-block">\
                        </div>\
                    </div>';
        questionStr = questionStr + data;
    }
    $('#questionSectionDataAppend').html('');
    $('#questionSectionDataAppend').append(questionStr);
    console.log('sectionalRenderedQuestions >>> ',sectionalRenderedQuestions);


    // ============================================================
    $('#create-div-section-1').addClass('d-none');
    $('#create-div-section-2').addClass('d-none');
    $('#create-div-section-3').addClass('d-none');
    $('#create-div-section-4').removeClass('d-none');
}


// get subjects from classID
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
                $('#paper-subject').html('');
                $('#paper-subject').append(subject_data);
                $('#paper-subject').selectpicker('refresh');

                $('#modal-paper-subject').html('');
                $('#modal-paper-subject').append(subject_data);
                $('#modal-paper-subject').selectpicker('refresh');

                $('#modal-question-id').val($(thisTxt).val().trim());
                $('#modal-question-id').selectpicker('refresh');
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
        url: "/question-bank-management/fetch-topics",
        data: { 'classID': $('#paper-class').val().trim(), 'subjectID': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            $('#modal-paper-subject').val($(thisTxt).val().trim());
            $('#modal-paper-subject').selectpicker('refresh');
            console.log(response['topicsList']);
            topic_data = '';
            topic_data = "<option class='d-none' value=''>Select Topic </option>";
            if (response['topicsList'].length > 0) {
                for (var i = 0; i < response['topicsList'].length; i++) {
                    var dataStr = '<option value="' + response['topicsList'][i] + '">' + response['topicsList'][i] + '</option>';
                    topic_data = topic_data + dataStr;
                }
                $('#modal-topic-id').html('');
                $('#modal-topic-id').append(topic_data);
                $('#modal-topic-id').selectpicker('refresh');
            } else {
                $('#modal-topic-id').html('');
                $('#modal-topic-id').selectpicker('refresh');
            }
        }
    }).then(function () {
        no_of_sections = '';
        $('#render-section-area').addClass('d-none');
        $('#section-data').html('');
        $('select').selectpicker();
        $('#no-of-section-error').removeClass('d-none');
        $('#no-of-section-error').html('');
        $('#no-of-section').val('');
        section_details = [];
    });
}

// check paper name
function check_paper_name(thisTxt) {
    $.ajax({
        type: 'GET',
        url: "/paper-management/check-paper-name",
        data: { 'search_string': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            if (response['message'] == 'exist') {
                $('#paper-name-error').removeClass('d-none');
                $('#paper-name-error').html('');
                $('#paper-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Paper name already exist</strong></small>");
                paper_name_exist_flag = true;
            } else {
                $('#paper-name-error').addClass('d-none');
                paper_name_exist_flag = false;
            }

            // button enabled/disable
            if (paper_name_exist_flag == true) {
                $('#next_btn_1').css('pointer-events', 'none');
                $('#next_btn_1').css('opacity', '0.2');
            } else {
                $('#next_btn_1').css('pointer-events', '');
                $('#next_btn_1').css('opacity', '1');
            }
        }
    });
}

// compare total marks and passing marks
function compare_marks() {
    total_mark = $('#paper-total-marks').val().trim();
    passing_mark = $('#paper-passing-marks').val().trim();

    if (total_mark != '' && passing_mark != '') {
        if (parseFloat(passing_mark) > parseFloat(total_mark)) {
            alert('Passing marks cannot be greater than total marks!');
            $('#paper-passing-marks').val('');
            $('#paper-passing-marks-error').removeClass('d-none');
            $('#paper-passing-marks-error').html('');
            $('#paper-passing-marks-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Passing marks cannot be greater than total marks</strong></small>");
            passing_mark_flag = true;
            return false;
        }
    }

    if (total_mark == '' && passing_mark != '') {
        alert('Enter total marks!');
        $('#paper-passing-marks').val('');
        $('#paper-total-marks-error').removeClass('d-none');
        $('#paper-total-marks-error').html('');
        $('#paper-total-marks-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Enter total marks</strong></small>");
        passing_mark_flag = true;
        return false;
    }

    else {
        $('#paper-passing-marks-error').addClass('d-none');
        $('#paper-passing-marks-error').html('');
        $('#paper-total-marks-error').addClass('d-none');
        $('#paper-total-marks-error').html('');
        passing_mark_flag = false;
    }
}



// render sections details
function render_section(thisTxt) {
    if ($(thisTxt).val().trim() != '' && $(thisTxt).val().trim() != 0 && $(thisTxt).val().trim() != 00 && $(thisTxt).val().trim() != 000) {
        var optionStr = '';
        section_details = [];
        for (var i = 0; i < $(thisTxt).val().trim(); i++) {
            var data = '<tr>\
                            <td>\
                            <span class="sno text-primary"><strong>Section '+ (i + 1) + '</strong></span>\
                            </td>\
                            <td><input type="text" name="" onkeypress="return /[0-9]/i.test(event.key)" onkeyup="check_section_fields(this)" maxlength="2" field_type="qno" id="section_'+ (i + 1) + '_qno" class="qno form-control"></td>\
                            <td><input type="text" name="" onkeypress="return /[0-9]/i.test(event.key)" onkeyup="check_section_fields(this)" maxlength="2" field_type="mandatory" id="section_'+ (i + 1) + '_mandatory" class="mandatory form-control"></td>\
                            <td>\
                            <select  title="Question Type" id="section_'+ (i + 1) + '_section_type" class="selectpicker d-block question_type_data" multiple data-live-search="false">\
                            <option value="1">Objective</option>\
                            <option  value="2">Subjective</option>\
                            <option  value="3">Multiple Choice Objective</option>\
                            <option  value="4">Diagram Upload</option>\
                            </select>\
                        </td>\
                            <td><input type="text" name="" onkeypress="return /[0-9]/i.test(event.key)" onkeyup="check_section_fields(this)" maxlength="2" field_type="total_marks" id="section_'+ (i + 1) + '_total_marks" class="total_marks form-control"></td>\
                        </tr>';
            optionStr = optionStr + data;
            // appending data into section_details variable
            // ==============================================================
            dataDict = {};
            dataDict['section_name'] = "Section_" + (i + 1) + "";
            dataDict['no_of_questions'] = 0;
            dataDict['mandatory_questions'] = 0;
            dataDict['question_type'] = [];
            dataDict['section_total_marks'] = 0;
            dataDict['question_array'] = [];

            // extra parameters for question add in paper and validation
            dataDict['question_sum'] = 0;
            dataDict['question_count'] = 0;
            dataDict['topic_array'] = [];
            // ==============================================================
            section_details.push(dataDict);
            sectionalRenderedQuestions["Section_" + (i + 1) + ""] = [];
        }

        $('#render-section-area').removeClass('d-none');
        $('#section-data').html('');
        $('#section-data').append(optionStr);
        $('select').selectpicker();
        $('#no-of-section-error').addClass('d-none');
        $('#no-of-section-error').html('');
    } else {
        $('#render-section-area').addClass('d-none');
        $('#section-data').html('');
        $('select').selectpicker();
        $('#no-of-section-error').removeClass('d-none');
        $('#no-of-section-error').html('');
        $('#no-of-section-error').append('<small><strong>Enter valid no. of sections</strong></small>');
        $('#no-of-section').val('');
        section_details = [];
    }

    console.log('section_details >>> ', section_details);


}

// validate sections total_question, madator_question and section_total_marks dta
function check_section_fields(thisTxt) {
    var field_type = $(thisTxt).attr('field_type');
    sectionCounter = $(thisTxt).attr('id').split('_')[1];
    var currentSection = 'section_' + sectionCounter;

    var sectionQuestion = $('#' + currentSection + '_qno').val().trim();
    var sectionMandatoryQuestion = $('#' + currentSection + '_mandatory').val().trim();

    if (field_type.trim() == 'qno') {
        if (sectionQuestion != '' && sectionQuestion != 0 && sectionQuestion != 00 && sectionQuestion != 000 && sectionMandatoryQuestion != '' && sectionMandatoryQuestion != 0 && sectionMandatoryQuestion != 00 && sectionMandatoryQuestion != 000) {
            if (parseInt(sectionQuestion) >= parseInt(sectionMandatoryQuestion)) {
                $('#' + currentSection + '_qno').css('border', '');
                $('#no-of-question-error').addClass('d-none');
                $('#no-of-question-error').html('');
                $('#next_btn_2').css('pointer-events', '');
                $('#next_btn_2').css('opacity', '1');

                section_details[sectionCounter - 1]['no_of_questions'] = 0;
                section_details[sectionCounter - 1]['no_of_questions'] = parseInt($('#' + currentSection + '_qno').val().trim());
            } else {
                $('#' + currentSection + '_qno').css('border', '2px solid red');
                $('#no-of-question-error').removeClass('d-none');
                $('#no-of-question-error').html('');
                $('#no-of-question-error').append('<small><strong>Total section question cannot be less than mandatory question</strong></small>');
                $('#next_btn_2').css('pointer-events', 'none');
                $('#next_btn_2').css('opacity', '0.2');
                section_details[sectionCounter - 1]['no_of_questions'] = 0;
            }
        } else {
            section_details[sectionCounter - 1]['no_of_questions'] = 0;
            section_details[sectionCounter - 1]['no_of_questions'] = parseInt($('#' + currentSection + '_qno').val().trim());
            $('#' + currentSection + '_mandatory').val(parseInt($('#' + currentSection + '_qno').val().trim()));
            section_details[sectionCounter - 1]['mandatory_questions'] = 0;
            section_details[sectionCounter - 1]['mandatory_questions'] = parseInt($('#' + currentSection + '_qno').val().trim());
        }
    } else if (field_type.trim() == 'mandatory') {
        if (sectionQuestion != '' && sectionQuestion != 0 && sectionQuestion != 00 && sectionQuestion != 000 && sectionMandatoryQuestion != '' && sectionMandatoryQuestion != 0 && sectionMandatoryQuestion != 00 && sectionMandatoryQuestion != 000) {
            if (parseInt(sectionQuestion) >= parseInt(sectionMandatoryQuestion)) {
                $('#' + currentSection + '_mandatory').css('border', '');
                $('#no-of-question-error').addClass('d-none');
                $('#no-of-question-error').html('');
                $('#next_btn_2').css('pointer-events', '');
                $('#next_btn_2').css('opacity', '1');
                section_details[sectionCounter - 1]['mandatory_questions'] = 0;
                section_details[sectionCounter - 1]['mandatory_questions'] = parseInt(sectionMandatoryQuestion);
            } else {
                $('#' + currentSection + '_mandatory').css('border', '2px solid red');
                $('#no-of-question-error').removeClass('d-none');
                $('#no-of-question-error').html('');
                $('#no-of-question-error').append('<small><strong>Total section question cannot be less than mandatory question</strong></small>');
                $('#next_btn_2').css('pointer-events', 'none');
                $('#next_btn_2').css('opacity', '0.2');
                section_details[sectionCounter - 1]['mandatory_questions'] = 0;
            }
        }

    } else if (field_type.trim() == 'total_marks') {
        if (parseFloat($('#' + currentSection + '_total_marks').val().trim()) >= parseFloat(total_mark)) {
            $('#' + currentSection + '_total_marks').css('border', '2px solid red');
            $('#no-of-question-error').removeClass('d-none');
            $('#no-of-question-error').html('');
            $('#no-of-question-error').append('<small><strong>Total marks cannot be less than section total marks.</strong></small>');
            $('#next_btn_2').css('pointer-events', 'none');
            $('#next_btn_2').css('opacity', '0.2');
            section_details[sectionCounter - 1]['section_total_marks'] = 0;
        } else {
            $('#' + currentSection + '_total_marks').css('border', '');
            $('#no-of-question-error').addClass('d-none');
            $('#no-of-question-error').html('');
            $('#next_btn_2').css('pointer-events', '');
            $('#next_btn_2').css('opacity', '1');
            section_details[sectionCounter - 1]['section_total_marks'] = 0;
            section_details[sectionCounter - 1]['section_total_marks'] = parseFloat($('#' + currentSection + '_total_marks').val().trim());
        }
    }
}


var temp_question_array = [];
var temp_question_marks_sum = 0;
var temp_question_count = 0;
var temp_topic_array = []
// get questions according to section selection
function get_modal_question(sectionID) {


    current_section_count = sectionID;
    var classID = $('#paper-class').val().trim();
    var subjectID = $('#paper-subject').val().trim();
    var branchID = $('#paper-branch').val().trim();

    console.log('classid >> ', classID);
    console.log('subjectid >> ', subjectID);
    console.log('sectionID >> ', sectionID);

    console.log('section data >> ', section_details[sectionID]['question_type']);

    temp_question_array = section_details[sectionID]['question_array'];
    temp_question_marks_sum = section_details[sectionID]['question_sum'];
    temp_question_count = section_details[sectionID]['question_count'];
    temp_topic_array = section_details[sectionID]['topic_array'];

    console.log('temp_question_array >> ', temp_question_array);
    console.log('temp_question_marks_sum >> ', temp_question_marks_sum);
    console.log('temp_question_count >> ', temp_question_count);
    console.log('temp_topic_array >> ', temp_topic_array);

    // return false;
    // appending questions into the modal
    // ========================= ajax call ========================================
    $.ajax({
        type: 'GET',
        url: "/paper-management/fetch-questions",
        data: {'branch_id': branchID, 'class_id': classID, 'subject_id': subjectID, 'qType[]': section_details[sectionID]['question_type'] },
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
                $('#total-fetched-questions').html('');
                $('#total-fetched-questions').append(response['data_list'].length);
            } else {
                $('#no-quest-div').removeClass('d-none');
                $('#example1').addClass('d-none');
                $('#total-fetched-questions').html('');
                $('#total-fetched-questions').append('0');
                $('#new-question-append').html('');
            }
        }
    });
    // ============================================================================
}


// add question to sections
// temporary_storage
function add_question_to_section(question_id, correct_mark, thisTxt) {
    console.log('temp_question_array >>> ', temp_question_array);
    console.log('temp_question_marks_sum >>> ', temp_question_marks_sum);
    console.log('temp_question_count >>> ', temp_question_count);
    console.log('temp_topic_array >>> ', temp_topic_array);
    // current_section_count = 0;
    var current_section_total_questions = parseInt(section_details[current_section_count]['no_of_questions']);
    var current_section_total_sum = parseFloat(section_details[current_section_count]['section_total_marks']);

    console.log('current_section_total_questions >>> ', current_section_total_questions);
    console.log('current_section_total_sum >>> ', current_section_total_sum);


    // ============== validate fields ======================
    if (selected_question_array.includes(parseInt(question_id))) {
        selected_question_array.pop(parseInt(question_id));
        temp_question_array.pop(question_id);
        temp_question_marks_sum = temp_question_marks_sum - parseFloat(correct_mark);
        temp_question_count = temp_question_count - 1;
        selected_question_array.push(parseInt(question_id));
        $(thisTxt).html('');
        $(thisTxt).append('<i class="fa fa-plus"></i> Add');
        $(thisTxt).addClass('text-white');
        $(thisTxt).css('background-color', '#118ed7');
    } else {
        temp_question_marks_sum = temp_question_marks_sum + parseFloat(correct_mark);
        temp_question_count = temp_question_count + 1;

        if (temp_question_count > current_section_total_questions) {
            temp_question_marks_sum = temp_question_marks_sum - parseFloat(correct_mark);
            temp_question_count = temp_question_count - 1;
            alert('Max. question count exceeded for this section');
            return false;
        } else if (temp_question_marks_sum > current_section_total_sum) {
            temp_question_marks_sum = temp_question_marks_sum - parseFloat(correct_mark);
            temp_question_count = temp_question_count - 1;
            alert('Max. marks exceeded for this section');
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

    if (temp_topic_array.includes($(thisTxt).attr('topic_name'))) {
        console.log('exisit');
    } else {
        temp_topic_array.push($(thisTxt).attr('topic_name'));
    }

    console.log('current_section_count >>> ', current_section_count);
    console.log('question_id >>> ', question_id);
    console.log('correct_mark >>> ', correct_mark);
    console.log('topic_name >>> ', $(thisTxt).attr('topic_name'));


    console.log('temp_question_array ->>> ', temp_question_array);
    console.log('temp_question_marks_sum ->>> ', temp_question_marks_sum);
    console.log('temp_question_count ->>> ', temp_question_count);
    console.log('temp_topic_array ->>> ', temp_topic_array);


    console.log('selected_question_array >>> ', selected_question_array);
}


// delete temperory storage
function delete_temperory_storage() {
    temp_question_array = [];
    temp_question_marks_sum = 0;
    temp_question_count = 0;
    temp_topic_array = [];

    console.log('temp_question_array deleted ->> ', temp_question_array);
    console.log('temp_question_marks_sum deleted ->> ', temp_question_marks_sum);
    console.log('temp_question_count deleted ->> ', temp_question_count);
    console.log('temp_topic_array deleted ->> ', temp_topic_array);
    for (var i = 0; i < temp_question_array.length; i++) {
        if (selected_question_array.includes(parseInt(temp_question_array[i]))) {
            selected_question_array.pop(parseInt(temp_question_array[i]));
        }
    }

    console.log('section_details >> ', section_details);
}

// add to paper
function add_to_paper() {
    console.log('current_section_count >>> ', current_section_count);

    section_details[current_section_count]['question_array'] = temp_question_array;
    section_details[current_section_count]['question_sum'] = temp_question_marks_sum;
    section_details[current_section_count]['question_count'] = temp_question_count;
    section_details[current_section_count]['topic_array'] = temp_topic_array;

    console.log('temp_question_array >> ', section_details);

    if(section_details[current_section_count]['question_array'].length == 0){
        alert('select atleast 1 question to add on paper!');
        return false;
    }else{
        $.ajax({
            type: 'GET',
            url: "/paper-management/get-questions",
            data: { 'question_array[]': section_details[current_section_count]['question_array'] },
            success: function (response) {
                Swal.close();
                console.log('response >> ',response['question_list']);
                sectionalRenderedQuestions["Section_" + (current_section_count + 1) + ""] = response['question_list'];
                
                var topic_str = '';
                for(var t=0;t<section_details[current_section_count]['topic_array'].length;t++){
                    var topics = '<small><label>'+section_details[current_section_count]['topic_array']+'</label></small>';
                    topic_str = topic_str + topics;
                }

                var question_append_str = '';
                for(var i=0;i<response['question_list'].length;i++){
                    var data = '<div class="ques">\
                                    <h5><span >Q.'+(i+1)+'</span> '+response['question_list'][i]['question_text']+'. <a href="javascript:;" class="float-right del" question_id="'+response['question_list'][i]['id']+'"><i class="fa fa-trash"></i></a></h5>\
                                </div>';
                    question_append_str = question_append_str + data;
                }

                $('#collapse_append_'+ (current_section_count+1) + '').html('');
                $('#collapse_append_'+ (current_section_count+1) + '').append('<div class="added-ques">\
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
        });
    }
}





// submit paper data
function submitPaper(){
    var formdata = new FormData();
    formdata.append("paperName", paper_name);
    formdata.append("branchID", branchID);
    formdata.append("classID", classID);
    formdata.append("subjectID", subjectID);
    formdata.append("yearID", yearID);
    formdata.append("totalMarks", total_mark);
    formdata.append("passingMarks", passing_mark);
    formdata.append("sectionCount", no_of_sections);
    formdata.append("sectionDetail[]", JSON.stringify(section_details));
    // ---------------  AJAX CALL  ----------------------------
    Swal.showLoading();
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "add-paper",
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
                    title: 'New paper added successfully.',
                    showConfirmButton: false,
                    timer: 2000
                }).then(function () {
                    window.location.href = 'paper-list';
                })
            }else {
                alert('An Error occured while adding new paper. Please try again!');
                return false;
            }
        }
    });
    // --------------------------------------------------------
}



// get class from branch-id
function get_class(thisTxt) {
    topic_array = [];
    $('#paper-class').html('');
    $('#paper-class').append("<option class='d-none' value=''>Select Class </option>");
    $('#paper-class').selectpicker('refresh');

    $('#paper-subject').html('');
    $('#paper-subject').append("<option class='d-none' value=''>Select Subject </option>");
    $('#paper-subject').selectpicker('refresh');

    // Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "/exam-management/fetch-class",
        data: { 'branchID': $(thisTxt).val().trim() },
        success: function (response) {
            // Swal.close();
            console.log(response['classList']);
            if(response['classList'].length == 0){
                $('#paper-class').html('');
                $('#paper-class').append('<option value="" class="d-none">No Class Available for this branch</option>'+classStr);
                $('#paper-class').selectpicker('refresh');
                $('#paper-branch-error').removeClass('d-none');
                $('#paper-branch-error').html('');
                $('#paper-branch-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class Available for this branch</strong></small>');
                $('#next_btn_1').css('pointer-events', 'none');
                $('#next_btn_1').css('opacity', '0.2');
            }else{
                var classStr = '';
                for(var i=0;i<response['classList'].length;i++){
                    var data = '<option value="'+response['classList'][i]['id']+'">'+response['classList'][i]['class_name']+'</option>';
                    classStr = classStr + data;
                }
                $('#paper-class').html('');
                $('#paper-class').append('<option value="" class="d-none">Select Class</option>'+classStr);
                $('#paper-class').selectpicker('refresh');
                $('#paper-branch-error').removeClass('d-none');
                $('#paper-branch-error').html('');
                $('#next_btn_1').css('pointer-events', '');
                $('#next_btn_1').css('opacity', '1');
            }
        }
    });
}