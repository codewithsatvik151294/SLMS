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
var principal_name_flag = false;
var principal_dob_flag = false;
var principal_gender_flag = false;
var principal_fathers_name_flag = false;
var principal_email_flag = false;
var principal_contact_flag = false;
var pincode_flag = false;
var city_flag = false;
var branchCode_flag = false;
var image_flag = false;
var branch_flag = false;

// add new principal
function edit_principal(){

    var principal_name = $('#principal_name').val().trim();
    var principal_dob = $('#principal_dob').val().trim();
    var principal_gender = $('#principal_gender').val().trim();
    var principal_fathers_name = $('#principal_fathers_name').val().trim();
    var principal_email = $('#principal_email').val().trim();
    var principal_contact = $('#principal_contact').val().trim();
    var principal_address = $('#principal_address').val().trim();
    var branchPinCode = $('#branchPinCode').val().trim();
    var principalCity = $('#principalCity').val().trim();
    var principal_state = $('#principal_state').val().trim();
    var branchCode = $('#default-select').val();


    // field validation
    if (principal_name == '') {
        $('#principal-name-error').removeClass('d-none');
        $('#principal-name-error').html('');
        $('#principal-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal name is required</strong></small>");
        principal_name_flag = true;
    } else {
        $('#principal-name-error').addClass('d-none');
        principal_name_flag = false;
    }

    if (principal_name.length < 3) {
        $('#principal-name-error').removeClass('d-none');
        $('#principal-name-error').html('');
        $('#principal-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal name must be of minimum 4 characters</strong></small>");
        principal_name_flag = true;
    } else {
        $('#principal-name-error').addClass('d-none');
        principal_name_flag = false;
    }

    if (principal_dob == '') {
        $('#principal-dob-error').removeClass('d-none');
        $('#principal-dob-error').html('');
        $('#principal-dob-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal DOB is required</strong></small>");
        principal_dob_flag = true;
    } else {
        $('#principal-dob-error').addClass('d-none');
        principal_dob_flag = false;
    }

    if (principal_gender == '') {
        $('#principal-gender-error').removeClass('d-none');
        $('#principal-gender-error').html('');
        $('#principal-gender-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal gender is required</strong></small>");
        principal_gender_flag = true;
    } else {
        $('#principal-gender-error').addClass('d-none');
        principal_gender_flag = false;
    }

    if (principal_fathers_name == '') {
        $('#principal-father-name-error').removeClass('d-none');
        $('#principal-father-name-error').html('');
        $('#principal-father-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal father's name is required</strong></small>");
        principal_fathers_name_flag = true;
    } else {
        $('#principal-father-name-error').addClass('d-none');
        principal_fathers_name_flag = false;
    }

    if (principal_fathers_name.length < 3) {
        $('#principal-father-name-error').removeClass('d-none');
        $('#principal-father-name-error').html('');
        $('#principal-father-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal father's name must be of minimum 4 characters</strong></small>");
        principal_fathers_name_flag = true;
    } else {
        $('#principal-father-name-error').addClass('d-none');
        principal_fathers_name_flag = false;
    }

    if (principal_email == '') {
        $('#principal-email-error').removeClass('d-none');
        $('#principal-email-error').html('');
        $('#principal-email-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal email is required</strong></small>");
        principal_email_flag = true;
    } else {
        $('#principal-email-error').addClass('d-none');
        principal_email_flag = false;
    }


    if (principal_contact == '') {
        $('#principal-contact-error').removeClass('d-none');
        if (principal_contact.length == 0) {
            $('#principal-contact-error').html('');
            $('#principal-contact-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Principal contact is required</strong></small>");
            principal_contact_flag = true;
        }
    } else {
        if (principal_contact.length < 10) {
            $('#principal-contact-error').removeClass('d-none');
            $('#principal-contact-error').html('');
            $('#principal-contact-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Invalid contact</strong></small>');
            principal_contact_flag = true;
        } else {
            $('#principal-contact-error').addClass('d-none');
            principal_contact_flag = false;
        }
    }

    if (branchPinCode == '') {
        $('#principal-pincode-error').removeClass('d-none');
        $('#principal-pincode-error').html('');
        $('#principal-pincode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Pincode is required</strong></small>');
        pincode_flag = true;
    } else {
        $('#principal-pincode-error').addClass('d-none');
        pincode_flag = false;
    }

    if (principalCity == '') {
        $('#principal-city-error').removeClass('d-none');
        $('#principal-city-error').html('');
        $('#principal-city-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;City is required</strong></small>');
        city_flag = true;
    } else {
        $('#principal-city-error').addClass('d-none');
        city_flag = false;
    }

    if (branchCode == '') {
        $('#principal-branch-error').removeClass('d-none');
        $('#principal-branch-error').html('');
        $('#principal-branch-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Principal branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#principal-branch-error').addClass('d-none');
        $('#principal-branch-error').html('');
        branch_flag = false;
    }

    let img_data = document.getElementById('stu_photo').files[0];
    if (typeof img_data != 'undefined') {
        $('#principal-image-error').addClass('d-none');
        $('#principal-image-error').html('');
        image_flag = false;
    } else {
        $('#principal-image-error').removeClass('d-none');
        $('#principal-image-error').html('');
        $('#principal-image-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Principal image is required</strong></small>");
        image_flag = true;
    }

    if(principal_name_flag == true || principal_dob_flag == true || principal_gender_flag == true || principal_fathers_name_flag == true || principal_email_flag == true || principal_contact_flag == true || pincode_flag == true || branchCode_flag == true || image_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("principal_name", principal_name);
        formdata.append("principal_dob", principal_dob);
        formdata.append("principal_gender", principal_gender);
        formdata.append("principal_fathers_name", principal_fathers_name);
        formdata.append("principal_email", principal_email);
        formdata.append("principal_contact", principal_contact);
        formdata.append("principal_address", principal_address);
        formdata.append("branchPinCode", branchPinCode);
        formdata.append("principalCity", principalCity);
        formdata.append("principal_state", principal_state);
        formdata.append("branchCode", branchCode);
    
        let myFileimg = document.getElementById('stu_photo').files[0];
        if (typeof myFileimg != 'undefined') {
            formdata.append('profile_image', myFileimg, myFileimg['name']);
        }
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        var url = window.location.href;
        var urlSplit = url.split('/');
        var res1 = urlSplit[urlSplit.length - 1];
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "/manage/edit-principal/"+res1,
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
                        title: 'Principal updated successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else{
                    alert('An Error occured while updating principal. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}




function changeStatus(thisTxt) {
    var principalId = $(thisTxt).attr('principalId');
    const csrftoken = getCookie('csrftoken');
    if ($(thisTxt).is(':checked')) {
        // alert('enabling');
        // AJAX CAll
        // ======================================================
        $.ajax({
            type: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            url: "change-principal-status",
            data: { 'principalId': principalId, 'data': true },
            success: function (response) {
                if(response['message'] == 'success'){
                Swal.fire({
                    icon: 'success',
                    title: 'Principal enabled successfully.',
                    showConfirmButton: false,
                    timer: 1000
                })
            }else{
                alert('An Error occured while updating status. Please try again!');
                return false;
            }
                
            }
        });
        // ======================================================
    } else {
        // alert('disableing');
        // AJAX CAll
        // ======================================================
        $.ajax({
            type: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            url: "change-principal-status",
            data: { 'principalId': principalId, 'data': false },
            success: function (response) {
                if(response['message'] == 'success'){
                Swal.fire({
                    icon: 'success',
                    title: 'Principal disabled successfully.',
                    showConfirmButton: false,
                    timer: 1000
                })
            }else{
                alert('An Error occured while updating principal. Please try again!');
                return false;
            }
            }
        });
        // ======================================================
    }
}