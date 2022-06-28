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



var badgeName_flag = false;

// add new badge
function add_badge_trigger(){

    var badgeName = $('#badge-name').val().trim();

    // field validation
    if (badgeName == '') {
        $('#badge-name-error').removeClass('d-none');
        $('#badge-name-error').html('');
        $('#badge-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Badge trigger name is required</strong></small>");
        badgeName_flag = true;
    } else {
        $('#badge-name-error').addClass('d-none');
        badgeName_flag = false;
    }

    if (badgeName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("badgeName", badgeName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-badge-trigger",
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
                        title: 'New badge trigger added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'badge already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new badge trigger. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}