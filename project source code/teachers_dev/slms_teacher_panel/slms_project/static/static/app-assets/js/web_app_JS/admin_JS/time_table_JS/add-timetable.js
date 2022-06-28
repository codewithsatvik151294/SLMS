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

// global variable & global flags
var branch = '';
var branch_flag = false;

var session = '';
var session_flag = false;

var year = '';
var year_flag = false;

var effective_from = '';
var effective_from_flag = false;

var class_id = '';
var class_flag = false;

var section_id = '';
var section_flag = false;

var slot_flag = false;
var monday_slot = {};
var tuesday_slot = {};
var wednesday_slot = {};
var thursday_slot = {};
var friday_slot = {};
var saturday_slot = {};


// store_time_table_data
function store_time_table_data(){

    branch = $('#branch-id').val().trim();
    session = $('#session-id').val().trim();
    year = $('#year-id').val().trim();
    effective_from = $('#effective-id').val().trim();
    class_id = $('#class-id').val().trim();
    section_id = $('#section-id').val().trim();

    // field validation
    if (branch == '') {
        $('#branch-error').removeClass('d-none');
        $('#branch-error').html('');
        $('#branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#branch-error').addClass('d-none');
        branch_flag = false;
    }

    if (session == '') {
        $('#session-error').removeClass('d-none');
        $('#session-error').html('');
        $('#session-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Session is required</strong></small>");
        session_flag = true;
    } else {
        $('#session-error').addClass('d-none');
        session_flag = false;
    }

    if (year == '') {
        $('#year-error').removeClass('d-none');
        $('#year-error').html('');
        $('#year-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Year is required</strong></small>");
        year_flag = true;
    } else {
        $('#year-error').addClass('d-none');
        year_flag = false;
    }

    if (effective_from == '') {
        $('#effective-error').removeClass('d-none');
        $('#effective-error').html('');
        $('#effective-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Effective month is required</strong></small>");
        effective_from_flag = true;
    } else {
        $('#effective-error').addClass('d-none');
        effective_from_flag = false;
    }

    if (class_id == '') {
        $('#class-error').removeClass('d-none');
        $('#class-error').html('');
        $('#class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Class is required</strong></small>");
        class_flag = true;
    } else {
        $('#class-error').addClass('d-none');
        class_flag = false;
    }

    if (section_id == '') {
        $('#section-error').removeClass('d-none');
        $('#section-error').html('');
        $('#section-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Section is required</strong></small>");
        section_flag = true;
    } else {
        $('#section-error').addClass('d-none');
        section_flag = false;
    }

    
    if(branch_flag == true || session_flag == true || year_flag == true || effective_from_flag == true || class_flag == true || section_flag == true){
        return false;
    }
    
    // storing slots data daywise (monday -> saturday)
    var rowCount = $('#time-table-slot-data tr').length;
    console.log('rowCount >>> ',rowCount);

    for(var i=0;i<rowCount;i++){
        var start_time = $('#start-time-slot-'+i+'').val().trim();
        var end_time = $('#end-time-slot-'+i+'').val().trim();

        if(start_time == ''){
            $('#start-time-slot-'+i+'').css('border','2px solid red');
            return false;
        }else{
            $('#start-time-slot-'+i+'').css('border','');
        }
        if(end_time == ''){
            $('#end-time-slot-'+i+'').css('border','2px solid red');
            return false;
        }else{
            $('#end-time-slot-'+i+'').css('border','');
        }

        // var date1 = new Date($('#start_'+paperID+'').val());
        // var date2 = new Date($('#end_'+paperID+'').val());
        // if(date1.getTime() < date2.getTime()){
        //     exam_data[i]['paper_start_date_time'] = date1;
        //     exam_data[i]['paper_end_date_time'] = date2;
        // }

        var monday_subject_id = $('#monday-subject-slot-'+i+'').val().trim();
        var monday_teache_id = $('#monday-teacher-slot-'+i+'').val().trim();

        var monday_subject_name = $('#monday-subject-slot-'+i+' option:selected' ).text().trim();
        var monday_teache_name = $('#monday-teacher-slot-'+i+' option:selected' ).text().trim();
        if(monday_subject_name == 'Select Subject'){
            monday_subject_name = '-'
        }
        if(monday_teache_name == 'No Teacher Available'){
            monday_teache_name = '-'
        }
        var slotDict = {};
        slotDict['startAt'] = start_time;
        slotDict['endAt'] = end_time;
        slotDict['subject'] = monday_subject_id;
        slotDict['teacher'] = monday_teache_id;
        slotDict['subject_name'] = monday_subject_name;
        slotDict['teacher_name'] = monday_teache_name;
        monday_slot['slot_'+(i+1)+''] = slotDict;
        delete(slotDict);

        var tuesday_subject_id = $('#tuesday-subject-slot-'+i+'').val().trim();
        var tuesday_teache_id = $('#tuesday-teacher-slot-'+i+'').val().trim();
        var tuesday_subject_name = $('#tuesday-subject-slot-'+i+' option:selected' ).text().trim();
        var tuesday_teache_name = $('#tuesday-teacher-slot-'+i+' option:selected' ).text().trim();
        if(tuesday_subject_name == 'Select Subject'){
            tuesday_subject_name = '-'
        }
        if(tuesday_teache_name == 'No Teacher Available'){
            tuesday_teache_name = '-'
        }
        var slotDict = {};
        slotDict['startAt'] = start_time;
        slotDict['endAt'] = end_time;
        slotDict['subject'] = tuesday_subject_id;
        slotDict['teacher'] = tuesday_teache_id;
        slotDict['subject_name'] = tuesday_subject_name;
        slotDict['teacher_name'] = tuesday_subject_name;
        tuesday_slot['slot_'+(i+1)+''] = slotDict;
        delete(slotDict);

        var wednesday_subject_id = $('#wednesday-subject-slot-'+i+'').val().trim();
        var wednesday_teache_id = $('#wednesday-teacher-slot-'+i+'').val().trim();
        var wednesday_subject_name = $('#wednesday-subject-slot-'+i+' option:selected' ).text().trim();
        var wednesday_teache_name = $('#wednesday-teacher-slot-'+i+' option:selected' ).text().trim();
        if(wednesday_subject_name == 'Select Subject'){
            wednesday_subject_name = '-'
        }
        if(wednesday_teache_name == 'No Teacher Available'){
            wednesday_teache_name = '-'
        }
        var slotDict = {};
        slotDict['startAt'] = start_time;
        slotDict['endAt'] = end_time;
        slotDict['subject'] = wednesday_subject_id;
        slotDict['teacher'] = wednesday_teache_id;
        slotDict['subject_name'] = wednesday_subject_name;
        slotDict['teacher_name'] = wednesday_teache_name;
        wednesday_slot['slot_'+(i+1)+''] = slotDict;
        delete(slotDict);

        var thursday_subject_id = $('#thursday-subject-slot-'+i+'').val().trim();
        var thursday_teache_id = $('#thursday-teacher-slot-'+i+'').val().trim();
        var thursday_subject_name = $('#thursday-subject-slot-'+i+' option:selected' ).text().trim();
        var thursday_teache_name = $('#thursday-teacher-slot-'+i+' option:selected' ).text().trim();
        if(thursday_subject_name == 'Select Subject'){
            thursday_subject_name = '-'
        }
        if(thursday_teache_name == 'No Teacher Available'){
            thursday_teache_name = '-'
        }
        var slotDict = {};
        slotDict['startAt'] = start_time;
        slotDict['endAt'] = end_time;
        slotDict['subject'] = thursday_subject_id;
        slotDict['teacher'] = thursday_teache_id;
        slotDict['subject_name'] = thursday_subject_name;
        slotDict['teacher_name'] = thursday_teache_name;
        thursday_slot['slot_'+(i+1)+''] = slotDict;
        delete(slotDict);

        var friday_subject_id = $('#friday-subject-slot-'+i+'').val().trim();
        var friday_teache_id = $('#friday-teacher-slot-'+i+'').val().trim();
        var friday_subject_name = $('#friday-subject-slot-'+i+' option:selected' ).text().trim();
        var friday_teache_name = $('#friday-teacher-slot-'+i+' option:selected' ).text().trim();
        if(friday_subject_name == 'Select Subject'){
            friday_subject_name = '-'
        }
        if(friday_teache_name == 'No Teacher Available'){
            friday_teache_name = '-'
        }
        var slotDict = {};
        slotDict['startAt'] = start_time;
        slotDict['endAt'] = end_time;
        slotDict['subject'] = friday_subject_id;
        slotDict['teacher'] = friday_teache_id;
        slotDict['subject_name'] = friday_subject_name;
        slotDict['teacher_name'] = friday_teache_name;
        friday_slot['slot_'+(i+1)+''] = slotDict;
        delete(slotDict);

        var saturday_subject_id = $('#saturday-subject-slot-'+i+'').val().trim();
        var saturday_teache_id = $('#saturday-teacher-slot-'+i+'').val().trim();
        var saturday_subject_name = $('#saturday-subject-slot-'+i+' option:selected' ).text().trim();
        var saturday_teache_name = $('#saturday-teacher-slot-'+i+' option:selected' ).text().trim();
        if(saturday_subject_name == 'Select Subject'){
            saturday_subject_name = '-'
        }
        if(saturday_teache_name == 'No Teacher Available'){
            saturday_teache_name = '-'
        }
        var slotDict = {};
        slotDict['startAt'] = start_time;
        slotDict['endAt'] = end_time;
        slotDict['subject'] = saturday_subject_id;
        slotDict['teacher'] = saturday_teache_id;
        slotDict['subject_name'] = saturday_subject_name;
        slotDict['teacher_name'] = saturday_teache_name;
        saturday_slot['slot_'+(i+1)+''] = slotDict;
        delete(slotDict);

    }

    console.log('monday_slot >> ',monday_slot);
    console.log('tuesday_slot >>',tuesday_slot);
    console.log('wednesday_slot >>',wednesday_slot);
    console.log('thursday_slot >>',thursday_slot);
    console.log('friday_slot >>',friday_slot);
    console.log('saturday_slot >>',saturday_slot);


    if(branch_flag == true || session_flag == true || year_flag == true || effective_from_flag == true || class_flag == true || section_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("branch_id", branch);
        formdata.append("session", session);
        formdata.append("year_id", year);
        formdata.append("effective_from", effective_from);
        formdata.append("class_id", class_id);
        formdata.append("section_id", section_id);
        formdata.append("monday_slot[]", JSON.stringify(monday_slot));
        formdata.append("tuesday_slot[]", JSON.stringify(tuesday_slot));
        formdata.append("wednesday_slot[]", JSON.stringify(wednesday_slot));
        formdata.append("thursday_slot[]", JSON.stringify(thursday_slot));
        formdata.append("friday_slot[]", JSON.stringify(friday_slot));
        formdata.append("saturday_slot[]", JSON.stringify(saturday_slot));
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-time-table",
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'New time table added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else {
                    alert('An Error occured while adding new time table. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }

}