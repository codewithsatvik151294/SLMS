// get paper details from examID
function getExam(thisTxt) {
    $.ajax({
        type: 'GET',
        url: "/approval-management/fetch-exam",
        data: { 'examID': $(thisTxt).attr('exam_id').trim() },
        success: function (response) {
            // Swal.close();
            console.log(response);
            $('#exam-id').html('');
            $('#exam-id').html(response['examDict']['exam_id']);

            $('#exam-name').html('');
            $('#exam-name').html(response['examDict']['exam_name']);

            $('#exam-branch').html('');
            $('#exam-branch').html(response['examDict']['branch_FK']);

            $('#exam-paper').html('');
            $('#exam-paper').html(response['examDict']['total_papers']);

            $('#exam-type').html('');
            $('#exam-type').html(response['examDict']['exam_type']);

            $('#exam-class').html('');
            $('#exam-class').html(response['examDict']['class']);

            var dataStr = '';
            for(var i=0;i<response['paperList'].length;i++){
                var data = '<tr>\
                                <td>'+response['paperList'][i]['paper_name']+'</td>\
                                <td>'+response['paperList'][i]['subject']+'</td>\
                                <td>'+response['paperList'][i]['start']+'</td>\
                                <td>'+response['paperList'][i]['end']+'</td>\
                                <td>'+response['paperList'][i]['proctor']+'</td>\
                            </tr>';
                dataStr = dataStr + data;
            }
            $('#paper-data').html('');
            $('#paper-data').append(dataStr);
        }
    });
}