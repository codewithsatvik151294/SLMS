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

    // $('#tt-table').css('opacity','0.3');
    // $('#tt-add-more').css('opacity','0.3');
    // $('#tt-table').css('pointer-events','none');
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
                // $('#submit_btn').css('pointer-events', 'none');
                // $('#submit_btn').css('opacity', '0.2');
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
                // $('#submit_btn').css('pointer-events', '');
                // $('#submit_btn').css('opacity', '1');
            }
        }
    });
}




// get subjects and sections of selected class
function get_subject_and_sections(thisTxt) {
    // $('#tt-table').css('opacity','0.3');
    // $('#tt-add-more').css('opacity','0.3');
    // $('#tt-table').css('pointer-events','none');
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


// global variables & flags
var branch_id = '';
var year_id = '';
var class_id = '';
var section_id = '';

var branch_flag = false;
var year_flag = false;
var class_flag = false;
var section_flag = false;
// filter students
function get_student(){
    branch_id = $('#branch-id').val().trim();
    year_id = $('#year-id').val().trim();
    class_id = $('#class-id').val().trim();
    section_id = $('#section-id').val().trim();

    // field validation
    if (branch_id == '') {
        $('#branch-error').removeClass('d-none');
        $('#branch-error').html('');
        $('#branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#branch-error').addClass('d-none');
        branch_flag = false;
    }

    if (year_id == '') {
        $('#year-error').removeClass('d-none');
        $('#year-error').html('');
        $('#year-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Year is required</strong></small>");
        year_flag = true;
    } else {
        $('#year-error').addClass('d-none');
        year_flag = false;
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

    if(branch_flag == true || year_flag == true || class_flag == true || section_flag == true){
        return false;
    }else{
        // ---------------  AJAX CALL  ----------------------------
        // Swal.showLoading();
        $.ajax({
            type: 'GET',
            url: "/attendance-management/filter-student",
            data: {"branchId":branch_id,"year_id":year_id,"class_id":class_id,"section_id":section_id},
            success: function (response) {
                // Swal.close();
                console.log('response >>> ',response['response']);
                if(response['response'].length == 0){
                    // daram-text').css('display','');
                    // $('#tt-table').css('display','none');
                    // daram-text').html('');
                    // daram-text').append('No Student Available!');
                    return false;
                }
                else{
                    var dataStr = '';
                    for(var i=0;i<response['response'].length;i++){
                        var data = '<tr>\
                                        <td>'+response['response'][i]['student_reg_no']+'</td>\
                                        <td>'+response['response'][i]['student_name']+'</td>\
                                        <td>'+response['response'][i]['overall_percent']+'</td>\
                                        <td>'+response['response'][i]['total_present']+'</td>\
                                        <td>'+response['response'][i]['total_absent']+'</td>\
                                        <td class="details-control">\
                                            <a href="/attendance-management/view-attendance/'+response['response'][i]['id']+'" class="view"><i class="fa fa-eye"></i></a>\
                                            <a href="/attendance-management/edit-attendance/'+response['response'][i]['id']+'" class="edit "><i class="fa fa-edit"></i></a> </td>\
                                    </tr>';
                                    dataStr = dataStr + data;
                                }
                    // daram-text').css('display','none');
                    // $('#tt-table').css('display','');
                    // $('#tt-table').css('opacity','1');
                    // $('#tt-append-list').html('');
                    // $('#tt-append-list').append(dataStr);


                    var table_data = '<thead>\
                                            <tr>\
                                            <th>Reg. No.</th>\
                                            <th>Student Name</th>\
                                            <th>Overall Attendance (%)</th>\
                                            <th>Total Present </th>\
                                            <th>Total Absent</th>\
                                            <th class="text-center">Action</th>\
                                            </tr>\
                                        </thead>\
                                        <tbody>'+ dataStr + '</tbody>';

                    $('#example2').DataTable().destroy();
                    $('#example2').html('');
                    $('#example2').append(table_data);
                    $('#example2').DataTable({
                        searching: true,
                        paging: true
                    });
                            
                }
            }
        });
        // --------------------------------------------------------
    }
}