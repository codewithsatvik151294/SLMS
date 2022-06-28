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
var director_name_flag = false;
var director_dob_flag = false;
var director_gender_flag = false;
var director_fathers_name_flag = false;
var director_email_flag = false;
var director_contact_flag = false;
var pincode_flag = false;
var city_flag = false;
var branchCode_flag = false;
var image_flag = false;
var branch_flag = false;
// add new director
function add_new_director(){

    var director_name = $('#director_name').val().trim();
    var director_dob = $('#director_dob').val().trim();
    var director_gender = $('#director_gender').val().trim();
    var director_fathers_name = $('#director_fathers_name').val().trim();
    var director_email = $('#director_email').val().trim();
    var director_contact = $('#director_contact').val().trim();
    var director_address = $('#director_address').val().trim();
    var branchPinCode = $('#branchPinCode').val().trim();
    var directorCity = $('#directorCity').val().trim();
    var director_state = $('#director_state').val().trim();
    var branchCode = $('#default-select').val().trim();


    // field validation
    if (director_name == '') {
        $('#director-name-error').removeClass('d-none');
        $('#director-name-error').html('');
        $('#director-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director name is required</strong></small>");
        director_name_flag = true;
    } else {
        $('#director-name-error').addClass('d-none');
        director_name_flag = false;
    }

    if (director_name.length < 3) {
        $('#director-name-error').removeClass('d-none');
        $('#director-name-error').html('');
        $('#director-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director name must be of minimum 4 characters</strong></small>");
        director_name_flag = true;
    } else {
        $('#director-name-error').addClass('d-none');
        director_name_flag = false;
    }

    if (director_dob == '') {
        $('#director-dob-error').removeClass('d-none');
        $('#director-dob-error').html('');
        $('#director-dob-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director DOB is required</strong></small>");
        director_dob_flag = true;
    } else {
        $('#director-dob-error').addClass('d-none');
        director_dob_flag = false;
    }

    if (director_gender == '') {
        $('#director-gender-error').removeClass('d-none');
        $('#director-gender-error').html('');
        $('#director-gender-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director gender is required</strong></small>");
        director_gender_flag = true;
    } else {
        $('#director-gender-error').addClass('d-none');
        director_gender_flag = false;
    }

    if (director_fathers_name == '') {
        $('#director-father-name-error').removeClass('d-none');
        $('#director-father-name-error').html('');
        $('#director-father-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director father's name is required</strong></small>");
        director_fathers_name_flag = true;
    } else {
        $('#director-father-name-error').addClass('d-none');
        director_fathers_name_flag = false;
    }

    if (director_fathers_name.length < 3) {
        $('#director-father-name-error').removeClass('d-none');
        $('#director-father-name-error').html('');
        $('#director-father-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director father's name must be of minimum 4 characters</strong></small>");
        director_fathers_name_flag = true;
    } else {
        $('#director-father-name-error').addClass('d-none');
        director_fathers_name_flag = false;
    }

    if (director_email == '') {
        $('#director-email-error').removeClass('d-none');
        $('#director-email-error').html('');
        $('#director-email-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director email is required</strong></small>");
        director_email_flag = true;
    } else {
        $('#director-email-error').addClass('d-none');
        director_email_flag = false;
    }


    if (director_contact == '') {
        $('#director-contact-error').removeClass('d-none');
        if (director_contact.length == 0) {
            $('#director-contact-error').html('');
            $('#director-contact-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Director contact is required</strong></small>");
            director_contact_flag = true;
        }
    } else {
        if (director_contact.length < 10) {
            $('#director-contact-error').removeClass('d-none');
            $('#director-contact-error').html('');
            $('#director-contact-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Invalid contact</strong></small>');
            director_contact_flag = true;
        } else {
            $('#director-contact-error').addClass('d-none');
            director_contact_flag = false;
        }
    }

    if (branchPinCode == '') {
        $('#director-pincode-error').removeClass('d-none');
        $('#director-pincode-error').html('');
        $('#director-pincode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Pincode is required</strong></small>');
        pincode_flag = true;
    } else {
        $('#director-pincode-error').addClass('d-none');
        pincode_flag = false;
    }

    if (directorCity == '') {
        $('#director-city-error').removeClass('d-none');
        $('#director-city-error').html('');
        $('#director-city-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;City is required</strong></small>');
        city_flag = true;
    } else {
        $('#director-city-error').addClass('d-none');
        city_flag = false;
    }

    if (branchCode == '') {
        $('#director-branch-error').removeClass('d-none');
        $('#director-branch-error').html('');
        $('#director-branch-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Director branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#director-branch-error').addClass('d-none');
        $('#director-branch-error').html('');
        branch_flag = false;
    }

    let img_data = document.getElementById('stu_photo').files[0];
    if (typeof img_data != 'undefined') {
        $('#director-image-error').addClass('d-none');
        $('#director-image-error').html('');
        image_flag = false;
    } else {
        $('#director-image-error').removeClass('d-none');
        $('#director-image-error').html('');
        $('#director-image-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Director image is required</strong></small>");
        image_flag = true;
    }

    if(director_name_flag == true || director_dob_flag == true || director_gender_flag == true || director_fathers_name_flag == true || director_email_flag == true || director_contact_flag == true || pincode_flag == true || city_flag == true || branchCode_flag == true || image_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("director_name", director_name);
        formdata.append("director_dob", director_dob);
        formdata.append("director_gender", director_gender);
        formdata.append("director_fathers_name", director_fathers_name);
        formdata.append("director_email", director_email);
        formdata.append("director_contact", director_contact);
        formdata.append("director_address", director_address);
        formdata.append("branchPinCode", branchPinCode);
        formdata.append("directorCity", directorCity);
        formdata.append("director_state", director_state);
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
            url: "add-director",
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
                        title: 'New director added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'director-list'
                    })
                }else{
                    alert('An Error occured while adding new director. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}