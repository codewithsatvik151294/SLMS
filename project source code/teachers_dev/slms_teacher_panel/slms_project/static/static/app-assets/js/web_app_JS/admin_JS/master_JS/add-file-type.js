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



var fileTypeName_flag = false;

// add new fileType
function add_file_type(){

    var fileTypeName = $('#fileType-name').val().trim();

    // field validation
    if (fileTypeName == '') {
        $('#fileType-name-error').removeClass('d-none');
        $('#fileType-name-error').html('');
        $('#fileType-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;File type name is required</strong></small>");
        fileTypeName_flag = true;
    } else {
        $('#fileType-name-error').addClass('d-none');
        fileTypeName_flag = false;
    }

    if (fileTypeName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("fileTypeName", fileTypeName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-file-type",
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
                        title: 'New file type added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'file type already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new file type. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}