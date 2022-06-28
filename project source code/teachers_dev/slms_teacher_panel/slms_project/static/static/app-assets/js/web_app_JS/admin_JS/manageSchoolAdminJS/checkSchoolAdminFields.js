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
                    $('#schoolAdminCity').val('');
                    $('#schoolAdmin_state').val('');

                    $('#schoolAdminCity').val(district);
                    $('#schoolAdmin_state').val(state);
                    // $('#schoolAdmin_state').selectpicker();
                    $('#schoolAdmin_state').selectpicker('refresh');
                    $('#schoolAdmin-pincode-error').addClass('d-none');

                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $(thisTxt).css('color', 'red');
                    $('#schoolAdminCity').val('');
                    $('#schoolAdmin_state').val('');
                    // $('#schoolAdmin_state').selectpicker();
                    $('#schoolAdmin_state').selectpicker('refresh');
                    $('#schoolAdmin-pincode-error').removeClass('d-none');
                }

            }
        });
    } else {
        $('#schoolAdminCity').val('');
        $('#schoolAdmin_state').val('');
        // $('#schoolAdmin_state').selectpicker();
        $('#schoolAdmin_state').selectpicker('refresh');
    }
}

// global variable flags
var codeFlag = false;
var emailFlag = false;
var contactFlag = false;


// branch existance check for schoolAdmin
function checkBranch(thisTxt) {
    if ($(thisTxt).val().trim() != '') {
        // ---------------  AJAX CALL  ----------------------------
        $.ajax({
            type: 'GET',
            url: "school-admin-checkBranch",
            data: { 'branchCode': $(thisTxt).val().trim() },
            success: function (response) {
                console.log('response >>> ', response);
                if (response['message'] == 'schoolAdmin-branch-exist') {
                    $('#schoolAdmin-branchcode-error').removeClass('d-none');
                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                    codeFlag = true;
                } else {
                    $('#schoolAdmin-branchcode-error').addClass('d-none');
                    $('#submit_btn').css('pointer-events', '');
                    $('#submit_btn').css('opacity', '1');
                    codeFlag = false;
                }

                // button enabled/disable
                if (codeFlag == true || emailFlag == true || contactFlag == true) {
                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                } else {
                    $('#submit_btn').css('pointer-events', '');
                    $('#submit_btn').css('opacity', '1');
                }
            }

        });
        // --------------------------------------------------------

    }
}


// check for  schoolAdmin fields existance
function checkFields(thisTxt) {
    var fieldType = $(thisTxt).attr('fieldType');
    var searchString = '';

    if (fieldType.trim() == 'schoolAdmin_email') {
        searchString = $('#schoolAdmin_email').val().trim();
    } else if (fieldType.trim() == 'schoolAdmin_contact') {
        searchString = $('#schoolAdmin_contact').val().trim();
    }
    // AJAX CAll
    // ======================================================
    $.ajax({
        type: 'GET',
        url: "add-school-admin-field-check",
        data: { 'fieldType': fieldType, 'searchString': searchString },
        success: function (response) {
            console.log('response >>> ', response);
            if (fieldType.trim() == 'schoolAdmin_email') {
                var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                if (searchString.match(mailformat)) {
                    if (response['message'] == 'schoolAdmin-email-exist') {
                        $(thisTxt).css('border', '2px solid red');
                        $('#schoolAdmin-email-error').removeClass('d-none');
                        $('#schoolAdmin-email-error').html('');
                        $('#schoolAdmin-email-error').html('<small><strong> Email Already Exist!</strong></small>');
                        emailFlag = true;
                    } else {
                        $('#schoolAdmin-email-error').addClass('d-none');
                        $(thisTxt).css('border', '');
                        emailFlag = false;
                    }
                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $('#schoolAdmin-email-error').removeClass('d-none');
                    $('#schoolAdmin-email-error').html('');
                    $('#schoolAdmin-email-error').html('<small><strong> Invalid email!</strong></small>');
                    emailFlag = true;
                }

            } else if (fieldType.trim() == 'schoolAdmin_contact') {
                if (response['message'] == 'schoolAdmin-contact-exist') {
                    $(thisTxt).css('border', '2px solid red');
                    $('#schoolAdmin-contact-error').removeClass('d-none');
                    contactFlag = true;
                } else {
                    $('#schoolAdmin-contact-error').addClass('d-none');
                    $(thisTxt).css('border', '');
                    contactFlag = false;
                }
            }

            // button enabled/disable
            if (codeFlag == true || emailFlag == true || contactFlag == true) {
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


