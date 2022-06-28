// filter_attendance
function filter_attendance(thisTxt){
    var student_id = $(thisTxt).attr('student_id').trim();
    var year = $('#reg_year').text().trim();
    // ---------------  AJAX CALL  ----------------------------
        // Swal.showLoading();
        $.ajax({
            type: 'GET',
            url: "/attendance-management/filter-student-monthwise",
            data: {"student_id":student_id,"year":year,"month":$(thisTxt).val().trim()},
            success: function (response) {
                // Swal.close();
                console.log('response >>> ',response['response']);

                if(response['response'].length == 0){
                    var table_data = '<thead>\
                                            <tr>\
                                            <th>S. No.</th>\
                                            <th>Date</th>\
                                            <th width="300"> Perform Action</th>\
                                            </tr>\
                                        </thead>\
                                        <tbody></tbody>';
                            
                    $('#example2').DataTable().destroy();
                    $('#example2').html('');
                    $('#example2').append(table_data);
                    $('#example2').DataTable({
                        searching: false,
                        paging: false,
                    });
                    return false;
                }
                else{
                    var dataStr = '';
                    for(var i=0;i<response['response'].length;i++){

                        var actionData = '';
                        if(response['response'][i]['attendance_status'] == '1'){
                            actionData = '<td>\
                                                <div class="demo-radio-button" id="check_'+(i+1)+'">\
                                                <label> <input name="atten_'+(i+1)+'" id="attendance_present_status_'+(i+1)+'" checked type="radio"  class="radio-col-success">\
                                                    <span>Present </span>\
                                                </label>\
                                                <label class="ml-5">\
                                                    <input name="atten_'+(i+1)+'" id="attendance_absent_status_'+(i+1)+'" type="radio"   class="radio-col-danger">\
                                                    <span>Absent</span>\
                                                </label>\
                                                </div>\
                                            </td>';
                        }else{
                            actionData = '<td>\
                                                <div class="demo-radio-button" id="check_'+(i+1)+'">\
                                                <label> <input name="atten_'+(i+1)+'" id="attendance_present_status_'+(i+1)+'" type="radio"  class="radio-col-success">\
                                                    <span>Present </span>\
                                                </label>\
                                                <label class="ml-5">\
                                                    <input name="atten_'+(i+1)+'" id="attendance_absent_status_'+(i+1)+'" checked type="radio"   class="radio-col-danger">\
                                                    <span>Absent</span>\
                                                </label>\
                                                </div>\
                                            </td>';
                        }
                        var data = '<tr> \
                                        <td><strong>'+(i+1)+'</strong></td>\
                                        <td class="text-secondary"><strong>'+response['response'][i]['date']+'</strong></td>'+actionData+'\
                                    </tr>';
                                    dataStr = dataStr + data;
                                }
                    var table_data = '<thead>\
                                            <tr>\
                                            <th>S. No.</th>\
                                            <th>Date</th>\
                                            <th width="300"> Perform Action</th>\
                                            </tr>\
                                        </thead>\
                                        <tbody>'+ dataStr + '</tbody>';
                            
                    $('#example2').DataTable().destroy();
                    $('#example2').html('');
                    $('#example2').append(table_data);
                    $('#example2').DataTable({
                        searching: true,
                        paging: true,
                    });
                            
                }
            }
        });
        // --------------------------------------------------------
}