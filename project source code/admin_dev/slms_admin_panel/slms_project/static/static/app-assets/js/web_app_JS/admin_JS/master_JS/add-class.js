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


// global flags
var branch_flag = false;
var className_flag = false;
var subject_flag = false;
var section_flag = false;
var class_type_flag = false;

// global variables
var section_data = '<option class="d-none" value="">Select Section</option>';
var class_type_data = '<option class="d-none" value="">Select Class Type</option>';
var counter = 0;
// add new class
function add_new_class(){
    var branch = $('#default-select').val().trim();
    var class_name = $('#class-name').val().trim();
    var subject_array = $('#class-subject').val();
    var class_description = $('#class-description').val();
    var section_array = [];
    var class_type_array = [];

    // branch field validation
    if (branch == '') {
        $('#class-branch-error').removeClass('d-none');
        $('#class-branch-error').html('');
        $('#class-branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#class-branch-error').addClass('d-none');
        branch_flag = false;
    }


    // class_name field validation
    if (class_name == '') {
        $('#class-name-error').removeClass('d-none');
        $('#class-name-error').html('');
        $('#class-name-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Class name is required</strong></small>");
        className_flag = true;
    } else {
        $('#class-name-error').addClass('d-none');
        className_flag = false;
    }


    // subject_array field validation
    if (subject_array.length == 0) {
        $('#class-subject-error').removeClass('d-none');
        $('#class-subject-error').html('');
        $('#class-subject-error').append("<small><strong>&nbsp;&nbsp;&nbsp;&nbsp;Subjects is/are required</strong></small>");
        subject_flag = true;
    } else {
        $('#class-subject-error').addClass('d-none');
        subject_flag = false;
    }

    $('.section-data').each(function () { 
        section_array.push($(this).val());
        if($(this).val().trim() == ''){
            $(this).css('border','1px solid red');
            section_flag = true;
        }else{
            $(this).css('border','');
            section_flag = false;
        }
    });
    console.log(section_array);

    $('.class-type-data').each(function () { 
        class_type_array.push($(this).val());
        if($(this).val().trim() == ''){
            $(this).css('border','1px solid red');
            class_type_flag = true;
        }else{
            $(this).css('border','');
            class_type_flag = false;
        }
    });
    console.log(class_type_array);

    if(branch_flag == true || className_flag == true || subject_flag == true || section_flag == true || class_type_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("branch", branch);
        formdata.append("class_name", class_name);
        formdata.append("subject_array[]", subject_array);
        formdata.append("section_array[]", section_array);
        formdata.append("class_type_array[]", class_type_array);
        formdata.append("class_description", class_description);

        // ---------------  AJAX CALL  ----------------------------
        Swal.showLoading();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            type: 'POST',
            url: "add-class",
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
                        title: 'New class added successfully.',
                        showConfirmButton: false,
                        timer: 2000
                    }).then(function () {
                        location.reload();
                    })
                }else if(response['message'] == 'Class already exist'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Class for selected branch already exist.',
                        showConfirmButton: false,
                        timer: 3000
                    }).then(function () {
                        $('#classTeacher_class').css('border','2px solid red');
                        $('#classTeacher_section').css('border','2px solid red');
                    })
                }else{
                    alert('An Error occured while adding new class. Please try again!');
                    return false;
                }
            }
        });
        // --------------------------------------------------------
    }


}


// get sections and class_type
// function get_sections_class_type(){
//     if(counter == 0){

//         // ======================================================
//         $.ajax({
//             type: 'GET',
//             url: "get-section-and-class-type",
//             success: function (response) {
//                 console.log(response);
//                 for(var i=0;i<response['sectionData'].length;i++){
//                     section_data = section_data + '<option value="'+response['sectionData'][i]['id']+'">'+response['sectionData'][i]['section_name']+'</option>';
//                 }
//                 for(var i=0;i<response['class_typeData'].length;i++){
//                     class_type_data = class_type_data + '<option value="'+response['class_typeData'][i]['id']+'">'+response['class_typeData'][i]['class_type_name']+'</option>';
//                 }
//         }
//     });
//     // ======================================================
//         counter = counter + 1;
//     }
// }


// add sections

$(document).on('click', '.add-sections', function(){
    // if(counter == 0){

        // ======================================================
        $.ajax({
            type: 'GET',
            url: "get-section-and-class-type",
            success: function (response) {
                section_data = '<option class="d-none" value="">Select Section</option>';
                class_type_data = '<option class="d-none" value="">Select Class Type</option>';
                console.log(response);
                for(var i=0;i<response['sectionData'].length;i++){
                    section_data = section_data + '<option value="'+response['sectionData'][i]['id']+'">'+response['sectionData'][i]['section_name']+'</option>';
                }
                for(var i=0;i<response['class_typeData'].length;i++){
                    class_type_data = class_type_data + '<option value="'+response['class_typeData'][i]['id']+'">'+response['class_typeData'][i]['class_type_name']+'</option>';
                }
            $( "#more-sections" ).append('<div class="row"> <div class="col-lg-3 no-ico form-group"> <label>Section </label> <select class="form-control section-data">'+section_data+'</select> </div><div class="col-lg-4 no-ico form-group"> <label>Class Type</label> <select class="form-control class-type-data">'+class_type_data+'</select> </div><div class=" col-lg-2 pt-2"><a style="margin-top:5px" class="btn btn-danger remove-section  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');
        }
    });
    // ======================================================
    //     counter = counter + 1;
    // }

 
        
   });
 
 $(document).on('click','.remove-section', function(){ 
      $(this).parent().parent('.row').remove();
  });