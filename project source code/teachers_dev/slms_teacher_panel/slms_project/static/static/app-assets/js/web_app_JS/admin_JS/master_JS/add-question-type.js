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



var questionTypeName_flag = false;

// add new questionType
function add_new_questionType(){

    var questionTypeName = $('#questionType-name').val().trim();

    // field validation
    if (questionTypeName == '') {
        $('#questionType-name-error').removeClass('d-none');
        $('#questionType-name-error').html('');
        $('#questionType-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Question type name is required</strong></small>");
        questionTypeName_flag = true;
    } else {
        $('#questionType-name-error').addClass('d-none');
        questionTypeName_flag = false;
    }

    if (questionTypeName_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("questionTypeName", questionTypeName);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-question-type",
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
                        title: 'New question type added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'data exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Question type already exist',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        return false;
                    })
                }else{
                    alert('An Error occured while adding new question type. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}