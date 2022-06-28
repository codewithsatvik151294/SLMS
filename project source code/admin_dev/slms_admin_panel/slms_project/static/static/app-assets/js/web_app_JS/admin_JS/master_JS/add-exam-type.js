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



var examTypeName_flag = false;

// add new examType
function add_exam_type(){

    var examTypeName = $('#exam-type-name').val().trim();

    // field validation
    if (examTypeName == '') {
        $('#examtype-name-error').removeClass('d-none');
        $('#examtype-name-error').html('');
        $('#examtype-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Exam type name is required</strong></small>");
        examTypeName_flag = true;
    } else {
        $('#examType-name-error').addClass('d-none');
        examTypeName_flag = false;
    }

    if (examTypeName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("examTypeName", examTypeName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-exam-type",
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
                        title: 'New exam type added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'exam type already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new exam type. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}