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



var authorityID_flag = false;
var sub_authority_name_flag = false;

// add new authority
function add_new_sub_authority() {

    var authorityID = $('#authority-id').val();

    // field validation
    if (authorityID.length == 0) {
        $('#authority-name-error').removeClass('d-none');
        $('#authority-name-error').html('');
        $('#authority-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Authority is required</strong></small>");
        authorityID_flag = true;
    } else {
        $('#authority-name-error').addClass('d-none');
        authorityID_flag = false;
    }

    var sub_auth_array = [];

    $('.sub-auth-name').each(function () {
        sub_auth_array.push($(this).val());
        if ($(this).val().trim() == '') {
            $(this).css('border', '1px solid red');
            $('#sub-authority-name-error').removeClass('d-none');
            $('#sub-authority-name-error').html('');
            $('#sub-authority-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Sub authority name is required</strong></small>");
            sub_authority_name_flag = true;
        } else {
            $(this).css('border', '');
            $('#sub-authority-name-error').addClass('d-none');
            sub_authority_name_flag = false;
        }
    });
    console.log(sub_auth_array);


    if (authorityID_flag == true || sub_authority_name_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("authorityID", authorityID);
        formdata.append("sub_auth_array[]", sub_auth_array);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-sub-authority",
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response['response']);

                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'New sub authority added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                } else if (response['message'] == 'data exist') {
                    Swal.fire({
                        icon: 'error',
                        title: 'Sub authority with this authority already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                } else {
                    alert('An Error occured while adding new sub authority. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}



$(document).on('click', '.add-sub-auth', function () {
    $("#sub-authority").append('<div class="row"><div class="col-lg-10 form-group mt-1">  <input class="form-control sub-auth-name" placeholder="Enter sub authority name"></div><div class="text-right col-lg-2  pt-1" ><a style="margin-top:2px" class="btn btn-danger remove-subauth  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');
});

$(document).on('click', '.remove-subauth', function () {
    $(this).parent().parent('.row').remove();

});


function check_sub_auth(thisTxt) {
    var Auth_ID = $(thisTxt).val();
    $.ajax({
        type: 'GET',
        url: "check-authority",
        data: { 'Auth_ID': Auth_ID },
        success: function (response) {
            if (response['message'] == 'exist') {
                $('#authority-name-error').removeClass('d-none');
                $('#authority-name-error').html('');
                $('#authority-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Authority with sub-authority already exist</strong></small>");
                $('#submitBtn').css('pointer-events', 'none');
                $('#submitBtn').css('opacity', '0.2');
                return false;
            }else {
                $('#authority-name-error').addClass('d-none');
                $('#authority-name-error').html('');
                $('#submitBtn').css('pointer-events', '');
                $('#submitBtn').css('opacity', '1');
            }
        }
    });
}