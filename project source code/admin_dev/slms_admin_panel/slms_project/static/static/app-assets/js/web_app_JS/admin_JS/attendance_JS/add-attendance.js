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

// global variables & flags
var branch_id = '';
var year_id = '';
var class_id = '';
var section_id = '';

var branch_flag = False;
var year_flag = False;
var class_flag = False;
var section_flag = False;
// filter students
function get_student_for_attendance(){
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
        $.ajax({
            type: 'GET',
            url: "/attendance-management/filter-student",
            data: {"branchId":branch_id,"year_id":year_id,"class_id":class_id,"section_id":section_id},
            success: function (response) {
                console.log('response >>> ',response['response']);
                if(response['response'].length == 0){
                    return false;
                }
                else{
                    var dataStr = '';
                    for(var i=0;i<response['response'].length;i++){
                        var data = '<tr> \
                                        <td>'+(i+1)+'</td>\
                                        <td>'+response['response'][i]['student_name']+'</td>\
                                        <td class="d-none" id="student_'+(i+1)+'">'+response['response'][i]['student_reg_no']+'</td>\
                                        <td>\
                                            <div class="demo-radio-button" id="check_'+(i+1)+'">\
                                            <label> <input name="atten_'+(i+1)+'" id="attendance_present_status_'+(i+1)+'" type="radio"  class="radio-col-success">\
                                                <span>Present </span>\
                                            </label>\
                                            <label class="ml-5">\
                                                <input name="atten_'+(i+1)+'" id="attendance_absent_status_'+(i+1)+'" type="radio"   class="radio-col-danger">\
                                                <span>Absent</span>\
                                            </label>\
                                            </div>\
                                        </td>\
                                    </tr>';
                                    dataStr = dataStr + data;
                                }
                    var table_data = '<thead>\
                                            <tr>\
                                            <th>S. No.</th>\
                                            <th>Student Name</th>\
                                            <th class="d-none">Student Name</th>\
                                            <th width="300"> Perform Action</th>\
                                            </tr>\
                                        </thead>\
                                        <tbody>'+ dataStr + '</tbody>';
                            
                    $('#example2').DataTable().destroy();
                    $('#example2').html('');
                    $('#example2').append(table_data);
                    $('#example2').DataTable({
                        searching: true,
                        paging: true,
                    });
                            
                }
            }
        });
        // --------------------------------------------------------
    }
}


// submit_attendance
function submit_attendance(){
    var attendace_list = [];
    var rowCount = $("tbody tr").length;
    if(rowCount <= 1){
        alert('Select parameters for attendance submission!');
        return;
    }else{
        for(var i=1;i<=rowCount;i++){
            if($('#attendance_present_status_'+(i)+'').is(":checked") == false && $('#attendance_absent_status_'+(i)+'').is(":checked") == false){
                $('#check_'+i+'').css('border','2px solid red');
                return false;
            }else{
                $('#check_'+i+'').css('border','');
            }
            var dataDict = {};
            dataDict['student_reg'] = $('#student_'+(i)+'').text().trim();
            if($('#attendance_present_status_'+(i)+'').is(":checked") == true){
                dataDict['attendance_status'] = '1';
            }
            if($('#attendance_absent_status_'+(i)+'').is(":checked") == true){
                dataDict['attendance_status'] = '2';
            }
            attendace_list.push(dataDict);
        }

        branch_id = $('#branch-id').val().trim();
        year_id = $('#year-id').val().trim();
        class_id = $('#class-id').val().trim();
        section_id = $('#section-id').val().trim();

        var formdata = new FormData();
        formdata.append("branch_id", branch_id);
        formdata.append("year_id", year_id);
        formdata.append("class_id", class_id);
        formdata.append("section_id", section_id);
        formdata.append("attendace_list[]", JSON.stringify(attendace_list));
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "/attendance-management/add-attendance",
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response['response']);
                Swal.close();
                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'Attendance added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else {
                    alert('An Error occured while adding attendance. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}