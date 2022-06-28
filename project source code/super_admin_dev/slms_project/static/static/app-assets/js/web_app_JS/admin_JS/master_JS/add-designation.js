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



var designationName_flag = false;

// add new designation
function add_designation(){

    var designationName = $('#designation-name').val().trim();

    // field validation
    if (designationName == '') {
        $('#designation-name-error').removeClass('d-none');
        $('#designation-name-error').html('');
        $('#designation-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Designation name is required</strong></small>");
        designationName_flag = true;
    } else {
        $('#designation-name-error').addClass('d-none');
        designationName_flag = false;
    }

    if (designationName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("designationName", designationName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-designation",
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
                        title: 'New designation added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Designation already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new designation. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}