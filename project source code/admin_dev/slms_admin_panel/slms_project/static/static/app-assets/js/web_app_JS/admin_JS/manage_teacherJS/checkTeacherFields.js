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

// get post code details
function getPostalAddress(thisTxt) {
    var pincode = $(thisTxt).val().trim();
    if (pincode.length == 6) {
        Swal.showLoading();

        $.ajax({
            type: 'GET',
            url: "https://api.postalpincode.in/pincode/" + pincode,
            success: function (response) {
                Swal.close();

                if (response[0]['Status'] == 'Success') {
                    $(thisTxt).css('border', '');
                    $(thisTxt).css('color', 'black');

                    var district = response[0]['PostOffice'][0]['District'];
                    var state = response[0]['PostOffice'][0]['State'];
                    $('#teacherCity').val('');
                    $('#teacher_state').val('');

                    $('#teacherCity').val(district);
                    $('#teacher_state').val(state);
                    // $('#teacher_state').selectpicker();
                    $('#teacher_state').selectpicker('refresh');
                    $('#teacher-pincode-error').addClass('d-none');

                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $(thisTxt).css('color', 'red');
                    $('#teacherCity').val('');
                    $('#teacher_state').val('');
                    // $('#teacher_state').selectpicker();
                    $('#teacher_state').selectpicker('refresh');
                    $('#teacher-pincode-error').removeClass('d-none');
                }

            }
        });
    } else {
        $('#teacherCity').val('');
        $('#teacher_state').val('');
        // $('#teacher_state').selectpicker();
        $('#teacher_state').selectpicker('refresh');
    }
}



// global variable flags
var emailFlag = false;
var contactFlag = false;
// check for  teacher fields existance
function checkFields(thisTxt) {
    var fieldType = $(thisTxt).attr('fieldType');
    var searchString = '';

    if (fieldType.trim() == 'teacher_email') {
        searchString = $('#teacher_email').val().trim();
    } else if (fieldType.trim() == 'teacher_contact') {
        searchString = $('#teacher_contact').val().trim();
    }
    // AJAX CAll
    // ======================================================
    $.ajax({
        type: 'GET',
        url: "add-teacher-field-check",
        data: { 'fieldType': fieldType, 'searchString': searchString },
        success: function (response) {
            console.log('response >>> ', response);
            if (fieldType.trim() == 'teacher_email') {
                var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                if (searchString.match(mailformat)) {
                    if (response['message'] == 'teacher-email-exist') {
                        $(thisTxt).css('border', '2px solid red');
                        $('#teacher-email-error').removeClass('d-none');
                        $('#teacher-email-error').html('');
                        $('#teacher-email-error').html('<small><strong> Email Already Exist!</strong></small>');
                        emailFlag = true;
                    } else {
                        $('#teacher-email-error').addClass('d-none');
                        $(thisTxt).css('border', '');
                        emailFlag = false;
                    }
                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $('#teacher-email-error').removeClass('d-none');
                    $('#teacher-email-error').html('');
                    $('#teacher-email-error').html('<small><strong> Invalid email!</strong></small>');
                    emailFlag = true;
                }

            } else if (fieldType.trim() == 'teacher_contact') {
                if (response['message'] == 'teacher-contact-exist') {
                    $(thisTxt).css('border', '2px solid red');
                    $('#teacher-contact-error').removeClass('d-none');
                    contactFlag = true;
                } else {
                    $('#teacher-contact-error').addClass('d-none');
                    $(thisTxt).css('border', '');
                    contactFlag = false;
                }
            }

            // button enabled/disable
            if (emailFlag == true || contactFlag == true) {
                $('#submit_btn').css('pointer-events', 'none');
                $('#submit_btn').css('opacity', '0.2');
            } else {
                $('#submit_btn').css('pointer-events', '');
                $('#submit_btn').css('opacity', '1');
            }
        }
    });
    // ======================================================
}


function changeStatus(thisTxt) {
    var teacherId = $(thisTxt).attr('teacherId');
    const csrftoken = getCookie('csrftoken');
    if ($(thisTxt).is(':checked')) {
        // alert('enabling');
        // AJAX CAll
        // ======================================================
        $.ajax({
            type: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            url: "change-teacher-status",
            data: { 'teacherId': teacherId, 'data': true },
            success: function (response) {
                if(response['message'] == 'success'){
                Swal.fire({
                    icon: 'success',
                    title: 'Teacher enabled successfully.',
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
            url: "change-teacher-status",
            data: { 'teacherId': teacherId, 'data': false },
            success: function (response) {
                if(response['message'] == 'success'){
                Swal.fire({
                    icon: 'success',
                    title: 'Teacher disabled successfully.',
                    showConfirmButton: false,
                    timer: 1000
                })
            }else{
                alert('An Error occured while updating teacher. Please try again!');
                return false;
            }
            }
        });
        // ======================================================
    }
}