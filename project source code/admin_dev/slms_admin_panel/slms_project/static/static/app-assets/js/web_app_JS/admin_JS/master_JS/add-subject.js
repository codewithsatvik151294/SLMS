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



var subjectName_flag = false;

// add new subject
function add_new_subject(){

    var subjectName = $('#subject-name').val().trim();

    // field validation
    if (subjectName == '') {
        $('#subject-name-error').removeClass('d-none');
        $('#subject-name-error').html('');
        $('#subject-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;subject name is required</strong></small>");
        subjectName_flag = true;
    } else {
        $('#subject-name-error').addClass('d-none');
        subjectName_flag = false;
    }

    if (subjectName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("subjectName", subjectName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-subject",
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
                        title: 'New subject added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'subject already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new subject. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}