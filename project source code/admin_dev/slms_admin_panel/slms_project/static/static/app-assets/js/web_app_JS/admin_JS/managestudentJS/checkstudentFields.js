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
                    $('#studentCity').val('');
                    $('#student_state').val('');

                    $('#studentCity').val(district);
                    $('#student_state').val(state);
                    $('#student_state').selectpicker('refresh');
                    $('#student-pincode-error').addClass('d-none');

                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $(thisTxt).css('color', 'red');
                    $('#studentCity').val('');
                    $('#student_state').val('');
                    $('#student_state').selectpicker('refresh');
                    $('#student-pincode-error').removeClass('d-none');
                }

            }
        });
    } else {
        $('#studentCity').val('');
        $('#student_state').val('');
        $('#student_state').selectpicker('refresh');
    }
}


var registration_flag = false;
var email_flag = false;
var contact_flag = false;
var parent_contact_flag = false;

// check for  schoolAdmin fields existance
function checkFields(thisTxt) {
    var fieldType = $(thisTxt).attr('fieldType');
    var searchString = '';

    if (fieldType.trim() == 'student_registration_no') {
        searchString = $('#student_registration_no').val().trim();
    } else if (fieldType.trim() == 'student_email') {
        searchString = $('#student_email').val().trim();
    } else if (fieldType.trim() == 'student_contact') {
        searchString = $('#student_contact').val().trim();
    } else if (fieldType.trim() == 'student_parent_contact') {
        searchString = $('#student_parent_contact').val().trim();
    }
    // AJAX CAll
    // ======================================================
    $.ajax({
        type: 'GET',
        url: "add-student-field-check",
        data: { 'fieldType': fieldType, 'searchString': searchString },
        success: function (response) {
            console.log('response >>> ', response);
            if (fieldType.trim() == 'student_email') {
                var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                if (searchString.match(mailformat)) {
                    if (response['message'] == 'student-email-exist') {
                        $(thisTxt).css('border', '2px solid red');
                        $('#student-email-error').removeClass('d-none');
                        $('#student-email-error').html('');
                        $('#student-email-error').html('<small><strong> Email Already Exist!</strong></small>');
                        email_flag = true;
                    } else {
                        $('#student-email-error').addClass('d-none');
                        $(thisTxt).css('border', '');
                        email_flag = false;
                    }
                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $('#student-email-error').removeClass('d-none');
                    $('#student-email-error').html('');
                    $('#student-email-error').html('<small><strong> Invalid email!</strong></small>');
                    email_flag = true;
                }

            } else if (fieldType.trim() == 'student_registration_no') {
                if (response['message'] == 'student-registration-exist') {
                    $(thisTxt).css('border', '2px solid red');
                    $('#student-registration-error').removeClass('d-none');
                    registration_flag = true;
                } else {
                    $('#student-registration-error').addClass('d-none');
                    $(thisTxt).css('border', '');
                    registration_flag = false;
                }
            }else if (fieldType.trim() == 'student_contact') {
                if (response['message'] == 'student-contact-exist') {
                    $(thisTxt).css('border', '2px solid red');
                    $('#student-contact-error').removeClass('d-none');
                    contact_flag = true;
                } else {
                    $('#student-contact-error').addClass('d-none');
                    $(thisTxt).css('border', '');
                    contact_flag = false;
                }
            }else if (fieldType.trim() == 'student_parent_contact') {
                if (response['message'] == 'student-parent-contact-exist') {
                    $(thisTxt).css('border', '2px solid red');
                    $('#student_parent-contact-error').removeClass('d-none');
                    parent_contact_flag = true;
                } else {
                    $('#student_parent-contact-error').addClass('d-none');
                    $(thisTxt).css('border', '');
                    parent_contact_flag = false;
                }
            }

            // button enabled/disable
            if (registration_flag == true || email_flag == true || contact_flag == true || parent_contact_flag == true) {
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