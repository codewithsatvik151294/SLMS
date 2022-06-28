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

// global flags
var badge_image_flag = false;
var description_flag = false;

// global variables
var badge_image = '';
var description = '';


// update badge
function update_badge(){
    description = $('#bagde-description').val().trim();

    if (description == '') {
        $('#bagde-description-error').removeClass('d-none');
        $('#bagde-description-error').html('');
        $('#bagde-description-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Badge description  must be minimum of 10 characters</strong></small>");
        description_flag = true;
    } else {
        $('#bagde-description-error').addClass('d-none');
        description_flag = false;
    }

    if (description == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("description", description);
    
        let myFileimg = document.getElementById('badge').files[0];
        if (typeof myFileimg != 'undefined') {
            formdata.append('image', myFileimg, myFileimg['name']);
        }else
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        var url = window.location.href;
        var urlSplit = url.split('/');
        var res1 = urlSplit[urlSplit.length - 1];
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "/badge-management/edit-badge/"+res1,
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
                        title: 'Badge updated successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else{
                    alert('An Error occured while updating badge. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}
