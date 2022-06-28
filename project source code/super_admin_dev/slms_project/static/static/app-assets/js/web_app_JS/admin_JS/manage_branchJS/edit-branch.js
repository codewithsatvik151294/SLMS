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
var branchCode_flag = false;
var branchName_flag = false;
var branchEmail_flag = false;
var branchContact_flag = false;
var branchPinCode_flag = false;

// add new branch
function edit_branch(){

    var branchCode = $('#branchCode').val().trim();
    var branchName = $('#branchName').val().trim();
    var branchEmail = $('#branchEmail').val().trim();
    var branchContact = $('#branchContact').val().trim();
    var branchAddress = $('#branchAddress').val().trim();
    var branchPinCode = $('#branchPinCode').val().trim();
    var branchCity = $('#branchCity').val().trim();
    var branchState = $('#branch_state').val().trim();

    // field validation
    if (branchCode == '') {
        $('#branch-code-error').removeClass('d-none');
        $('#branch-code-error').html('');
        $('#branch-code-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch code is required</strong></small>");
        branchCode_flag = true;
    } else {
        $('#branch-code-error').addClass('d-none');
        branchCode_flag = false;
    }
    
    if (branchName == '') {
        $('#branch-name-error').removeClass('d-none');
        $('#branch-name-error').html('');
        $('#branch-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch name is required</strong></small>");
        branchName_flag = true;
    } else {
        $('#branch-name-error').addClass('d-none');
        branchName_flag = false;
    }

    if (branchName.length < 3) {
        $('#branch-name-error').removeClass('d-none');
        $('#branch-name-error').html('');
        $('#branch-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch name must be of minimum 4 characters</strong></small>");
        branchName_flag = true;
    } else {
        $('#branch-name-error').addClass('d-none');
        branchName_flag = false;
    }

    if (branchEmail == '') {
        $('#branch-email-error').removeClass('d-none');
        $('#branch-email-error').html('');
        $('#branch-email-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch email is required</strong></small>");
        branchEmail_flag = true;
    } else {
        $('#branch-email-error').addClass('d-none');
        branchEmail_flag = false;
    }

    if (branchContact == '') {
        $('#student-contact-error').removeClass('d-none');
        if (branchContact.length == 0) {
            $('#student-contact-error').html('');
            $('#student-contact-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch contact is required</strong></small>");
            branchContact_flag = true;
        }
    } else {
        if (branchContact.length < 10) {
            $('#student-contact-error').removeClass('d-none');
            $('#student-contact-error').html('');
            $('#student-contact-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Invalid contact</strong></small>');
            branchContact_flag = true;
        } else {
            $('#student-contact-error').addClass('d-none');
            branchContact_flag = false;
        }
    }
    
    if (branchPinCode == '') {
        $('#branch-pincode-error').removeClass('d-none');
        $('#branch-pincode-error').html('');
        $('#branch-pincode-error').append('<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Pincode is required</strong></small>');
        branchPinCode_flag = true;
    } else {
        $('#branch-pincode-error').addClass('d-none');
        branchPinCode_flag = false;
    }


    if(branchCode_flag == true || branchName_flag == true || branchEmail_flag == true || branchContact_flag == true || branchPinCode_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("branchCode", branchCode);
        formdata.append("branchName", branchName);
        formdata.append("branchEmail", branchEmail);
        formdata.append("branchContact", branchContact);
        formdata.append("branchAddress", branchAddress);
        formdata.append("branchPinCode", branchPinCode);
        formdata.append("branchCity", branchCity);
        formdata.append("branchState", branchState);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        var url = window.location.href;
        var urlSplit = url.split('/');
        var res1 = urlSplit[urlSplit.length - 1];
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "/manage/edit-branch/"+res1,
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache : false,
            processData : false,
            contentType : false,
            encType : 'multipart/form-data',
            success: function (response) {            
                if(response['message'] == 'success'){
                    Swal.fire({
                        icon: 'success',
                        title: '<small>Branch updated successfully.</small>',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else{
                    alert('An Error occured while updating Branch. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}