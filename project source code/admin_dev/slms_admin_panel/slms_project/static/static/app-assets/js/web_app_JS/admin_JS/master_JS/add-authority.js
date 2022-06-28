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



var authorityName_flag = false;

// add new authority
function add_new_authority(){

    var authorityName = $('#authority-name').val().trim();

    // field validation
    if (authorityName == '') {
        $('#authority-name-error').removeClass('d-none');
        $('#authority-name-error').html('');
        $('#authority-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Authority name is required</strong></small>");
        authorityName_flag = true;
    } else {
        $('#authority-name-error').addClass('d-none');
        authorityName_flag = false;
    }

    if (authorityName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("authorityName", authorityName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-authority",
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
                        title: 'New authority added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Authority already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new authority. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}