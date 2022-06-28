// global variable & global flags
var branch = '';
var branch_flag = false;

var session = '';
var session_flag = false;

var year = '';
var year_flag = false;

var effective_from = '';
var effective_from_flag = false;

var class_id = '';
var class_flag = false;

var section_id = '';
var section_flag = false;


// filter_time_table
function filter_time_table(){
    branch = $('#branch-id').val().trim();
    session = $('#session-id').val().trim();
    year = $('#year-id').val().trim();
    effective_from = $('#effective-id').val().trim();
    class_id = $('#class-id').val().trim();
    section_id = $('#section-id').val().trim();

    // field validation
    if (branch == '') {
        $('#branch-error').removeClass('d-none');
        $('#branch-error').html('');
        $('#branch-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Branch is required</strong></small>");
        branch_flag = true;
    } else {
        $('#branch-error').addClass('d-none');
        branch_flag = false;
    }

    if (session == '') {
        $('#session-error').removeClass('d-none');
        $('#session-error').html('');
        $('#session-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Session is required</strong></small>");
        session_flag = true;
    } else {
        $('#session-error').addClass('d-none');
        session_flag = false;
    }

    if (year == '') {
        $('#year-error').removeClass('d-none');
        $('#year-error').html('');
        $('#year-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Year is required</strong></small>");
        year_flag = true;
    } else {
        $('#branch-error').addClass('d-none');
        year_flag = false;
    }

    if (effective_from == '') {
        $('#effective-error').removeClass('d-none');
        $('#effective-error').html('');
        $('#effective-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Effective month is required</strong></small>");
        effective_from_flag = true;
    } else {
        $('#effective-error').addClass('d-none');
        effective_from_flag = false;
    }

    if (class_id == '') {
        $('#class-error').removeClass('d-none');
        $('#class-error').html('');
        $('#class-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Class is required</strong></small>");
        class_flag = true;
    } else {
        $('#class-error').addClass('d-none');
        class_flag = false;
    }

    if (section_id == '') {
        $('#section-error').removeClass('d-none');
        $('#section-error').html('');
        $('#section-error').append("<small><strong>&nbsp;&nbsp;&nbsp;Section is required</strong></small>");
        section_flag = true;
    } else {
        $('#section-error').addClass('d-none');
        section_flag = false;
    }

    
    if(branch_flag == true || session_flag == true || year_flag == true || effective_from_flag == true || class_flag == true || section_flag == true){
        return false;
    }else{
        var formdata = new FormData();
        formdata.append("branchId", branch);
        formdata.append("session", session);
        formdata.append("year_id", year);
        formdata.append("effective_from", effective_from);
        formdata.append("class_id", class_id);
        formdata.append("section_id", section_id);
        // ---------------  AJAX CALL  ----------------------------
        // Swal.showLoading();
        $.ajax({
            type: 'GET',
            url: "/time-table-management/filter-time-table",
            data: {"branchId":branch,"session":session,"year_id":year,"effective_from":effective_from,"class_id":class_id,"section_id":section_id},
            success: function (response) {
                // Swal.close();
                console.log('response >>> ',response['response']);
                if(response['response'].length == 0){
                    $('#tt-param-text').css('display','');
                    $('#tt-table').css('display','none');
                    $('#tt-param-text').html('');
                    $('#tt-param-text').append('No Time Table Available!');
                    return false;
                }else{

                    console.log('response >>> ',response['response'][0]['slots_count']);
                    console.log(response['response'][0]['monday_slot']);

                    var dataStr = '';
                    var colorArray = ['success','danger','primary','secondary','warning','info','dark']
                    for(var i=0;i<response['response'][0]['slots_count'];i++){
                        var data = '<tr>\
                                        <td>'+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['startAt']+' to '+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['endAt']+'</td>\
                                        <td> <i class="d-block text-'+colorArray[i]+'">'+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['teacher_name']+'</i>\
                                        <span class="d-block">'+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['subject_name']+'</span>\
                                        </td>\
                                        <td> <i class="d-block text-'+colorArray[i]+'">'+response['response'][0]['tuesday_slot']['slot_'+(i+1)+'']['teacher_name']+'</i>\
                                        <span class="d-block">'+response['response'][0]['tuesday_slot']['slot_'+(i+1)+'']['subject_name']+'</span>\
                                        </td>\
                                        <td> <i class="d-block text-'+colorArray[i]+'">'+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['teacher_name']+'</i>\
                                        <span class="d-block">'+response['response'][0]['wednesday_slot']['slot_'+(i+1)+'']['subject_name']+'</span>\
                                        </td>\
                                        <td> <i class="d-block text-'+colorArray[i]+'">'+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['teacher_name']+'</i>\
                                        <span class="d-block">'+response['response'][0]['thursday_slot']['slot_'+(i+1)+'']['subject_name']+'</span>\
                                        </td>\
                                        <td> <i class="d-block text-'+colorArray[i]+'">'+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['teacher_name']+'</i>\
                                        <span class="d-block">'+response['response'][0]['friday_slot']['slot_'+(i+1)+'']['subject_name']+'</span>\
                                        </td>\
                                        <td> <i class="d-block text-'+colorArray[i]+'">'+response['response'][0]['monday_slot']['slot_'+(i+1)+'']['teacher_name']+'</i>\
                                        <span class="d-block">'+response['response'][0]['saturday_slot']['slot_'+(i+1)+'']['subject_name']+'</span>\
                                        </td>\
                                    </tr>';
                                    dataStr = dataStr + data;
                                }
                    $('#tt-param-text').css('display','none');
                    $('#tt-table').css('display','');
                    $('#tt-append-list').html('');
                    $('#tt-append-list').append(dataStr);
                            
                }
            }
        });
        // --------------------------------------------------------
    }
}