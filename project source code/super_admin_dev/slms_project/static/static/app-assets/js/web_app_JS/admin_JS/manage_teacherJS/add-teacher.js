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

// global flags for field validation
var name_flag = false;
var dob_flag = false;
var email_flag = false;
var contact_flag = false;
var pincode_flag = false;
var branch_flag = false;
var classTeacher_class_flag = false;
var classTeacher_section_flag = false;
var noClass_flag = false;

var row_class_flag = false;
var row_section_flag = false;
var row_subject_flag = false;


// add new teacher
function add_new_teacher() {

    var teacher_name = $('#teacher_name').val().trim();
    var teacher_dob = $('#teacher_dob').val().trim();
    var teacher_gender = $('#teacher_gender').val().trim();
    var teacher_fathers_name = $('#teacher_fathers_name').val().trim();
    var teacher_email = $('#teacher_email').val().trim();
    var teacher_contact = $('#teacher_contact').val().trim();
    var teacher_address = $('#teacher_address').val().trim();
    var branchPinCode = $('#branchPinCode').val().trim();
    var teacherCity = $('#teacherCity').val().trim();
    var teacher_state = $('#teacher_state').val().trim();
    var branchCode = $('#default-select').val().trim();

    var isClassTeacher = false;
    var classTeacherID = '';
    var classTeacherSectionID = '';

    // field validation
    if (teacher_name == '') {
        $('#teacher-name-error').removeClass('d-none');
        $('#teacher-name-error').html('');
        $('#teacher-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Teacher's name required</strong></small>");
        name_flag = true;
    } else {
        $('#teacher-name-error').addClass('d-none');
        name_flag = false;
    }

    if (teacher_name.length < 3) {
        $('#teacher-name-error').removeClass('d-none');
        $('#teacher-name-error').html('');
        $('#teacher-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Teacher's name must be of minimum 4 characters</strong></small>");
        name_flag = true;
    } else {
        $('#teacher-name-error').addClass('d-none');
        name_flag = false;
    }

    if (teacher_dob == '') {
        $('#teacher-dob-error').removeClass('d-none');
        $('#teacher-dob-error').html('');
        $('#teacher-dob-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Teacher's DOB required</strong></small>");
        dob_flag = true;
    } else {
        $('#teacher-dob-error').addClass('d-none');
        dob_flag = false;
    }

    if (teacher_email == '') {
        $('#teacher-email-error').removeClass('d-none');
        $('#teacher-email-error').html('');
        $('#teacher-email-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Teacher's email required</strong></small>");
        email_flag = true;
    } else {
        $('#teacher-email-error').addClass('d-none');
        email_flag = false;
    }

    if (teacher_contact == '') {
        $('#teacher-contact-error').removeClass('d-none');
        if (teacher_contact.length == 0) {
            $('#teacher-contact-error').html('');
            $('#teacher-contact-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Teacher's contact required</strong></small>");
            contact_flag = true;
        }
    } else {
        if (teacher_contact.length < 10) {
            $('#teacher-contact-error').removeClass('d-none');
            $('#teacher-contact-error').html('');
            $('#teacher-contact-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Invalid contact</strong></small>');
            contact_flag = true;
        } else {
            $('#teacher-contact-error').addClass('d-none');
            contact_flag = false;
        }
    }

    if (branchPinCode == '') {
        $('#teacher-pincode-error').removeClass('d-none');
        $('#teacher-pincode-error').html('');
        $('#teacher-pincode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Pincode required</strong></small>');
        pincode_flag = true;
    } else {
        $('#teacher-pincode-error').addClass('d-none');
        pincode_flag = false;
    }

    if (branchCode == '') {
        $('#teacher-branchcode-error').removeClass('d-none');
        $('#teacher-branchcode-error').html('');
        $('#teacher-branchcode-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Teacher's branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#teacher-branchcode-error').addClass('d-none');
        $('#teacher-branchcode-error').html('');
        branch_flag = false;
    }


    if ($('#classTeacherCheck').prop("checked") == true) {
        isClassTeacher = true;
        if ($('#classTeacher_class').val().trim() == '') {
            $('#teacher-classTeacher_class-error').removeClass('d-none');
            classTeacherID = '';
            classTeacher_class_flag = true;
        } else {
            $('#teacher-classTeacher_class-error').addClass('d-none');
            classTeacherID = $('#classTeacher_class').val().trim();
            classTeacher_class_flag = false;
        }
        if ($('#classTeacher_section').val().trim() == '') {
            $('#teacher-classTeacher_section-error').removeClass('d-none');
            classTeacherSectionID = '';
            classTeacher_section_flag = true;
        } else {
            $('#teacher-classTeacher_section-error').addClass('d-none');
            classTeacherSectionID = $('#classTeacher_section').val().trim();
            classTeacher_section_flag = false;
        }
    }else{
        isClassTeacher = false;
        classTeacher_class_flag = false;
        classTeacher_section_flag = false;

    }

    var classArray = [];
    var sectionArray = [];
    var subjectArray = [];

    $('.row-class').each(function () { 
        classArray.push($(this).val());
        if($(this).val().trim() == ''){
            $(this).css('border','1px solid red');
            row_class_flag = true;
        }else{
            $(this).css('border','');
            row_class_flag = false;
        }
    });
    console.log(classArray);

    $('.row-section').each(function () { 
        sectionArray.push($(this).val());
        if($(this).val().trim() == ''){
            $(this).css('border','1px solid red');
            row_section_flag = true;
        }else{
            $(this).css('border','');
            row_section_flag = false;
        } 
    });
    console.log(sectionArray);

    $('.row-subject').each(function () { 
        subjectArray.push($(this).val()); 
        if($(this).val().trim() == ''){
            $(this).css('border','1px solid red');
            row_subject_flag = true;
        }else{
            $(this).css('border','');
            row_subject_flag = false;
        }
    });

    if (name_flag == true || dob_flag == true || email_flag == true || contact_flag == true || pincode_flag == true || branch_flag == true || classTeacher_class_flag == true || classTeacher_section_flag == true || noClass_flag == true || row_class_flag == true || row_section_flag == true || row_subject_flag == true) {
        // if(noClass_flag == true){
        //     $('.row-section-data').addClass('d-none');
        //     $('#teacher-branchcode-error').removeClass('d-none');
        //     $('#teacher-branchcode-error').html('');
        //     $('#teacher-branchcode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class available in this branch</strong></small>');
        // }else{
        //     $('.row-section-data').removeClass('d-none');
        //     $('#teacher-branchcode-error').addClass('d-none');
        //     $('#teacher-branchcode-error').html('');
        // }
        return false;
    }else{
        console.log('teacher_name >>> ',teacher_name);
        console.log('teacher_dob >>> ',teacher_dob);
        console.log('teacher_gender >>> ',teacher_gender);
        console.log('teacher_fathers_name >>> ',teacher_fathers_name);
        console.log('teacher_email >>> ',teacher_email);
        console.log('teacher_contact >>> ',teacher_contact);
        console.log('teacher_address >>> ',teacher_address);
        console.log('branchPinCode >>> ',branchPinCode);
        console.log('teacherCity >>> ',teacherCity);
        console.log('teacher_state >>> ',teacher_state);
        console.log('branchCode >>> ',branchCode);
        console.log('classArray >>> ',classArray);
        console.log('sectionArray >>> ',sectionArray);
        console.log('subjectArray >>> ',subjectArray);

        console.log('isClassTeacher >>> ',isClassTeacher);
        console.log('classTeacherID >>> ',classTeacherID);
        console.log('classTeacherSectionID >>> ',classTeacherSectionID);



        if ($('#classTeacherCheck').prop("checked") == true) {
            if(classArray.includes(classTeacherID)){
                $('#teacher-classTeacher_class-error').addClass('d-none');
                $('#teacher-classTeacher_class-error').html('');
                $('#teacher-classTeacher_class-error').append('<small><strong>Class is required for class teacher</strong></small>');
                classTeacher_class_flag = false;
            }else{
                $('#teacher-classTeacher_class-error').removeClass('d-none');
                $('#teacher-classTeacher_class-error').html('');
                $('#teacher-classTeacher_class-error').append('<small><strong>Class not available in selected classes</strong></small>');
                classTeacher_class_flag = true;
            }
    
            if(sectionArray.includes(classTeacherSectionID)){
                $('#teacher-classTeacher_section-error').addClass('d-none');
                $('#teacher-classTeacher_section-error').html('');
                $('#teacher-classTeacher_section-error').append('<small><strong>Section is required for class teacher</strong></small>');
                classTeacher_section_flag = false;
            }else{
                $('#teacher-classTeacher_section-error').removeClass('d-none');
                $('#teacher-classTeacher_section-error').html('');
                $('#teacher-classTeacher_section-error').append('<small><strong>Section not available in selected sections</strong></small>');
                classTeacher_section_flag = true;
            }
        }else{
            isClassTeacher = false;
            classTeacher_class_flag = false;
            classTeacher_section_flag = false;
    
        }


        

        if(classTeacher_class_flag == true || classTeacher_section_flag == true){
            return false;
        }else{
            var formdata = new FormData();
            formdata.append("teacher_name", teacher_name);
            formdata.append("teacher_dob", teacher_dob);
            formdata.append("teacher_gender", teacher_gender);
            formdata.append("teacher_fathers_name", teacher_fathers_name);
            formdata.append("teacher_email", teacher_email);
            formdata.append("teacher_contact", teacher_contact);
            formdata.append("teacher_address", teacher_address);
            formdata.append("branchPinCode", branchPinCode);
            formdata.append("teacherCity", teacherCity);
            formdata.append("teacher_state", teacher_state);
            formdata.append("branchCode", branchCode);
            formdata.append("classArray[]", classArray);
            formdata.append("sectionArray[]", sectionArray);
            formdata.append("subjectArray[]", subjectArray);
            formdata.append("isClassTeacher", isClassTeacher);
            formdata.append("classTeacherID", classTeacherID);
            formdata.append("classTeacherSectionID", classTeacherSectionID);

        
            let myFileimg = document.getElementById('stu_photo').files[0];
            if (typeof myFileimg != 'undefined') {
                formdata.append('profile_image', myFileimg, myFileimg['name']);
            }
            // ---------------  AJAX CALL  ----------------------------
            Swal.showLoading();
            const csrftoken = getCookie('csrftoken');
            $.ajax({
                type: 'POST',
                url: "add-teacher",
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
                            title: 'New teacher added successfully.',
                            showConfirmButton: false,
                            timer: 2000
                        }).then(function () {
                            window.location.href = 'teacher-list'
                        })
                    }else if(response['message'] == 'Class teacher already exist'){
                        Swal.fire({
                            icon: 'error',
                            title: 'Class teacher for selected class and section already exist.',
                            showConfirmButton: false,
                            timer: 3000
                        }).then(function () {
                            $('#classTeacher_class').css('border','2px solid red');
                            $('#classTeacher_section').css('border','2px solid red');
                        })
                    }else{
                        alert('An Error occured while adding new teacher. Please try again!');
                        return false;
                    }
                }
            });
            // --------------------------------------------------------
        }

    }

}


var class_data = '';
var section_data = '';
var subject_data = '';

// get class from branch
function getBranch(thisTxt) {
    if ($(thisTxt).val().trim() != '') {
        Swal.showLoading();

        $.ajax({
            type: 'GET',
            url: "add-teacher-get-class",
            data: { 'branchID': $(thisTxt).val().trim() },
            success: function (response) {
                Swal.close();
                console.log(response);
                class_data = '';
                class_data = "<option class='d-none' value=''>Select Class </option>";
                if (response['classList'].length > 0) {
                    for (var i = 0; i < response['classList'].length; i++) {
                        var dataStr = '<option value="' + response['classList'][i]['id'] + '">' + response['classList'][i]['class_name'] + '</option>';
                        class_data = class_data + dataStr;
                    }
                    $('#row_1_class').html('');
                    $('#row_1_class').append(class_data);

                    $('#classTeacher_class').html('');
                    $('#classTeacher_class').append(class_data);

                    $('#teacher-branchcode-error').addClass('d-none');
                    $('#teacher-branchcode-error').html('');
                    $('.row-section-data').removeClass('d-none');
                    $('.row-section-data1').html('');
                    noClass_flag = false;
                } else {
                    $('#classTeacher_class').html('');
                    $('#classTeacher_class').append(class_data);

                    $('.row-section-data').addClass('d-none');
                    $('#teacher-branchcode-error').removeClass('d-none');
                    $('#teacher-branchcode-error').html('');
                    $('#teacher-branchcode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class available in this branch</strong></small>');
                    $('.row-section-data1').html('');
                    noClass_flag = true;
                }
            }
        });

    } else {
        $('.row-section-data').addClass('d-none');
    }
}



// add class to teacher
var counter = 2;
$('.add-class').click(function () {
    $("#more-classes").append('<div class=row><div class="pt-1 col-md-3 form-group"><select class="form-control row-class" id="row_' + counter + '_class"  onchange="get_subject_and_sections(this)">' + class_data + '</select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-section" id="row_' + counter + '_section">' + section_data + '</select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-subject" id="row_' + counter + '_subject">' + subject_data + '</select></div><div class="pt-1 col-lg-3 text-right"><a style="margin-top:5px" class="btn btn-danger remove-class  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a> </div></div>');
    counter = counter + 1;
});

$(document).on('click', '.remove-class', function () {
    $(this).parent().parent().remove();
    counter = counter - 1;
});



// get subjects and sections of selected class
function get_subject_and_sections(thisTxt) {
    var classId = $(thisTxt).val().trim();
    var currentCounter = $(thisTxt).attr('id').split('_')
    console.log('classId >>> ', classId);
    console.log('currentCounter >>> ', currentCounter[1]);

    Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "get-subject-and-section",
        data: { 'classID': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            console.log(response);
            section_data = '';
            section_data = "<option class='d-none' value=''>Select Section </option>";
            subject_data = '';
            subject_data = "<option class='d-none' value=''>Select Subject </option>";
            if (response['sectionList'].length > 0) {
                for (var i = 0; i < response['sectionList'].length; i++) {
                    var dataStr = '<option value="' + response['sectionList'][i]['id'] + '">' + response['sectionList'][i]['section_name'] + '</option>';
                    section_data = section_data + dataStr;
                }
                $('#row_'+currentCounter[1]+'_section').html('');
                $('#row_'+currentCounter[1]+'_section').append(section_data);

                for (var i = 0; i < response['subjectList'].length; i++) {
                    var dataStr = '<option value="' + response['subjectList'][i]['id'] + '">' + response['subjectList'][i]['subject_name'] + '</option>';
                    subject_data = subject_data + dataStr;
                }
                $('#row_'+currentCounter[1]+'_subject').html('');
                $('#row_'+currentCounter[1]+'_subject').append(subject_data);
            }
        }
    });
}



// get subjects and sections of selected class
function get_subject_and_sections_class_teacher(thisTxt) {
    var classId = $(thisTxt).val().trim();
    var currentCounter = $(thisTxt).attr('id').split('_')
    console.log('classId >>> ', classId);
    console.log('currentCounter >>> ', currentCounter[1]);

    Swal.showLoading();
    $.ajax({
        type: 'GET',
        url: "get-subject-and-section",
        data: { 'classID': $(thisTxt).val().trim() },
        success: function (response) {
            Swal.close();
            console.log(response);
            section_data = '';
            section_data = "<option class='d-none' value=''>Select Section </option>";
            if (response['sectionList'].length > 0) {
                for (var i = 0; i < response['sectionList'].length; i++) {
                    var dataStr = '<option value="' + response['sectionList'][i]['id'] + '">' + response['sectionList'][i]['section_name'] + '</option>';
                    section_data = section_data + dataStr;
                }
                $('#classTeacher_section').html('');
                $('#classTeacher_section').append(section_data);
            }
        }
    });
}