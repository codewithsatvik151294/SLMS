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
                    $('#principalCity').val('');
                    $('#principal_state').val('');

                    $('#principalCity').val(district);
                    $('#principal_state').val(state);
                    // $('#principal_state').selectpicker();
                    $('#principal_state').selectpicker('refresh');
                    $('#principal-pincode-error').addClass('d-none');

                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $(thisTxt).css('color', 'red');
                    $('#principalCity').val('');
                    $('#principal_state').val('');
                    // $('#principal_state').selectpicker();
                    $('#principal_state').selectpicker('refresh');
                    $('#principal-pincode-error').removeClass('d-none');
                }

            }
        });
    } else {
        $('#principalCity').val('');
        $('#principal_state').val('');
        // $('#principal_state').selectpicker();
        $('#principal_state').selectpicker('refresh');
    }
}

// global variable flags
var codeFlag = false;
var emailFlag = false;
var contactFlag = false;


// branch existance check for principal
function checkBranch(thisTxt) {
    if ($(thisTxt).val().trim() != '') {
        // ---------------  AJAX CALL  ----------------------------
        $.ajax({
            type: 'GET',
            url: "principal-checkBranch",
            data: { 'branchCode': $(thisTxt).val().trim() },
            success: function (response) {
                console.log('response >>> ', response);
                if (response['message'] == 'principal-branch-exist') {
                    $('#principal-branchcode-error').removeClass('d-none');
                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                    codeFlag = true;
                } else {
                    $('#principal-branchcode-error').addClass('d-none');
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


// check for  principal fields existance
function checkFields(thisTxt) {
    var fieldType = $(thisTxt).attr('fieldType');
    var searchString = '';

    if (fieldType.trim() == 'principal_email') {
        searchString = $('#principal_email').val().trim();
    } else if (fieldType.trim() == 'principal_contact') {
        searchString = $('#principal_contact').val().trim();
    }
    // AJAX CAll
    // ======================================================
    $.ajax({
        type: 'GET',
        url: "add-director-field-check",
        data: { 'fieldType': fieldType, 'searchString': searchString },
        success: function (response) {
            console.log('response >>> ', response);
            if (fieldType.trim() == 'director_email') {
                var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                if (searchString.match(mailformat)) {
                    if (response['message'] == 'director-email-exist') {
                        $(thisTxt).css('border', '2px solid red');
                        $('#director-email-error').removeClass('d-none');
                        $('#director-email-error').html('');
                        $('#director-email-error').html('<small><strong> Email Already Exist!</strong></small>');
                        emailFlag = true;
                    } else {
                        $('#director-email-error').addClass('d-none');
                        $(thisTxt).css('border', '');
                        emailFlag = false;
                    }
                } else {
                    $(thisTxt).css('border', '2px solid red');
                    $('#director-email-error').removeClass('d-none');
                    $('#director-email-error').html('');
                    $('#director-email-error').html('<small><strong> Invalid email!</strong></small>');
                    emailFlag = true;
                }

            } else if (fieldType.trim() == 'director_contact') {
                if (response['message'] == 'director-contact-exist') {
                    $(thisTxt).css('border', '2px solid red');
                    $('#director-contact-error').removeClass('d-none');
                    contactFlag = true;
                } else {
                    $('#director-contact-error').addClass('d-none');
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


