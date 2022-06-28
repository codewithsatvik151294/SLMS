// get post code details
function getPostalAddress(thisTxt) {
    var pincode = $(thisTxt).val().trim();
    if (pincode.length == 6) {
        Swal.showLoading();

        $.ajax({
            type: 'GET',
            url: "https://api.postalpincode.in/pincode/"+pincode,
            success: function (response) {
                Swal.close();

                if(response[0]['Status'] == 'Success'){
                    $(thisTxt).css('border','');
                    $(thisTxt).css('color','black');

                    var district = response[0]['PostOffice'][0]['District'];
                    var state = response[0]['PostOffice'][0]['State'];
                    $('#branchCity').val('');
                    $('#branch_state').val('');
                    
                    $('#branchCity').val(district);
                    $('#branch_state').val(state);
                    // $('#branch_state').selectpicker();
                    // $('#branch_state').selectpicker('refresh');
                    $('#branch-pincode-error').addClass('d-none');

                }else{
                    $(thisTxt).css('border','2px solid red');
                    $(thisTxt).css('color','red');
                    $('#branchCity').val('');
                    $('#branch_state').val('');
                    // $('#branch_state').selectpicker();
                    // $('#branch_state').selectpicker('refresh');
                    $('#branch-pincode-error').removeClass('d-none');
                }
                
            }
        });
    }else{
        $('#branchCity').val('');
        $('#branch_state').val('');
        // $('#branch_state').selectpicker();
        // $('#branch_state').selectpicker('refresh');
    }
}

// =========================================================
// global variable flags
var codeFlag = false;
var nameFlag = false;
var emailFlag = false;
var contactFlag = false;
// check for  branch fields existance
function checkFields (thisTxt){
    var fieldType = $(thisTxt).attr('fieldType');
    var searchString = '';

    if(fieldType.trim() == 'branchCode'){
        searchString = $('#branchCode').val().trim();
    }else if(fieldType.trim() == 'branchName'){
        searchString = $('#branchName').val().trim();
    }else if(fieldType.trim() == 'branchEmail'){
        searchString = $('#branchEmail').val().trim();
    }else if(fieldType.trim() == 'branchContact'){
        searchString = $('#branchContact').val().trim();
    }
    // AJAX CAll
    // ======================================================
    $.ajax({
        type: 'GET',
        url: "add-branch-field-check",
        data : {'fieldType':fieldType,'searchString':searchString},
        success: function (response) {
            if(fieldType.trim() == 'branchCode'){
                if(response['message'] == 'branch-code-exist'){
                    $(thisTxt).css('border','2px solid red');
                    $('#branch-code-error').removeClass('d-none');
                    codeFlag = true;
                }else{
                    $('#branch-code-error').addClass('d-none');
                    $(thisTxt).css('border','');
                    codeFlag = false;
                }
            }else if(fieldType.trim() == 'branchName'){
                if(response['message'] == 'branch-name-exist'){
                    $(thisTxt).css('border','2px solid red');
                    $('#branch-name-error').removeClass('d-none');
                    nameFlag = true;
                }else{
                    $('#branch-name-error').addClass('d-none');
                    $(thisTxt).css('border','');
                    nameFlag = false;
                }
            }else if(fieldType.trim() == 'branchEmail'){
                var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                if (searchString.match(mailformat)) {
                    if(response['message'] == 'branch-email-exist'){
                        $(thisTxt).css('border','2px solid red');
                        $('#branch-email-error').removeClass('d-none');
                        $('#branch-email-error').html('');
                        $('#branch-email-error').html('<small><strong> Email Already Exist!</strong></small>');
                        emailFlag = true;
                    }else{
                        $('#branch-email-error').addClass('d-none');
                        $(thisTxt).css('border','');
                        emailFlag = false;
                    }
                } else {
                    $(thisTxt).css('border','2px solid red');
                    $('#branch-email-error').removeClass('d-none');
                    $('#branch-email-error').html('');
                    $('#branch-email-error').html('<small><strong> Invalid email!</strong></small>');
                    emailFlag = true;
                }
                
            }else if(fieldType.trim() == 'branchContact'){
                if(response['message'] == 'branch-contact-exist'){
                    $(thisTxt).css('border','2px solid red');
                    $('#branch-contact-error').removeClass('d-none');
                    contactFlag = true;
                }else{
                    $('#branch-contact-error').addClass('d-none');
                    $(thisTxt).css('border','');
                    contactFlag = false;
                }
            } 

            // button enabled/disable
            if(codeFlag == true || nameFlag == true || emailFlag == true || contactFlag == true){
                $('#submit_btn').css('pointer-events','none');
                $('#submit_btn').css('opacity','0.2');
            }else{
                $('#submit_btn').css('pointer-events','');
                $('#submit_btn').css('opacity','1');
            }
        }
    });
    // ======================================================
}