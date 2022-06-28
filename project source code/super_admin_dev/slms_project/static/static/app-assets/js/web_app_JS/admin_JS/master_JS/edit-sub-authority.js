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

var sub_auth = eval(localStorage.getItem("sub-auth"));
var splitedArray = sub_auth[0].split(',');
console.log('splitedArray >>> ',splitedArray);
// generate fields for sub-authorities
for (var i = 0;i < splitedArray.length;i++) {
    if(i==0){
        $('#first-sub-auth').val(splitedArray[i]);
    }else{
        $( "#sub-authority" ).append('<div class="row"><div class="col-lg-10 form-group mt-1">  <input class="form-control sub-auth-name" placeholder="Enter sub authority name" value="'+splitedArray[i]+'"></div><div class="text-right col-lg-2  pt-1" ><a style="margin-top:2px" class="btn btn-danger remove-subauth  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');
    }
}

// ##############################################################################

var sub_authority_name_flag = false;

// add new authority
function update_sub_authority() {
    // field validation
    var sub_auth_array = [];

    $('.sub-auth-name').each(function () {
        sub_auth_array.push($(this).val());
        if ($(this).val().trim() == '') {
            $(this).css('border', '1px solid red');
            $('#sub-authority-name-error').removeClass('d-none');
            $('#sub-authority-name-error').html('');
            $('#sub-authority-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Sub authority name is required</strong></small>");
            sub_authority_name_flag = true;
        } else {
            $(this).css('border', '');
            $('#sub-authority-name-error').addClass('d-none');
            sub_authority_name_flag = false;
        }
    });

    if (sub_authority_name_flag == true) {
        return false;
    } else {
        var formdata = new FormData();
        formdata.append("sub_auth_array[]", sub_auth_array);
        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        var url = window.location.href;
        var urlSplit = url.split('/');
        var res1 = urlSplit[urlSplit.length - 1];
        $.ajax({
            type: 'POST',
            url: "/master/edit-sub-authority/"+res1,
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
                        title: 'Sub authority updated successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else {
                    alert('An Error occured while updating sub authority. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}


$(document).on('click', '.add-sub-auth', function(){
   $( "#sub-authority" ).append('<div class="row"><div class="col-lg-10 form-group mt-1">  <input class="form-control sub-auth-name" placeholder="Enter sub authority name" value=""></div><div class="text-right col-lg-2  pt-1" ><a style="margin-top:2px" class="btn btn-danger remove-subauth  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');
  });

$(document).on('click','.remove-subauth', function(){ 
	 $(this).parent().parent('.row').remove();
	  
 });