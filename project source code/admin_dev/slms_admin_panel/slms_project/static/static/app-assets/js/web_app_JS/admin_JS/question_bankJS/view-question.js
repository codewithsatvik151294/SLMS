// get question specific details
function get_question_detail(thisTxt) {
    $.ajax({
        type: 'GET',
        url: "/question-bank-management/view-question/"+$(thisTxt).attr('questionId').trim(),
        success: function (response) {
            $('#ClassModal').html('').append(response['question_dict']['class_name']);
            $('#SubjectModal').html('').append(response['question_dict']['subject_name']);
            $('#TopicModal').html('').append(response['question_dict']['topic_name']);
            $('#YearModal').html('').append(response['question_dict']['year_name']);
            $('#QuestionTypeMod').html('').append(response['question_dict']['question_type']);
            $('#QuestionSubTypeModal').html('').append(response['question_dict']['question_sub_type']);
            if(response['question_dict']['difficulty'] == '1'){
                $('#DifficultyModal').html('').append('Easy');
            }else if(response['question_dict']['difficulty'] == '2'){
                $('#DifficultyModal').html('').append('Moderate');
            }else{
                $('#DifficultyModal').html('').append('Hard');
            }
            $('#CorrectMarkModal').html('').append(response['question_dict']['correct_mark']);
            $('#NegativeMarkModal').html('').append(response['question_dict']['negative_mark']);
            $('#QuestionModal').html('').append(response['question_dict']['question_text']);

            if(parseInt(response['question_dict']['option_count']) > 1){
                var optionStr = '<label class="mb-1" style="font-size:15px;font-weight: 700;" id="optionModalAppend" >Options</label>';

                for(var i=0;i<response['question_dict']['option_array'].length;i++){
                    if(response['question_dict']['option_array'][i]['status'] == 'true'){
                        var data = '<p class="ml-1"><i style="color: green;font-size: large;font-weight: 600;" class="far fa-check-circle"></i>&nbsp;&nbsp;'+response['question_dict']['option_array'][i]['option'+(i+1)+'']+'</p>';
                    }else{
                        var data = '<p class="ml-1"><i style="color: red;font-size: large;font-weight: 600;" class="far fa-circle"></i>&nbsp;&nbsp;'+response['question_dict']['option_array'][i]['option'+(i+1)+'']+'</p>';
                    }
                    optionStr = optionStr + data;
                }
                $('#OptionModal').css('display','');
                $('#OptionModal').html('').append(optionStr);
            }else{
                $('#OptionModal').css('display','none');
                $('#OptionModal').html('').append('');
            }
            $('#edit-btn').attr('href','')
            $('#edit-btn').attr('href','/question-bank-management/edit-question/'+response['question_dict']['id']+'')
        }
    });
}