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



var sectionName_flag = false;

// add new section
function add_new_section(){

    var sectionName = $('#section-name').val().trim();

    // field validation
    if (sectionName == '') {
        $('#section-name-error').removeClass('d-none');
        $('#section-name-error').html('');
        $('#section-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Section name is required</strong></small>");
        sectionName_flag = true;
    } else {
        $('#section-name-error').addClass('d-none');
        sectionName_flag = false;
    }

    if (sectionName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("sectionName", sectionName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-section",
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
                        title: 'New section added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'section already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new section. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}