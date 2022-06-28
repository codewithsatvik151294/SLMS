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

var file_type_flag = false;
var content_flag = false;

// update_study_material
function update_study_material(){
    var file_type_id = $('#file-type-id').val().trim();

    // field validation
    if (file_type_id == '') {
        $('#file-type-error').removeClass('d-none');
        $('#file-type-error').html('');
        $('#file-type-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;File type is required</strong></small>");
        file_type_flag = true;
    } else {
        $('#file-type-error').addClass('d-none');
        file_type_flag = false;
    }


    let content = document.getElementById('content').files[0];
    if (typeof content != 'undefined') {
        $('#content-error').addClass('d-none');
        $('#content-error').html('');
        content_flag = false;
    } else {
        $('#content-error').removeClass('d-none');
        $('#content-error').html('');
        $('#content-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Study material is required</strong></small>");
        content_flag = true;
    }


    if(file_type_flag == true || content_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("file_type_id", file_type_id);

        let content = document.getElementById('content').files[0];
        if (typeof content != 'undefined') {
            formdata.append('content', content, content['name']);
        }
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        var url = window.location.href;
        var urlSplit = url.split('/');
        var res1 = urlSplit[urlSplit.length - 1];
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "/study-material-management/edit-study-material/"+res1,
            headers: { 'X-CSRFToken': csrftoken },
            data: formdata,
            cache: false,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            success: function (response) {
                console.log(response['response']);

                if (response['message'] == 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: 'Study material updated successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                } else {
                    alert('An Error occured while adding updating study material. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }

}