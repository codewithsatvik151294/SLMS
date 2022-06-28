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
var title_flag = false;
var trigger_flag = false;
var image_flag = false;
var description_flag = false;

// global variables
var title = '';
var trigger = '';
var description = '';


// add new badge
function add_badge(){
    title = $('#badge-title').val().trim();
    trigger = $('#badge-trigger').val().trim();
    description = $('#bagde-description').val().trim();

    // field validation
    if (title == '') {
        $('#badge-title-error').removeClass('d-none');
        $('#badge-title-error').html('');
        $('#badge-title-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Badge title is required</strong></small>");
        title_flag = true;
    } else {
        $('#badge-title-error').addClass('d-none');
        title_flag = false;
    }

    if (title.length < 3) {
        $('#badge-title-error').removeClass('d-none');
        $('#badge-title-error').html('');
        $('#badge-title-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Badge title must be minimum of 4 characters</strong></small>");
        title_flag = true;
    } else {
        $('#badge-title-error').addClass('d-none');
        title_flag = false;
    }

    if (trigger == '') {
        $('#badge-trigger-error').removeClass('d-none');
        $('#badge-trigger-error').html('');
        $('#badge-trigger-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Badge trigger is required</strong></small>");
        trigger_flag = true;
    } else {
        $('#badge-trigger-error').addClass('d-none');
        trigger_flag = false;
    }

    if (description == '') {
        $('#bagde-description-error').removeClass('d-none');
        $('#bagde-description-error').html('');
        $('#bagde-description-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Badge description is required</strong></small>");
        description_flag = true;
    } else {
        $('#bagde-description-error').addClass('d-none');
        description_flag = false;
    }

    if (description == '') {
        $('#bagde-description-error').removeClass('d-none');
        $('#bagde-description-error').html('');
        $('#bagde-description-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Badge description  must be minimum of 10 characters</strong></small>");
        description_flag = true;
    } else {
        $('#bagde-description-error').addClass('d-none');
        description_flag = false;
    }


    let image = document.getElementById('badge').files[0];
    if (typeof image != 'undefined') {
        $('#bagde-image-error').addClass('d-none');
        $('#bagde-image-error').html('');
        image_flag = false;
    } else {
        $('#bagde-image-error').removeClass('d-none');
        $('#bagde-image-error').html('');
        $('#bagde-image-error').append("<small><strong> &nbsp;&nbsp;&nbsp;Badge image is required</strong></small>");
        image_flag = true;
    }

    if (title_flag == true || trigger_flag == true || image_flag == true || description == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("title", title);
        formdata.append("trigger", trigger);
        formdata.append("description", description);
    
        let myFileimg = document.getElementById('badge').files[0];
        if (typeof myFileimg != 'undefined') {
            formdata.append('image', myFileimg, myFileimg['name']);
        }
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-badge",
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
                        title: 'New badge added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        window.location.href = 'badge-list'
                    })
                }else{
                    alert('An Error occured while adding new badge. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }
}



// check title name
function check_title(thisTxt){
    if ($(thisTxt).val().trim() != '') {
        // ---------------  AJAX CALL  ----------------------------
        $.ajax({
            type: 'GET',
            url: "/badge-management/check-title",
            data: { 'search_string': $(thisTxt).val().trim() },
            success: function (response) {
                if (response['message'] == 'exist') {
                    $('#badge-title-error').removeClass('d-none');
                    $('#badge-title-error').html('');
                    $('#badge-title-error').append('<small><strong> Badge title already exist!</strong></small>');

                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                    title_flag = true;
                } else {
                    $('#badge-title-error').addClass('d-none');
                    $('#badge-title-error').html('');
                    
                    $('#submit_btn').css('pointer-events', '');
                    $('#submit_btn').css('opacity', '1');
                    title_flag = false;
                }

                // button enabled/disable
                if (title_flag == true || trigger_flag == true || image_flag == true || description == true) {
                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                } else {
                    $('#submit_btn').css('pointer-events', '');
                    $('#submit_btn').css('opacity', '1');
                }
            }

        });
        // --------------------------------------------------------

    }
}



// check badge_trigget
function check_trigger(thisTxt){
    if ($(thisTxt).val().trim() != '') {
        // ---------------  AJAX CALL  ----------------------------
        $.ajax({
            type: 'GET',
            url: "/badge-management/check-trigger",
            data: { 'search_string': $(thisTxt).val().trim() },
            success: function (response) {
                if (response['message'] == 'exist') {
                    $('#badge-trigger-error').removeClass('d-none');
                    $('#badge-trigger-error').html('');
                    $('#badge-trigger-error').append('<small><strong> Badge trigger already exist!</strong></small>');

                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                    trigger_flag = true;
                } else {
                    $('#badge-trigger-error').addClass('d-none');
                    $('#badge-trigger-error').html('');
                    
                    $('#submit_btn').css('pointer-events', '');
                    $('#submit_btn').css('opacity', '1');
                    trigger_flag = false;
                }

                // button enabled/disable
                if (title_flag == true || trigger_flag == true || image_flag == true || description == true) {
                    $('#submit_btn').css('pointer-events', 'none');
                    $('#submit_btn').css('opacity', '0.2');
                } else {
                    $('#submit_btn').css('pointer-events', '');
                    $('#submit_btn').css('opacity', '1');
                }
            }

        });
        // --------------------------------------------------------

    }
}