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


// check for existing designations
function check_designation(thisTxt){
    // ======== AJAX call ======================
    Swal.showLoading();
        $.ajax({
            type: 'GET',
            url: "check-designation",
            data : {'designation_id':$(thisTxt).val().trim()},
            success: function (response) {
                Swal.close();
                if(response['message'] == 'not-exist'){
                    $('#auth-section').css('opacity','1');
                    $('#auth-section').css('pointer-events','');
                    $('#designation-error').addClass('d-none');
                    $('#designation-error').html('');
                }else{
                    $('#auth-section').css('opacity','0.3');
                    $('#auth-section').css('pointer-events','none');
                    $('#designation-error').removeClass('d-none');
                    $('#designation-error').html('');
                    $('#designation-error').append('<small><strong> Designation already exist with attached authorities.</strong></small>');
                }
            }
        });
    // =========================================
}

var designation_flag = false;
var authorityArray_false = false;
var subAuthorityArray_false = false;
// attach_new_student
function update_authority(){
    var selectCounter = 0;

    var authority_array = []

    var row_count = $('tbody tr').length;;
    console.log('row_count >>> ',row_count);

    for(var i=1;i<=row_count;i++){
        var auth_dict = {}
        auth_dict['auth_name'] = $('#authority-name-'+i+'').text();
        if($('#selected-authority-'+i+'').prop("checked") == true){
            auth_dict['auth_selected'] = true;
        }
        else if($('#selected-authority-'+i+'').prop("checked") == false){
            auth_dict['auth_selected'] = false;
        }

        var sub_auth_dict = {};

        $('.sub-auth-name-'+i+'').each(function(){
            if($(this).parent().parent().find('input').prop("checked") == true){
                sub_auth_dict[''+$(this).text()+''] = true;
                selectCounter = selectCounter + 1;
            }
            else if($(this).parent().parent().find('input').prop("checked") == false){
                sub_auth_dict[''+$(this).text()+''] = false;
            }
        });


        auth_dict['sub_auth'] = sub_auth_dict;
        authority_array.push(auth_dict);

    }

    if(selectCounter > 0){
        var formdata = new FormData();
        formdata.append("authority_array", JSON.stringify(authority_array));
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        var url = window.location.href;
        var urlSplit = url.split('/');
        var res1 = urlSplit[urlSplit.length - 1];
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "/authority-management/edit-authority/"+res1,
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response['message']);
                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'Authorities updated successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else {
                    alert('An Error occured while attaching updating authorities. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }else if(selectCounter <= 0){
        alert('Select atleast 1 authority or sub-authority to continue.');
        return false;
    }
}