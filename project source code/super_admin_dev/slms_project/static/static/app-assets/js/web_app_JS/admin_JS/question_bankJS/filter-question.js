// filter questions with paramenters
function filter_question(){
    alert('Under development!');
    return false;
    var year_filter = $('#year-filter').val();
    // ==================================  AJAX CALL  ========================================
    $.ajax({
        type: 'GET',
        url: "/question-bank-management/filter-question",
        data : {'year_filter' : year_filter},
        success: function (response) {
            console.log('response >>> ',response['data_list']);

            var dataStr = '';
            for(var i=0;i<response['data_list'.length];i++){
                var data = '<tr> \
                <td width="700px;">'+response['data_list'.length][i]['question_text']+'</td>\
                <td>'+response['data_list'.length][i]['question_type']+'</td>\
                <td>'+response['data_list'.length][i]['difficulty']+'\
                                </td>\
                                <td>'+response['data_list'.length][i]['correct_mark']+'</td>\
                                <td>'+response['data_list'.length][i]['subject_name']+'</td>\
                                <td>'+response['data_list'.length][i]['topic_name']+'</td>\
                                <td>'+response['data_list'.length][i]['year_name']+'</td>\
                                <td class="details-control">\
                                <a onclick="get_question_detail(this)" questionId="'+response['data_list'.length][i]['id']+'" class="view" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i></a>\
                                <a href="edit-question.php" class="edit "><i class="fa fa-edit"></i></a>\
                                <a href="javascript:;" class="del "><i class="fa fa-trash"></i></a>\
                                </td>\
                                </tr>';
                dataStr = dataStr + data;
            }
                var table_data_string = '<thead>\
                                            <tr>\
                                            <th>Question</th>\
                                            <th>Qtype</th>\
                                            <th>Difficulty</th>\
                                            <th>Marks</th>\
                                            <th>Subject</th>\
                                            <th>Topic</th>\
                                            <th>Year</th>\
                                            <th class="text-center">Action</th>\
                                            </tr>\
                                        </thead><tbody>'+dataStr+'</tbody>';

            $("#example").DataTable().destroy();

            $("#example").DataTable();
            $("#example").html('');
            $("#example").append(table_data_string);
        }
    });
    // ==========================================================================================
}