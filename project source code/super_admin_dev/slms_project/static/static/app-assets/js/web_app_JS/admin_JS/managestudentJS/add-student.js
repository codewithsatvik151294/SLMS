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
var registration_flag = false;
var fname_flag = false;
var dob_flag = false;
var parent_name_flag = false;
var email_flag = false;
var contact_flag = false;
var parent_contact_flag = false;
var pincode_flag = false;
var city_flag = false;
var branch_flag = false;
var classs_flag = false;
var section_flag = false;
var subject_flag = false;
var image_flag = false;

// add new student
function add_new_student() {

    var student_registration_number = $('#student_registration_no').val().trim();
    var student_fname = $('#student_first_name').val().trim();
    var student_lname = $('#student_last_name').val().trim();
    var student_dob = $('#student_dob').val().trim();
    var student_gender = $('#student_gender').val().trim();
    var student_parent_name = $('#student_parent_name').val().trim();
    var student_parent_relation = $('#student_parent_relation').val().trim();
    var student_hobbies = $('#student_hobbies').val();

    var student_email = $('#student_email').val().trim();
    var student_contact = $('#student_contact').val().trim();
    var student_parent_contact = $('#student_parent_contact').val().trim();

    var student_address = $('#student_address').val().trim();
    var branchPinCode = $('#branchPinCode').val().trim();
    var studentCity = $('#studentCity').val().trim();
    var student_state = $('#student_state').val().trim();

    var branchCode = $('#default-select').val().trim();
    var student_class = $('#student_class').val().trim();
    var student_section = $('#student_section').val().trim();
    var student_subject = $('#student_subject').val();

    // field validation
    if (student_registration_number == '') {
        $('#student-registration-error').removeClass('d-none');
        $('#student-registration-error').html('');
        $('#student-registration-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Registration no. required</strong></small>");
        registration_flag = true;
    } else {
        $('#student-registration-error').addClass('d-none');
        registration_flag = false;
    }

    if (student_fname == '') {
        $('#student-first-name-error').removeClass('d-none');
        $('#student-first-name-error').html('');
        $('#student-first-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;First name required</strong></small>");
        fname_flag = true;
    } else {
        $('#student-first-name-error').addClass('d-none');
        fname_flag = false;
    }

    if (student_fname.length < 3) {
        $('#student-first-name-error').removeClass('d-none');
        $('#student-first-name-error').html('');
        $('#student-first-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;First name must be minimum of 4 characters</strong></small>");
        fname_flag = true;
    } else {
        $('#student-first-name-error').addClass('d-none');
        fname_flag = false;
    }

    if (student_dob == '') {
        $('#student-dob-error').removeClass('d-none');
        $('#student-dob-error').html('');
        $('#student-dob-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;student's DOB required</strong></small>");
        dob_flag = true;
    } else {
        $('#student-dob-error').addClass('d-none');
        dob_flag = false;
    }

    if (student_parent_name == '') {
        $('#student-parent-name-error').removeClass('d-none');
        $('#student-parent-name-error').html('');
        $('#student-parent-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;student's parent name required</strong></small>");
        fname_flag = true;
    } else {
        $('#student-parent-name-error').addClass('d-none');
        fname_flag = false;
    }

    if (student_parent_name.length < 3) {
        $('#student-parent-name-error').removeClass('d-none');
        $('#student-parent-name-error').html('');
        $('#student-parent-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Parent name must be minimum of 4 characters</strong></small>");
        fname_flag = true;
    } else {
        $('#student-parent-name-error').addClass('d-none');
        fname_flag = false;
    }

    if (student_email == '') {
        $('#student-email-error').removeClass('d-none');
        $('#student-email-error').html('');
        $('#student-email-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;student's email required</strong></small>");
        email_flag = true;
    } else {
        $('#student-email-error').addClass('d-none');
        email_flag = false;
    }

    if (student_contact == '') {
        $('#student-contact-error').removeClass('d-none');
        if (student_contact.length == 0) {
            $('#student-contact-error').html('');
            $('#student-contact-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;student's contact required</strong></small>");
            contact_flag = true;
        }
    } else {
        if (student_contact.length < 10) {
            $('#student-contact-error').removeClass('d-none');
            $('#student-contact-error').html('');
            $('#student-contact-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Invalid contact</strong></small>');
            contact_flag = true;
        } else {
            $('#student-contact-error').addClass('d-none');
            contact_flag = false;
        }
    }

    if (student_parent_contact == '') {
        $('#student_parent-contact-error').removeClass('d-none');
        if (student_parent_contact.length == 0) {
            $('#student_parent-contact-error').html('');
            $('#student_parent-contact-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;student's contact required</strong></small>");
            parent_contact_flag = true;
        }
    } else {
        if (student_parent_contact.length < 10) {
            $('#student_parent-contact-error').removeClass('d-none');
            $('#student_parent-contact-error').html('');
            $('#student_parent-contact-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Invalid contact</strong></small>');
            parent_contact_flag = true;
        } else {
            $('#student_parent-contact-error').addClass('d-none');
            parent_contact_flag = false;
        }
    }

    if (branchPinCode == '') {
        $('#student-pincode-error').removeClass('d-none');
        $('#student-pincode-error').html('');
        $('#student-pincode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Pincode required</strong></small>');
        pincode_flag = true;
    } else {
        $('#student-pincode-error').addClass('d-none');
        pincode_flag = false;
    }

    if (studentCity == '') {
        $('#student-city-error').removeClass('d-none');
        $('#student-city-error').html('');
        $('#student-city-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;City is required</strong></small>');
        city_flag = true;
    } else {
        $('#student-city-error').addClass('d-none');
        city_flag = false;
    }

    if (branchCode == '') {
        $('#student-branchcode-error').removeClass('d-none');
        $('#student-branchcode-error').html('');
        $('#student-branchcode-error').append("<small><strong> &nbsp;&nbsp;&nbsp;student's branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#student-branchcode-error').addClass('d-none');
        $('#student-branchcode-error').html('');
        branch_flag = false;
    }

    if (student_class == '') {
        $('#student-class-error').removeClass('d-none');
        $('#student-class-error').html('');
        $('#student-class-error').append("<small><strong> &nbsp;&nbsp;&nbsp;student's class is required</strong></small>");
        classs_flag = true;
    } else {
        $('#student-class-error').addClass('d-none');
        $('#student-class-error').html('');
        classs_flag = false;
    }

    if (student_section == '') {
        $('#student-section-error').removeClass('d-none');
        $('#student-section-error').html('');
        $('#student-section-error').append("<small><strong> &nbsp;&nbsp;&nbsp;student's section is required</strong></small>");
        classs_flag = true;
    } else {
        $('#student-section-error').addClass('d-none');
        $('#student-section-error').html('');
        classs_flag = false;
    }

    if (student_subject.length == 0) {
        $('#student-subject-error').removeClass('d-none');
        $('#student-subject-error').html('');
        $('#student-subject-error').append("<small><strong> &nbsp;&nbsp;&nbsp;student's subject is required</strong></small>");
        classs_flag = true;
    } else {
        $('#student-subject-error').addClass('d-none');
        $('#student-subject-error').html('');
        classs_flag = false;
    }


    let myFileimg = document.getElementById('stu_photo').files[0];
    if (typeof myFileimg != 'undefined') {
        $('#student-photo-error').addClass('d-none');
        $('#student-photo-error').html('');
        image_flag = false;
    } else {
        $('#student-photo-error').removeClass('d-none');
        $('#student-photo-error').html('');
        $('#student-photo-error').append("<small><strong> &nbsp;&nbsp;&nbsp;student's image is required</strong></small>");
        image_flag = true;
    }


    if (registration_flag == true || city_flag == true || fname_flag == true || dob_flag == true || parent_name_flag == true || email_flag == true || contact_flag == true || parent_contact_flag == true || pincode_flag == true || branch_flag == true || classs_flag == true || section_flag == true || subject_flag == true || image_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("student_registration_number", student_registration_number);
        formdata.append("student_fname", student_fname);
        formdata.append("student_lname", student_lname);
        formdata.append("student_dob", student_dob);
        formdata.append("student_gender", student_gender);
        formdata.append("student_parent_name", student_parent_name);
        formdata.append("student_parent_relation", student_parent_relation);
        formdata.append("student_hobbies[]", student_hobbies);
        formdata.append("student_email", student_email);
        formdata.append("student_contact", student_contact);
        formdata.append("student_parent_contact", student_parent_contact);
        formdata.append("student_address", student_address);
        formdata.append("branchPinCode", branchPinCode);
        formdata.append("studentCity", studentCity);
        formdata.append("student_state", student_state);
        formdata.append("branchCode", branchCode);
        formdata.append("student_class", student_class);
        formdata.append("student_section", student_section);
        formdata.append("student_subject[]", student_subject);

        let myFileimg = document.getElementById('stu_photo').files[0];
        if (typeof myFileimg != 'undefined') {
            formdata.append('profile_image', myFileimg, myFileimg['name']);
        }
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-student",
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
                        title: 'New student added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'student-list'
                    })
                } else {
                    alert('An Error occured while adding new student. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}




// get class from branch
var class_data = '';
var section_data = '';
var subject_data = '';

// get class from branch
function getClass(thisTxt) {
    if ($(thisTxt).val().trim() != '') {
        Swal.showLoading();

        $.ajax({
            type: 'GET',
            url: "/manage/add-teacher-get-class",
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
                    $('#student_class').html('');
                    $('#student_class').append(class_data);
                    $('#student_class').selectpicker('refresh');
                    $('#student-branchcode-error').html('');
                    $('#student-branchcode-error').addClass('d-none');
                    classs_flag = false;
                } else {
                    $('#student_class').html('');
                    $('#student_class').append(class_data);
                    $('#student_class').selectpicker('refresh');
                    $('#student-branchcode-error').removeClass('d-none');
                    $('#student-branchcode-error').html('');
                    $('#student-branchcode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;No Class available in this branch</strong></small>');
                    classs_flag = true;
                }
            }
        });

    }
}




// get sections and subjects from classID
function get_subject_and_sections(thisTxt) {
    Swal.showLoading();
    console.log('class id >> ',$(thisTxt).val().trim());
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
                $('#student_section').html('');
                $('#student_section').append(section_data);
                $('#student_section').selectpicker('refresh');

                for (var i = 0; i < response['subjectList'].length; i++) {
                    var dataStr = '<option value="' + response['subjectList'][i]['id'] + '" selected>' + response['subjectList'][i]['subject_name'] + '</option>';
                    subject_data = subject_data + dataStr;
                }
                $('#student_subject').html('');
                $('#student_subject').append(subject_data);
                $('#student_subject').selectpicker('refresh');
            }
        }
    });
}