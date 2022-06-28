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
var exam_name_exist_flag = false;
var exam_type_flag = false;
var classID_flag = false;
var branchID_flag = false;

var paper_start_flag = false;
var paper_end_flag = false;
var paper_proctor_flag = false;



// global variables
var exam_name = '';
var exam_type = '';
var branchID = '';
var classID = '';
var negative_marking_allowed = 0;

var papers_array = [];
var selected_question_array = [];

// navigate_to_page_1
function navigate_to_page_1() {
    $('#create-div-section-2').addClass('d-none');
    $('#create-div-section-3').addClass('d-none');
    $('#create-div-section-1').removeClass('d-none');

}


// navigate_to_page_2
function navigate_to_page_2() {
    if (selected_question_array.length == 0) {
        exam_name = $('#exam_unique_name').val().trim();
        exam_type = $('#exam_type').val().trim();
        branchID = $('#branch-id').val().trim();
        classID = $('#class-id').val().trim();
        negative_marking_allowed = $('#negative-marking').val().trim();

        if (exam_name == '') {
            $('#exam-name-error').removeClass('d-none');
            $('#exam-name-error').html('');
            $('#exam-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Exam name is required</strong></small>");
            exam_name_exist_flag = true;
        } else {
            $('#exam-name-error').addClass('d-none');
            exam_name_exist_flag = false;
        }

        if (exam_type == '') {
            $('#exam-type-error').removeClass('d-none');
            $('#exam-type-error').html('');
            $('#exam-type-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Exam type is required</strong></small>");
            exam_type_flag = true;
        } else {
            $('#exam-type-error').addClass('d-none');
            exam_type_flag = false;
        }

        // if (branchID == '') {
        //     $('#exam-branch-error').removeClass('d-none');
        //     $('#exam-branch-error').html('');
        //     $('#exam-branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
        //     branchID_flag = true;
        // } else {
        //     $('#exam-branch-error').addClass('d-none');
        //     branchID_flag = false;
        // }

        if (classID == '') {
            $('#exam-class-error').removeClass('d-none');
            $('#exam-class-error').html('');
            $('#exam-class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Exam class is required</strong></small>");
            classID_flag = true;
        } else {
            $('#exam-class-error').addClass('d-none');
            classID_flag = false;
        }

        if (exam_name_exist_flag == true || exam_type_flag == true || branchID_flag == true || classID_flag == true) {
            return false;
        } else {
            // =================== ajax call ===========================
            $.ajax({
                type: 'GET',
                url: "/exam-management/get-exam-papers",
                data: { 'classID': classID },
                success: function (response) {
                    console.log(response);
                    var dataStr = '';
                    papers_array = response['paperList'];
                    if (response['paperList'].length > 0) {
                        for (var i = 0; i < response['paperList'].length; i++) {
                            var data = '<tr>\
                                            <td>'+ response['paperList'][i]['paper_id'] + '</td>\
                                            <td>'+ response['paperList'][i]['paper_name'] + '</td>\
                                            <td>'+ response['paperList'][i]['subject'] + ' </td>\
                                            <td>'+ response['paperList'][i]['year'] + '</td>\
                                            <td>'+ response['paperList'][i]['total_marks'] + '</td>\
                                            <td class="text-center">\
                                                <a id="paper-'+ response['paperList'][i]['id'] + '" paperID="' + response['paperList'][i]['id'] + '" class="addP text-white" onclick="add_to_selected(' + response['paperList'][i]['id'] + ',this)"> + Select</a>\
                                            </td>\
                                        </tr>';
                            dataStr = dataStr + data;
                        }
                    }
                    var table_data = '<thead>\
                                        <tr>\
                                            <th>Paper ID  </th>\
                                            <th>Paper Name</th>\
                                            <th>Subject</th>\
                                            <th>Year</th>\
                                            <th>Total Marks </th>\
                                            <th width="150" class="text-center">Select </th>\
                                        </tr>\
                                        </thead>\
                                        <tbody>'+ dataStr + '</tbody>';

                    $('#example').DataTable().destroy();
                    $('#example').html('');
                    $('#example').append(table_data);
                    $('#example').DataTable({
                        searching: true,
                        paging: true
                    });

                    var table_data2 = '<thead>\
                            <tr>\
                                <th>Paper ID  </th>\
                                <th>Paper Name</th>\
                                <th>Subject</th>\
                                <th>Year</th>\
                                <th>Total Marks </th>\
                                <th width="150" class="text-center">Remove </th>\
                            </tr>\
                            </thead>\
                            <tbody></tbody>';

                    $('#example2').DataTable().destroy();
                    $('#example2').html('');
                    $('#example2').append(table_data2);
                    $('#example2').DataTable({
                        searching: false,
                        paging: false
                    });
                }
            });
            // =========================================================
            $('#create-div-section-1').addClass('d-none');
            $('#create-div-section-3').addClass('d-none');
            $('#create-div-section-2').removeClass('d-none');
        }
    } else {
        $('#create-div-section-1').addClass('d-none');
        $('#create-div-section-3').addClass('d-none');
        $('#create-div-section-2').removeClass('d-none');
    }

}


// add questions to the selected table
function add_to_selected(paper_id, thisTxt) {
    console.log('papers_array >>> ', papers_array);
    console.log('papers_array >>> ', paper_id, typeof (paper_id));

    if (selected_question_array.includes(paper_id)) {
        console.log('already exist');
    } else {
        selected_question_array.push(paper_id);
        var dataStr = '';

        for (var i = 0; i < papers_array.length; i++) {
            for (var j = 0; j < selected_question_array.length; j++) {
                if (parseInt(papers_array[i]['id']) == parseInt(selected_question_array[j])) {
                    var data = '<tr >\
                                    <td>'+ papers_array[i]['paper_id'] + '</td>\
                                    <td>'+ papers_array[i]['paper_name'] + '</td>\
                                    <td>'+ papers_array[i]['subject'] + ' </td>\
                                    <td>'+ papers_array[i]['year'] + '</td>\
                                    <td>'+ papers_array[i]['total_marks'] + '</td>\
                                    <td class="text-center">\
                                        <a paperID="'+ papers_array[i]['id'] + '" class="delR" onclick="remove_paper(' + papers_array[i]['id'] + ',this)" style="font-size:20px;color:red;"> <i class="fa fa-trash"></i></a>\
                                    </td>\
                                </tr>';
                    dataStr = dataStr + data;
                }
            }
        }
        var table_data = '<thead>\
                            <tr>\
                                <th>Paper ID  </th>\
                                <th>Paper Name</th>\
                                <th>Subject</th>\
                                <th>Year</th>\
                                <th>Total Marks </th>\
                                <th width="150" class="text-center">Remove </th>\
                            </tr>\
                            </thead>\
                            <tbody>'+ dataStr + '</tbody>';

        $('#example2').DataTable().destroy();
        $('#example2').html('');
        $('#example2').append(table_data);
        $('#example2').DataTable({
            searching: false,
            paging: false
        });

        $('#paper-' + paper_id + '').addClass('selected');
        $('#paper-' + paper_id + '').html('<i class="fa fa-check"></i> Selected');

        // $(thisTxt).css('background', '#93db66');
        // $(thisTxt).html('');
        // $(thisTxt).append('<i class="fa fa-check"></i> Selected');
        // $(thisTxt).css('color', 'white');
    }
    console.log('selected_question_array >>> ', selected_question_array);


}

var exam_data = [];
// navigate_to_page_3
function navigate_to_page_3() {
    exam_data = [];
    if (selected_question_array.length == 0) {
        alert('Select atleast 1 paper to continue!');
        return false;
    } else {
        var teacherStr = '';
        Swal.showLoading();
        $.ajax({
            type: 'GET',
            url: "/exam-management/fetch-teachers",
            data: { 'branchID': branchID.trim() },
            success: function (response) {
                Swal.close();
                console.log(response['teacherList']);
                if(response['teacherList'].length == 0){
                    teacherStr = '<option value="" class="d-none">No Proctor Available for this branch</option>';
                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                }else{
                    teacherStr = '<option value="" class="d-none">Select Proctor</option>';
                    for(var i=0;i<response['teacherList'].length;i++){
                        var data = '<option value="'+response['teacherList'][i]['id']+'">'+response['teacherList'][i]['teacher_name']+'</option>';
                        teacherStr = teacherStr + data;
                    }
                    $('#submit_btn').css('pointer-events', '');
                    $('#submit_btn').css('opacity', '1');
                }
            }
        }).then(function(){
            var dataStr = '';
            for (var i = 0; i < papers_array.length; i++) {
                for (var j = 0; j < selected_question_array.length; j++) {
                    if (parseInt(papers_array[i]['id']) == parseInt(selected_question_array[j])) {
                        var data = '<tr>\
                                            <td>'+ papers_array[i]['paper_id'] + '</td>\
                                            <td>'+ papers_array[i]['paper_name'] + '</td>\
                                            <td>'+ papers_array[i]['subject'] + ' </td>\
                                            <td>'+ papers_array[i]['year'] + '</td>\
                                            <td>'+ papers_array[i]['total_marks'] + '</td>\
                                            <td class="text-center">\
                                                <a class="delR" onclick="remove_paper('+ papers_array[i]['id'] + ',this)" style="font-size:20px;color:red;"> <i class="fa fa-trash"></i></a>\
                                            </td>\
                                        </tr>';
    
                        var data = '<tr >\
                                        <td>'+ papers_array[i]['paper_name'] + '</td>\
                                        <td>'+ papers_array[i]['subject'] + ' </td>\
                                        <td>'+ papers_array[i]['year'] + '</td>\
                                        <td><input type="datetime-local" id="start_'+papers_array[i]['id']+'" onchange="check_exam_date_time('+papers_array[i]['id']+',this)" class=" form-control"  onkeypress="return /[]/i.test(event.key)" onkeydown="no_backspaces(event);" placeholder="Select date" name=""></td>\
                                        <td><input type="datetime-local" id="end_'+papers_array[i]['id']+'" onchange="check_exam_date_time('+papers_array[i]['id']+',this)" class=" form-control" placeholder="Select time"  name=""></td>\
                                        <td class="text-center">\
                                        <select id="proctor_'+papers_array[i]['id']+'">'+teacherStr+'</select>\
                                        </td>\
                                    </tr>';
                        dataStr = dataStr + data;
                        var context = {};
                        context['paper_id'] = papers_array[i]['id'];
                        context['paper_start_date_time'] = '';
                        context['paper_end_date_time'] = '';
                        context['paper_proctor_id'] = '';
                        exam_data.push(context);
                    }
                }
            }
            var table_data = '<thead>\
                                <tr>\
                                    <th>Paper ID</th>\
                                    <th>Subject</th>\
                                    <th>Year</th>\
                                    <th>Start Date-Time </th>\
                                    <th>End Date-Time </th>\
                                    <th width="150" class="text-center">Proctor </th>\
                                </tr>\
                            </thead>\
                            <tbody>'+ dataStr + '</tbody>';
    
            $('#example3').DataTable().destroy();
            $('#example3').html('');
            $('#example3').append(table_data);
            $('#example3').DataTable({
                searching: false,
                paging: false
            });
    
            $('#create-div-section-1').addClass('d-none');
            $('#create-div-section-2').addClass('d-none');
            $('#create-div-section-3').removeClass('d-none');
    
            $('#exam-3-name').html('');
            $('#exam-3-name').append(exam_name);
    
            $('#exam-3-total-paper').html('');
            $('#exam-3-total-paper').append(selected_question_array.length);

            console.log('exam_data >>>> ',exam_data);
        });
    }

}

// validate startdate-time and end date-time
function check_exam_date_time(paper_id,thisTxt){
    console.log('start >> ',$('#start_'+paper_id+'').val());
    console.log('end >> ',$('#end_'+paper_id+'').val());


    var date1 = new Date($('#start_'+paper_id+'').val());
    var date2 = new Date($('#end_'+paper_id+'').val());

    console.log('date1 >> ',date1);
    console.log('date2 >> ',date2);

    if($('#start_'+paper_id+'').val() != '' && $('#end_'+paper_id+'').val()){
        if(date1.getTime() === date2.getTime()){
            alert('Start and End date-time cannot be same!');
            $('#start_'+paper_id+'').css('border','2px solid red');
            $('#end_'+paper_id+'').css('border','2px solid red');
        }else{
            $('#start_'+paper_id+'').css('border','');
            $('#end_'+paper_id+'').css('border','');
        }
        
        if(date1.getTime() > date2.getTime()){
            alert('Start date-time cannot be End date-time!');
            $('#start_'+paper_id+'').css('border','2px solid red');
            $('#end_'+paper_id+'').css('border','2px solid red');
        }else{
            $('#start_'+paper_id+'').css('border','');
            $('#end_'+paper_id+'').css('border','');
        }
    
        // if(date1.getTime() < date2.getTime()){
        //     console.log('date 1 is smaller than date 2');
        // }else{
        //     $('#start_'+paper_id+'').css('border','');
        //     $('#end_'+paper_id+'').css('border','');
        // }
    }

}


// get class from branchID
var subject_data = '';
function get_class(thisTxt) {
    Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "/exam-management/fetch-class",
        data: { 'branchID': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            console.log(response['classList']);
            if(response['classList'].length == 0){
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">No Class Available for this branch</option>'+classStr);
                $('#exam-class-error').removeClass('d-none');
                $('#exam-class-error').html('');
                $('#exam-class-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class Available for this branch</strong></small>');
                $('#next_btn_1').css('pointer-events', 'none');
                $('#next_btn_1').css('opacity', '0.2');
            }else{
                var classStr = '';
                for(var i=0;i<response['classList'].length;i++){
                    var data = '<option value="'+response['classList'][i]['id']+'">'+response['classList'][i]['class_name']+'</option>';
                    classStr = classStr + data;
                }
                $('#exam-branch-error').addClass('d-none');
                $('#class-id').html('');
                $('#class-id').append('<option value="" class="d-none">Select Class</option>'+classStr);
                $('#exam-class-error').removeClass('d-none');
                $('#exam-class-error').html('');
                $('#next_btn_1').css('pointer-events', '');
                $('#next_btn_1').css('opacity', '1');
            }
        }
    });
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
                $('#default-select').html('');
                $('#default-select').append(subject_data);
                $('#default-select').trigger('change');
            }


            var table_data2 = '<thead>\
                            <tr>\
                                <th>Paper ID  </th>\
                                <th>Paper Name</th>\
                                <th>Subject</th>\
                                <th>Year</th>\
                                <th>Total Marks </th>\
                                <th width="150" class="text-center">Remove </th>\
                            </tr>\
                            </thead>\
                            <tbody></tbody>';

            $('#example2').DataTable().destroy();
            $('#example2').html('');
            $('#example2').append(table_data2);
            $('#example2').DataTable({
                searching: false,
                paging: false
            });


            var table_data = '<thead>\
                            <tr>\
                                <th>Paper ID  </th>\
                                <th>Paper Name</th>\
                                <th>Subject</th>\
                                <th>Year</th>\
                                <th>Total Marks </th>\
                                <th width="150" class="text-center">Select </th>\
                            </tr>\
                            </thead>\
                            <tbody></tbody>';

            $('#example').DataTable().destroy();
            $('#example').html('');
            $('#example').append(table_data);
            $('#example').DataTable({
                searching: false,
                paging: false
            });

            selected_question_array = [];
        }
    });
}



function check_exam_name(thisTxt) {
    $.ajax({
        type: 'GET',
        url: "/exam-management/check-exam",
        data: { 'search_string': $(thisTxt).val().trim() },
        success: function (response) {
            if (response['message'] == 'exist') {
                $('#exam-name-error').removeClass('d-none');
                $('#exam-name-error').html('');
                $('#exam-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Exam name already exist</strong></small>");
                exam_name_exist_flag = true;
            } else {
                $('#exam-name-error').addClass('d-none');
                exam_name_exist_flag = false;
            }

            // button enabled/disable
            if (exam_name_exist_flag == true) {
                $('#next_btn_1').css('pointer-events', 'none');
                $('#next_btn_1').css('opacity', '0.2');
            } else {
                $('#next_btn_1').css('pointer-events', '');
                $('#next_btn_1').css('opacity', '1');
            }
        }
    });
}



// remove paper from selected list
function remove_paper(paper_id, thisTxt) {
    var index = selected_question_array.indexOf(paper_id);
    if (index > -1) {
        selected_question_array.splice(index, 1);
    }
    var dataStr = '';
    for (var i = 0; i < papers_array.length; i++) {
        for (var j = 0; j < selected_question_array.length; j++) {
            if (parseInt(papers_array[i]['id']) == parseInt(selected_question_array[j])) {
                var data = '<tr>\
                                    <td>'+ papers_array[i]['paper_id'] + '</td>\
                                    <td>'+ papers_array[i]['paper_name'] + '</td>\
                                    <td>'+ papers_array[i]['subject'] + ' </td>\
                                    <td>'+ papers_array[i]['year'] + '</td>\
                                    <td>'+ papers_array[i]['total_marks'] + '</td>\
                                    <td class="text-center">\
                                        <a class="delR" onclick="remove_paper('+ papers_array[i]['id'] + ',this)" style="font-size:20px;color:red;"> <i class="fa fa-trash"></i></a>\
                                    </td>\
                                </tr>';
                dataStr = dataStr + data;
            }
        }
    }
    var table_data = '<thead>\
                            <tr>\
                                <th>Paper ID  </th>\
                                <th>Paper Name</th>\
                                <th>Subject</th>\
                                <th>Year</th>\
                                <th>Total Marks </th>\
                                <th width="150" class="text-center">Remove </th>\
                            </tr>\
                            </thead>\
                            <tbody>'+ dataStr + '</tbody>';

    $('#example2').DataTable().destroy();
    $('#example2').html('');
    $('#example2').append(table_data);
    $('#example2').DataTable({
        searching: false,
        paging: false
    });
    $('#paper-' + paper_id + '').removeClass('selected');
    $('#paper-' + paper_id + '').html('<i class="fa fa-plus"></i> Select');

}



// submit data
function submit_exam_data(){
    for(var i=0;i<exam_data.length;i++){
        var paperID = exam_data[i]['paper_id'];
        if($('#start_'+paperID+'').val() == ''){
            $('#start_'+paperID+'').css('border','2px solid red');
            return false;
        }
        if($('#end_'+paperID+'').val() == ''){
            $('#end_'+paperID+'').css('border','2px solid red');
            return false;
        }
        var date1 = new Date($('#start_'+paperID+'').val());
        var date2 = new Date($('#end_'+paperID+'').val());

        if($('#start_'+paperID+'').val() != '' && $('#end_'+paperID+'').val()){
            if(date1.getTime() === date2.getTime()){
                alert('Start and End date-time cannot be same!');
                $('#start_'+paperID+'').css('border','2px solid red');
                $('#end_'+paperID+'').css('border','2px solid red');
            }else{
                $('#start_'+paperID+'').css('border','');
                $('#end_'+paperID+'').css('border','');
            }
            
            if(date1.getTime() > date2.getTime()){
                alert('Start date-time cannot be End date-time!');
                $('#start_'+paperID+'').css('border','2px solid red');
                $('#end_'+paperID+'').css('border','2px solid red');
            }else{
                $('#start_'+paperID+'').css('border','');
                $('#end_'+paperID+'').css('border','');
            }

            if(date1.getTime() < date2.getTime()){
                exam_data[i]['paper_start_date_time'] = date1;
                exam_data[i]['paper_end_date_time'] = date2;
            }
        }

        if($('#proctor_'+paperID+'').val() == ''){
            $('#proctor_'+paperID+'').css('border','2px solid red');
            return false;
        }else{
            exam_data[i]['paper_proctor_id'] = $('#proctor_'+paperID+'').val();
            $('#proctor_'+paperID+'').css('border','');
        }

    }
    if(paper_start_flag == true || paper_end_flag == true || paper_proctor_flag == true){
        return false;
    }else{
        console.log('exam_data >>> ',exam_data);
        var formdata = new FormData();
        formdata.append("examName", exam_name);
        formdata.append("exam_type", exam_type);
        formdata.append("branchID", branchID);
        formdata.append("classID", classID);
        formdata.append("negative_marking_allowed", negative_marking_allowed);
        formdata.append("exam_data[]", JSON.stringify(exam_data));
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-exam",
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
                        title: 'New exam added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'exam-list';
                    })
                }else if (response['message'] == 'exist') {
                    Swal.fire({
                        icon: 'error',
                        title: 'Exam already exist with this name and seleted parameters!',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else {
                    alert('An Error occured while adding new exam. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}