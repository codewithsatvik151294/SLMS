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



var classTypeName_flag = false;
var classSubTypeName_flag = false;

// add new classType
function add_new_classType(){

    var classTypeName = $('#class-type-name').val().trim();
    var classSubTypeName = $('#class-sub-type-name').val().trim();

    // field validation
    if (classTypeName == '') {
        $('#class-type-name-error').removeClass('d-none');
        $('#class-type-name-error').html('');
        $('#class-type-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Class type name is required</strong></small>");
        classTypeName_flag = true;
    } else {
        $('#class-type-name-error').addClass('d-none');
        classTypeName_flag = false;
    }

    if (classSubTypeName == '') {
        $('#class-sub-type-name-error').removeClass('d-none');
        $('#class-sub-type-name-error').html('');
        $('#class-sub-type-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Class sub-type name is required</strong></small>");
        classSubTypeName_flag = true;
    } else {
        $('#class-sub-type-name-error').addClass('d-none');
        classSubTypeName_flag = false;
    }

    if (classTypeName_flag == true || classSubTypeName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("classTypeName", classTypeName);
        formdata.append("classSubTypeName", classSubTypeName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-class-type",
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
                        title: 'New class type added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Class type and sub-type pair already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new class type. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}