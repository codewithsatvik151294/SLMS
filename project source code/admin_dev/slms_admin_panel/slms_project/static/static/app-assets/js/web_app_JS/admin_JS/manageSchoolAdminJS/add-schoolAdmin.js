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

var schoolAdmin_name_flag = false;
var schoolAdmin_dob_flag = false;
var schoolAdmin_gender_flag = false;
var schoolAdmin_fathers_name_flag = false;
var schoolAdmin_email_flag = false;
var schoolAdmin_contact_flag = false;
var pincode_flag = false;
var city_flag = false;
var branchCode_flag = false;
var image_flag = false;
var branch_flag = false;
// add new schoolAdmin
function add_new_schoolAdmin(){

    var schoolAdmin_name = $('#schoolAdmin_name').val().trim();
    var schoolAdmin_dob = $('#schoolAdmin_dob').val().trim();
    var schoolAdmin_gender = $('#schoolAdmin_gender').val().trim();
    var schoolAdmin_fathers_name = $('#schoolAdmin_fathers_name').val().trim();
    var schoolAdmin_email = $('#schoolAdmin_email').val().trim();
    var schoolAdmin_contact = $('#schoolAdmin_contact').val().trim();
    var schoolAdmin_address = $('#schoolAdmin_address').val().trim();
    var branchPinCode = $('#branchPinCode').val().trim();
    var schoolAdminCity = $('#schoolAdminCity').val().trim();
    var schoolAdmin_state = $('#schoolAdmin_state').val().trim();
    var branchCode = $('#default-select').val().trim();


    // field validation
    if (schoolAdmin_name == '') {
        $('#schoolAdmin-name-error').removeClass('d-none');
        $('#schoolAdmin-name-error').html('');
        $('#schoolAdmin-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin name is required</strong></small>");
        schoolAdmin_name_flag = true;
    } else {
        $('#schoolAdmin-name-error').addClass('d-none');
        schoolAdmin_name_flag = false;
    }

    if (schoolAdmin_name.length < 3) {
        $('#schoolAdmin-name-error').removeClass('d-none');
        $('#schoolAdmin-name-error').html('');
        $('#schoolAdmin-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin name must me minimum of 4 characters</strong></small>");
        schoolAdmin_name_flag = true;
    } else {
        $('#schoolAdmin-name-error').addClass('d-none');
        schoolAdmin_name_flag = false;
    }

    if (schoolAdmin_dob == '') {
        $('#schoolAdmin-dob-error').removeClass('d-none');
        $('#schoolAdmin-dob-error').html('');
        $('#schoolAdmin-dob-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin DOB is required</strong></small>");
        schoolAdmin_dob_flag = true;
    } else {
        $('#schoolAdmin-dob-error').addClass('d-none');
        schoolAdmin_dob_flag = false;
    }

    if (schoolAdmin_gender == '') {
        $('#schoolAdmin-gender-error').removeClass('d-none');
        $('#schoolAdmin-gender-error').html('');
        $('#schoolAdmin-gender-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin gender is required</strong></small>");
        schoolAdmin_gender_flag = true;
    } else {
        $('#schoolAdmin-gender-error').addClass('d-none');
        schoolAdmin_gender_flag = false;
    }

    if (schoolAdmin_fathers_name == '') {
        $('#schoolAdmin-father-name-error').removeClass('d-none');
        $('#schoolAdmin-father-name-error').html('');
        $('#schoolAdmin-father-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin father's name is required</strong></small>");
        schoolAdmin_fathers_name_flag = true;
    } else {
        $('#schoolAdmin-father-name-error').addClass('d-none');
        schoolAdmin_fathers_name_flag = false;
    }

    if (schoolAdmin_fathers_name.length < 3) {
        $('#schoolAdmin-father-name-error').removeClass('d-none');
        $('#schoolAdmin-father-name-error').html('');
        $('#schoolAdmin-father-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin father's name must me minimum of 4 characters</strong></small>");
        schoolAdmin_fathers_name_flag = true;
    } else {
        $('#schoolAdmin-father-name-error').addClass('d-none');
        schoolAdmin_fathers_name_flag = false;
    }

    if (schoolAdmin_email == '') {
        $('#schoolAdmin-email-error').removeClass('d-none');
        $('#schoolAdmin-email-error').html('');
        $('#schoolAdmin-email-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin email is required</strong></small>");
        schoolAdmin_email_flag = true;
    } else {
        $('#schoolAdmin-email-error').addClass('d-none');
        schoolAdmin_email_flag = false;
    }


    if (schoolAdmin_contact == '') {
        $('#schoolAdmin-contact-error').removeClass('d-none');
        if (schoolAdmin_contact.length == 0) {
            $('#schoolAdmin-contact-error').html('');
            $('#schoolAdmin-contact-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;schoolAdmin contact is required</strong></small>");
            schoolAdmin_contact_flag = true;
        }
    } else {
        if (schoolAdmin_contact.length < 10) {
            $('#schoolAdmin-contact-error').removeClass('d-none');
            $('#schoolAdmin-contact-error').html('');
            $('#schoolAdmin-contact-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Invalid contact</strong></small>');
            schoolAdmin_contact_flag = true;
        } else {
            $('#schoolAdmin-contact-error').addClass('d-none');
            schoolAdmin_contact_flag = false;
        }
    }

    if (branchPinCode == '') {
        $('#schoolAdmin-pincode-error').removeClass('d-none');
        $('#schoolAdmin-pincode-error').html('');
        $('#schoolAdmin-pincode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Pincode is required</strong></small>');
        pincode_flag = true;
    } else {
        $('#schoolAdmin-pincode-error').addClass('d-none');
        pincode_flag = false;
    }

    if (schoolAdminCity == '') {
        $('#schoolAdmin-city-error').removeClass('d-none');
        $('#schoolAdmin-city-error').html('');
        $('#schoolAdmin-city-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;City is required</strong></small>');
        city_flag = true;
    } else {
        $('#schoolAdmin-city-error').addClass('d-none');
        city_flag = false;
    }

    if (branchCode == '') {
        $('#schoolAdmin-branch-error').removeClass('d-none');
        $('#schoolAdmin-branch-error').html('');
        $('#schoolAdmin-branch-error').append("<small><strong> &nbsp;&nbsp;&nbsp;schoolAdmin branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#schoolAdmin-branch-error').addClass('d-none');
        $('#schoolAdmin-branch-error').html('');
        branch_flag = false;
    }

    let img_data = document.getElementById('stu_photo').files[0];
    if (typeof img_data != 'undefined') {
        $('#schoolAdmin-image-error').addClass('d-none');
        $('#schoolAdmin-image-error').html('');
        image_flag = false;
    } else {
        $('#schoolAdmin-image-error').removeClass('d-none');
        $('#schoolAdmin-image-error').html('');
        $('#schoolAdmin-image-error').append("<small><strong> &nbsp;&nbsp;&nbsp;schoolAdmin image is required</strong></small>");
        image_flag = true;
    }

    if(schoolAdmin_name_flag == true || city_flag == true || schoolAdmin_dob_flag == true || schoolAdmin_gender_flag == true || schoolAdmin_fathers_name_flag == true || schoolAdmin_email_flag == true || schoolAdmin_contact_flag == true || pincode_flag == true || branchCode_flag == true || image_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("schoolAdmin_name", schoolAdmin_name);
        formdata.append("schoolAdmin_dob", schoolAdmin_dob);
        formdata.append("schoolAdmin_gender", schoolAdmin_gender);
        formdata.append("schoolAdmin_fathers_name", schoolAdmin_fathers_name);
        formdata.append("schoolAdmin_email", schoolAdmin_email);
        formdata.append("schoolAdmin_contact", schoolAdmin_contact);
        formdata.append("schoolAdmin_address", schoolAdmin_address);
        formdata.append("branchPinCode", branchPinCode);
        formdata.append("schoolAdminCity", schoolAdminCity);
        formdata.append("schoolAdmin_state", schoolAdmin_state);
        formdata.append("branchCode", branchCode);
    
        let myFileimg = document.getElementById('stu_photo').files[0];
        if (typeof myFileimg != 'undefined') {
            formdata.append('profile_image', myFileimg, myFileimg['name']);
        }
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-school-admin",
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
                        title: 'New schoolAdmin added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'school-admin-list'
                    })
                }else{
                    alert('An Error occured while adding new schoolAdmin. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}