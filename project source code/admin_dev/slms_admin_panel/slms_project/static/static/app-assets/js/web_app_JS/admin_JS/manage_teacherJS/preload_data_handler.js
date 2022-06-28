var branchID = localStorage.getItem("branchID");
var class_section_subject_detail = eval(localStorage.getItem("class_section_subject_detail"));
var classTeacher = localStorage.getItem("classTeacher");
// ###############################################################################################################################################
console.log('branchID >>> ', branchID);
console.log('class_section_subject_detail >>> ', class_section_subject_detail, typeof (class_section_subject_detail));
console.log('classTeacher >>> ', classTeacher);
// ##############################################################################################################################################
var rowData = '';
var row_counter = class_section_subject_detail.length;
console.log('rowData >>> ', rowData);
console.log('row_counter >>> ', row_counter);
var class_Str = '<option value="" class="d-none">Select Class</option>';
var section_Str = '<option value="" class="d-none">Select Section</option>';
var subject_Str = '<option value="" class="d-none">Select Subject</option>';
var rowDataStr = '';
// ###############################################################################################################################################
// prefetch_teacher_data
var classArray = [];

$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: "/manage/add-teacher-get-class",
        data: { 'branchID': branchID },
        success: function (response) {
            Swal.close();
            var counter = 1;
            for (var i = 0; i < row_counter; i++) {
                console.log('i > ', i);
                class_Str = '<option value="" class="d-none">Select Class</option>';
                for (var j = 0; j < response['classList'].length; j++) {
                    var class_rowData = '<option value="' + response['classList'][j]['id'] + '">' + response['classList'][j]['class_name'] + '</option>';
                    class_Str = class_Str + class_rowData;
                }

                // $('#classTeacher_class').html('');
                // $('#classTeacher_class').append(class_rowData);
                // ============= 2nd ajax call ====================
                $.ajax({
                    type: 'GET',
                    url: "/manage/get-subject-and-section",
                    data: { 'classID': class_section_subject_detail[i][0] },
                    success: function (response) {
                        Swal.close();
                        console.log('response >> ',response);
                        section_Str = '';
                        section_Str = "<option class='d-none' value=''>Select Section </option>";
                        subject_Str = '';
                        subject_Str = "<option class='d-none' value=''>Select Subject </option>";
                        if (response['sectionList'].length > 0) {
                            for (var k = 0; k < response['sectionList'].length; k++) {
                                var dataStr = '<option value="' + response['sectionList'][k]['id'] + '">' + response['sectionList'][k]['section_name'] + '</option>';
                                section_Str = section_Str + dataStr;
                            }
                            
                            for (var l = 0; l < response['subjectList'].length; l++) {
                                var dataStr = '<option value="' + response['subjectList'][l]['id'] + '">' + response['subjectList'][l]['subject_name'] + '</option>';
                                subject_Str = subject_Str + dataStr;
                            }
                        }
                        // $('#classTeacher_section').html('');
                        // $('#classTeacher_section').append(section_Str);
                        
                        // ================================================
                        if (counter == 1) {
                            $("#more-classes").append('<div class=row><div class="pt-1 col-md-3 form-group"><select class="form-control row-class" id="row_' + (counter) + '_class"  onchange="get_subject_and_sections(this)">' + class_Str + '</select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-section" id="row_' + (counter) + '_section">' + section_Str + '</select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-subject" id="row_' + (counter) + '_subject">' + subject_Str + '</select></div><div class="pt-1 col-lg-3 text-right"><a style="margin-top:5px" class="btn btn-purple add-class  btn-sm " href="javascript:;"   ><i class="fa fa-plus"></i></a> </div></div>');

                            $('#row_' + (counter) + '_class').val(class_section_subject_detail[counter-1][0]);
                            $('#row_' + (counter) + '_section').val(class_section_subject_detail[counter-1][1]);
                            $('#row_' + (counter) + '_subject').val(class_section_subject_detail[counter-1][2]);
                        } else {
                            $("#more-classes").append('<div class=row><div class="pt-1 col-md-3 form-group"><select class="form-control row-class" id="row_' + (counter) + '_class"  onchange="get_subject_and_sections(this)">' + class_Str + '</select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-section" id="row_' + (counter) + '_section">' + section_Str + '</select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-subject" id="row_' + (counter) + '_subject">' + subject_Str + '</select></div><div class="pt-1 col-lg-3 text-right"><a style="margin-top:5px" class="btn btn-danger remove-class  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a> </div></div>');

                            $('#row_' + (counter) + '_class').val(class_section_subject_detail[counter-1][0]);
                            $('#row_' + (counter) + '_section').val(class_section_subject_detail[counter-1][1]);
                            $('#row_' + (counter) + '_subject').val(class_section_subject_detail[counter-1][2]);
                        }
                    }
                }).then(function () {
                    counter = counter +1;
                    console.log('counter >>> ',counter);
                    // $('#row_' + (counter-1) + '_class').val(class_section_subject_detail[i][0]);
                })
            }
        }
    })
});
// ###############################################################################################################################################
// add class to teacher
var counter = row_counter;
$('.add-class').click(function () {
    $("#more-classes").append('<div class=row><div class="pt-1 col-md-3 form-group"><select class="form-control row-class" id="row_' + counter + '_class"  onchange="get_subject_and_sections(this)">' + class_Str + '</select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-section" id="row_' + counter + '_section"><option class="d-none" value="">Select Section </option></select></div><div class="pt-1 col-md-3 form-group"><select class="form-control row-subject" id="row_' + counter + '_subject"><option class="d-none" value="">Select ubject </option></select></div><div class="pt-1 col-lg-3 text-right"><a style="margin-top:5px" class="btn btn-danger remove-class  btn-sm " href="javascript:;"><i class="fa fa-minus"></i></a> </div></div>');
    counter = counter + 1;
});

$(document).on('click', '.remove-class', function () {
    $(this).parent().parent().remove();
    counter = counter - 1;
});
// ###############################################################################################################################################

// $('.row-class').each(function () {
//     classArray.push($(this).attr('id'));
// });
console.log(classArray);