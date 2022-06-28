$( window ).scroll(function() {
	if($(this).scrollTop() > 60) {
      $( ".navbar" ).removeClass('transparent');
    }
    else {$( ".navbar" ).addClass('transparent');}
});

$('.menu-toggle').click(function(){
	 // $( ".navbar.transparent" ).addClass('transparent');
	$('.content-wrapper-before').toggleClass('full');
});
$('.table tr td .del').click(function(){
	 // $( ".navbar.transparent" ).addClass('transparent');
	$('#alert').modal('show');
});


 
 // for dashboard only
var href = document.location.href;
var pageName = href.substr(href.lastIndexOf('/') + 1);
 if(pageName=="dashboard.php"){
 	  $('.navbar').addClass('transparent');
 	  $('.content-wrapper-before').show();
 }
 else { 
 	$('.content-wrapper-before').hide(); 
	   $( window ).scroll(function() {
	      $( ".navbar" ).removeClass('transparent');
	});
}


$('#process').change(function(){
  	$('.card.info').show();
  	$(".other option[value=1]").attr('selected', 'selected');
  	$("html, body").animate({ scrollTop: 400 }, "medium");
    return false;
});

$('#example2 .add').click(function(){
	$('#add_batches span.watermark').hide();
	  $('#add_batches').append('<div class="batch card"><ul><li> <span>Batch ID</span>BID001</li><li> <span>Batch Name</span>CSIIA</li><li> <a href="javascript:;" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#add-paper">Select Paper(s)</a> <a href="#" data-toggle="tooltip" data-placement="top" title="Add students"><img src="../app-assets/images/addstudent.svg"></a> <a href="#" id="delete" data-toggle="tooltip" data-placement="top" title="Delete Batch"><img src="../app-assets/images/delete.svg"></a></li></ul></div>');
});

	

$('.add_seld').click(function(){
	if($('#example2 tr td').find('input[type=checkbox]').prop("checked") == true){
	  $('#add_batches').append('<div class="batch card"><ul><li> <span>Batch ID</span>BID001</li><li> <span>Batch Name</span>CSIIA</li><li> <a href="javascript:;" class="btn btn-primary btn-sm">Select Paper(s)</a> <a href="#" data-toggle="tooltip" data-placement="top" title="Add students"><img src="../app-assets/images/addstudent.svg"></a> <a href="#" id="delete" data-toggle="tooltip" data-placement="top" title="Delete Batch"><img src="../app-assets/images/delete.svg"></a></li></ul></div><div class="batch card"><ul><li> <span>Batch ID</span>BID001</li><li> <span>Batch Name</span>CSIIA</li><li> <a href="javascript:;" class="btn btn-primary btn-sm">Select Paper(s)</a> <a href="#" data-toggle="tooltip" data-placement="top" title="Add students"><img src="../app-assets/images/addstudent.svg"></a> <a href="#" id="delete" data-toggle="tooltip" data-placement="top" title="Delete Batch"><img src="../app-assets/images/delete.svg"></a></li></ul></div><div class="batch card"><ul><li> <span>Batch ID</span>BID001</li><li> <span>Batch Name</span>CSIIA</li><li> <a href="javascript:;" class="btn btn-primary btn-sm">Select Paper(s)</a> <a href="#" data-toggle="tooltip" data-placement="top" title="Add students"><img src="../app-assets/images/addstudent.svg"></a> <a href="#" id="delete" data-toggle="tooltip" data-placement="top" title="Delete Batch"><img src="../app-assets/images/delete.svg"></a></li></ul></div>');
	}
	else{alert('Please select one or more batches from table.');}
});

$('#example3 .add').click(function(){
	$('#add_papers span.watermark').hide();
	  $('#add_papers').append('<div class="batch card paper"><ul><li> <span>Paper ID</span>PID001</li> <li>  <a href="#" data-toggle="tooltip" data-placement="top" title="Edit paper"><img src="../app-assets/images/editing.svg"></a> <a href="#"  data-toggle="tooltip" data-placement="top" title="View Paper"><img src="../app-assets/images/view.svg"></a><a href="#"   data-toggle="tooltip" data-placement="top" title="Delete"><img src="../app-assets/images/delete.svg"></a><a href="create-exam-step-4.php" class="btn btn-primary btn-sm"  >Select Slot</a></li></ul></div>');
});

$('.add_seld_p').click(function(){
	if($('#example3 tr td').find('input[type=checkbox]').prop("checked") == true){
	  $('#add_papers').append('<div class="batch card paper"><ul><li> <span>Paper ID</span>PID001</li> <li>  <a href="#" data-toggle="tooltip" data-placement="top" title="Edit paper"><img src="../app-assets/images/editing.svg"></a> <a href="#"  data-toggle="tooltip" data-placement="top" title="View Paper"><img src="../app-assets/images/view.svg"></a><a href="#"   data-toggle="tooltip" data-placement="top" title="Delete"><img src="../app-assets/images/delete.svg"></a><a href="create-exam-step-4.php" class="btn btn-primary btn-sm"  >Select Slot</a></li></ul></div><div class="batch card paper"><ul><li> <span>Paper ID</span>PID001</li> <li>  <a href="#" data-toggle="tooltip" data-placement="top" title="Edit paper"><img src="../app-assets/images/editing.svg"></a> <a href="#"  data-toggle="tooltip" data-placement="top" title="View Paper"><img src="../app-assets/images/view.svg"></a><a href="#"   data-toggle="tooltip" data-placement="top" title="Delete"><img src="../app-assets/images/delete.svg"></a><a href="create-exam-step-4.php" class="btn btn-primary btn-sm" >Select Slot</a></li></ul></div><div class="batch card paper"><ul><li> <span>Paper ID</span>PID001</li> <li>  <a href="#" data-toggle="tooltip" data-placement="top" title="Edit paper"><img src="../app-assets/images/editing.svg"></a> <a href="#"  data-toggle="tooltip" data-placement="top" title="View Paper"><img src="../app-assets/images/view.svg"></a><a href="#"   data-toggle="tooltip" data-placement="top" title="Delete"><img src="../app-assets/images/delete.svg"></a><a href="create-exam-step-4.php" class="btn btn-primary btn-sm"  >Select Slot</a></li></ul></div>');
	}
	else{alert('Please select one or more batches from table.');}
});
 

 $( function() {
    $( ".datepicker" ).datepicker();
   // $('.timepicker').timepicker();
  } );

 $(document).ready(function(){
    $('input.timepicker').timepicker({});
});


$('.addmore').click(function(){
   $( "#add-more-slots" ).append('<div class="row position-relative "><a href="javascript:;" class="remove">x</a><div class="col-lg-2 mb-2 pr-0 form-group"> <label>Batch Slot</label> <select class="form-control"><option>1</option><option>2</option> </select></div><div class="col-lg-3 mb-2 pr-0 form-group"> <label>Lies From registration no.</label> <input type="text" placeholder="Enter Registration no" class="form-control "></div><div class="col-lg-3 mb-2 pr-0 form-group"> <label>To</label> <input type="text" placeholder="Enter Registration no" class="form-control "></div><div class="col-lg-2 mb-2 pr-0 form-group"> <label>Center No.</label> <input type="text" placeholder="Enter Center no" class="form-control "></div><div class="col-lg-2 mb-2 form-group"> <label>Room No.</label> <input type="text" placeholder="Enter Room no" class="form-control "></div></div>');
      $('.added-slots').show();
      $('.added-slots').append('<p><i class="fa fa-arrow-right"></i> The students from registration no. <strong>1254545</strong> to <strong>1254645</strong> will sit in Exam centre no. <strong>35</strong></p>');
});
$(document).on('click','.remove', function(){ 
	$(this).parent().remove();
	$('.added-slots').children().last().remove();
	var lenght = $('.added-slots').children().length;
	 if(lenght<1) {
 	    $('.added-slots').hide();
	 }
 });


$('#example2 .assign-resources').click(function(){
	$('#add_resources span.watermark').hide();
	  $('#add_resources').append('<div class="batch card resources"><div class="row"><div class="col-lg-6"><p><span>Faculty Name</span>Rajesh Kumar</p><p><span>Faculty Code</span>FCODE001</p></div><div class="col-lg-6"><p><span>Assigned Responsibilities</span> <em>Teacher</em> <em>Proctor</em> <em>Examiner</em></p></div></div></div>');
});
$('.add_sel_res').click(function(){
	if($('#example2 tr td').find('input[type=checkbox]').prop("checked") == true){
	$('#add_resources span.watermark').hide();
	  $('#add_resources').append('<div class="batch card resources"><div class="row"><div class="col-lg-6"><p><span>Faculty Name</span>Rajesh Kumar</p><p><span>Faculty Code</span>FCODE001</p></div><div class="col-lg-6"><p><span>Assigned Responsibilities</span> <em>Teacher</em> <em>Proctor</em> <em>Examiner</em></p></div></div></div><div class="batch card resources"><div class="row"><div class="col-lg-6"><p><span>Faculty Name</span>Rajesh Kumar</p><p><span>Faculty Code</span>FCODE001</p></div><div class="col-lg-6"><p><span>Assigned Responsibilities</span> <em>Teacher</em> <em>Proctor</em> <em>Examiner</em></p></div></div></div>');
	}
	else{alert('Please select one or more resources from table.');}
});

$(document).on('click','#add_resources p em', function(){ 
	$(this).remove();	 
});


$('.add-students').click(function(){
	 $('#students tbody tr.not-added').hide();
	 $('#students tbody').append('<tr><td>Amit Kumar</td><td>ST7867887</td><td>amit@gmail.com</td><td>8575856688</td><td>Male</td><td class="details-control"> <a href="javascript:;" class="del pt-0 mt-0"><i class="fa fa-trash"></i></a></td></tr>');
});
 
  $(document).on('click','#students .del', function(){  
	var lenght1 = $('#students tbody').children().length;
	$(this).parents('tr').remove();	 
	  if( lenght1<=2) { 
	 	$('#students tbody').append('<tr class="not-added"><td colspan="6" class="text-center">No student added</td></tr>');
	  }
  });

  $('.add-bacthes').click(function(){
	 $('#batchess tbody tr.not-added').hide();
	 $('#batchess tbody').append('<tr><td>BID001</td><td>Batch 1</td><td>Ankur Singh</td><td>65</td> <td class="details-control"> <a href="javascript:;" class="del pt-0 mt-0"><i class="fa fa-trash"></i></a></td></tr>');
});
 
  $(document).on('click','#batchess .del', function(){  
	var lenght1 = $('#batchess tbody').children().length;
	$(this).parents('tr').remove();	 
	  if( lenght1<=2) { 
	 	$('#batchess tbody').append('<tr class="not-added"><td colspan="6" class="text-center">No batches added</td></tr>');
	  }
	
  });

 $('.upload label input').change(function(e){ 
	var fileName = e.target.files[0].name;
	$('#file').show();
	$('#file').html(fileName);
});
 
$('.upload .btn-upload').click(function(){
	$(this).parent().hide();
	$('.col-assign').show();
	$('.sel_val_tbl th select').show();
});

$('#uploadF').click(function(){
	if($(this).prop("checked") == true){
		$('.manual-entry, .bottom-btn').hide();
		$('.upload-csv, .bottom-btn1').show();
	}

});
$('#manual').click(function(){
	if($(this).prop("checked") == true){
		$('.manual-entry, .bottom-btn').show();
		$('.upload-csv, .bottom-btn1').hide();
	} 
});


function readURL(input) {
	  if (input.files && input.files[0]) {
	    var reader = new FileReader();
	    reader.onload = function(e) {
	      $('#imgphoto').attr('src', e.target.result);
	    }
	    
	    reader.readAsDataURL(input.files[0]); // convert to base64 string
	  }
	}

	$("#stu_photo").change(function() {
	  readURL(this);
	});

	// function readURL(input) {
	//   if (input.files && input.files[0]) {
	//     var reader = new FileReader();
	    
	//     reader.onload = function(e) {
	//       $('#imgsign').attr('src', e.target.result);
	//     }
	    
	//     reader.readAsDataURL(input.files[0]); 
	//   }
	// }

	// $("#stu_sign").change(function() {
	//   readURL(this);
	// });



function myFunction() {
  var copyText = document.getElementById("link-box");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
  $('.msg').html('link copied!');
}

// $('#no-of-section').change(function(){
// 	alert()
// });
$(document).ready(function(){
	$('#no-of-section').on('input',function(e){
     $('#sections').show()
});
})


$('.sections input[type=radio]').on('click',function(e){
    if($(this).attr('value')=="yes"){
    	$(this).parents('td').find('.set-time-limit').show();
    }
    else {
    	$(this).parents('td').find('.set-time-limit').hide();
    }
});
// $('#sections .marks, #sections .qno').on('input',function(e){
//     var qno =  $('#sections .qno').val();
//     var marks =   $('#sections .marks').val();
//     var total = parseInt(qno) * parseInt(marks);
//     $(this).parent().parent().find('td .total_marks').val(total);	
// });
$('.timeL input[type=radio]').on('click',function(e){
    if($(this).attr('value')=="yes"){
    	$('table').find('.time_limit').show();
    }
    else {
    	$('table').find('.time_limit').hide();
    }
});
$('.ques_type table tr td #q_type').change(function(){ 
	 $(this).parent().parent().find('.last').html('<span class="q_type">Objective</span>');
});

$('.ques_type .add-more').click(function(){
	$('.ques_type table tbody').append('<tr><td> <select class="form-control"><option class="d-none">Select</option><option>Section A</option><option>Section B</option> </select></td><td> <select title="Select question" class="selectpicker d-block" multiple data-live-search="false"><option>1</option><option>2</option><option>3</option><option>4</option> </select></td><td> <select id="q_type" title="Select question type" class="selectpicker d-block" multiple data-live-search="false"><option>Objctive</option><option>fill in the Blanks</option><option>True/false</option> </select></td><td ><div class="last"></div></td></tr>');
	 $('select').selectpicker();
});

$('.set-creation input[type=radio][name=set]').on('click',function(e){
    if($(this).attr('value')=="yes"){
    	$('.set-creation .set-options').show();
    }
    else {
    	$('.set-creation .set-options').hide();
    }
});



 // $('#add-paper').modal('show');

 // roles section

 	$('#assign-roles .btn-dark').on('click',function(){ 
 		 	$('#assigned-roles').show();
 		 	$('#assign-roles').hide();
 	});
 		$('#assigned-roles .back, #assigned-roles .btn-dark').on('click',function(){ 
 		 	$('#assigned-roles').hide();
 		 	$('#assign-roles').show();
 	})
 

//  // add topics

//  $(document).on('click', '.add-topic', function(){
//    $( "#more-topics" ).append('<div class="row"><div class="col-lg-11 mt-0 form-group">  <input type="text" class="form-control" placeholder="Enter topic name" value="" /></div><div class="text-right col-lg-1  pt-0" ><a style="margin-top:2px" class="btn btn-danger remove-topic  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');
//        // $(this).remove();
//   });

// $(document).on('click','.remove-topic', function(){ 
// 	 $(this).parent().parent('.row').remove();
	  
// 	 //$(this).parents('.row').prev().find('.add-topic').show();
//  });

 // add sections

//  $(document).on('click', '.add-sections', function(){
//    $( "#more-sections" ).append('<div class="row"> <div class="col-lg-3 no-ico form-group"> <label>Section </label> <select class="  form-control  " > <option class="d-none">Select </option> <option value="1">Section A</option> <option value="2">Section B</option> </select> </div><div class="col-lg-4 no-ico form-group"> <label>Class Type</label> <select class="  form-control  " >  <option class="d-none">Select </option><option value="1">Batch-Morning</option> <option value="2">Batch-Evening</option> </select> </div><div class=" col-lg-2 pt-2"><a style="margin-top:5px" class="btn btn-danger remove-section  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');

       
//   });

// $(document).on('click','.remove-section', function(){ 
// 	 $(this).parent().parent('.row').remove();
// 	 // $(this).parent().parent('.row').last().find('.add-sections').show();
// 	 //$(this).parents('.row').prev().find('.add-topic').show();
//  });

// add class to teacher
// $('.add-class').click(function(){
//    $( "#more-classes" ).append('<div class=row><div class="pt-1 col-md-3 form-group"><select class=form-control><option class=d-none>Select Class<option value=1>Class 1<option value=2>Class 2<option value=3>Class 3</select></div><div class="pt-1 col-md-3 form-group"><select class=form-control><option class=d-none>Select Section<option value=1>Section A<option value=2>Section B<option value=3>Section C</select></div><div class="pt-1 col-md-3 form-group"><select class=form-control><option class=d-none>Select Subject<option value=1>Hindi<option value=2>English<option value=3>Maths</select></div><div class="pt-1 col-lg-3 text-right"><a style="margin-top:5px" class="btn btn-danger remove-class  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a> </div></div>');    
// });
// $(document).on('click','.remove-class', function(){ 
// 	$(this).parent().parent().remove();
	 
//  });
 
  $('.class-t input').change(function(){
 	 if($(this).is(':checked')){
 	 	 $('#class-teacher').show()
 	 }
 	 else {
 	 	 $('#class-teacher').hide()
 	 }
 });

 $('.sel_filters a').click(function(){
 	$(this).remove();
 });

  $('#option').change(function(){
 	 $('#options').show()
 })

  $('.accordion .card-header').click(function(){
  	  var val = $(this).attr('href');
  		$(val).toggle();
  });

    $('.question_modal  a.edit').click(function(){
  	  $(this).html('<i class="fa fa-check"></i> Added');
  	  $(this).addClass('added')
  });

    $('.question_modal  .add-to-paper').click(function(){
  	  // $('#collapseOne .add-ques-btn').hide();
  	   $('#collapseOne .added-ques').show();
  	   $("html, body").animate({scrollTop: 0}, 100);
  });

     $('.added-ques .del').click(function(){
  	   $(this).parent().parent().hide();
  	    
  });

	$('.addP').click(function(){
	       $(this).addClass('selected');
	        $(this).html('<i class="fa fa-check"></i> Selected')
	    	// $(this).parent().find('.delP').addClass('show');
	   });
	$('.delR').click(function(){
	       $(this).removeClass('show');
	        $(this).parent().find('.addP').html('+ Select')
	    	$(this).parent().find('.addP').removeClass('selected');
	   });

 $('.addEva').click(function(){
       
        if($(this).hasClass('selected'))
        {
        	$(this).removeClass('selected');
        $(this).html(' Select +');
          }
          else {
          	$(this).addClass('selected');
      		  $(this).html('<i class="fa fa-check"></i> Selected');
          }
    	 
   });

 $('.modal .save').click(function(){
 	 $('table tr#row1 td .select').html('Selected  (2)');
 	 $('table tr#row1').find('.select').addClass('selected');
  });

  $('.schedule-exam .btn').click(function(){

 	  if($(this).hasClass('editD'))
        {
    	 $(this).removeClass('editD');
    	 $(this).html('Update');
    	 $(this).removeClass('btn-primary');
    	 $(this).addClass('btn-success');
    	 $(this).parent().parent().find('input').removeClass('readonly');
    	 if($(this).parent().parent().find('.select').hasClass('selected')){
    	 	$(this).parent().parent().find('.select').addClass('editt');
    	 	$(this).parent().parent().find('.select').html('Edit Evaluator');
    	 }
    	 
       }
       else {
       	  $(this).parent().parent().find('input').addClass('readonly');
	 	  $(this).addClass('editD');
	 	  $(this).html('Edit');
       }

  });


$(document).ready(function() {
  $("#select2-placeholder12").select2({
    dropdownParent: $("#questions")
  });
});
 
  
 
  	     
$(document).ready(function(){

		//iterate through each textboxes and add keyup
		//handler to trigger sum event
		$(".marks_ob").each(function() {
			calculateSum();
			$(this).keyup(function(){
				calculateSum();
			});
		});


	});

	function calculateSum() {

		var sum = 0;
		//iterate through each textboxes and add the values
		$(".marks_ob").each(function() {

			//add only if the value is number
			if(!isNaN(this.value) && this.value.length!=0) {
				sum += parseInt(this.value);
			}

		});
		//.toFixed() method will roundoff the final sum to 2 decimal places
		$("#markss").html(sum);
	}
  

  // add authority

//  $(document).on('click', '.add-sub-auth', function(){
//    $( "#sub-authority" ).append('<div class="row"><div class="col-lg-10 form-group mt-1">  <input class=form-control placeholder="Enter sub authority name"></div><div class="text-right col-lg-2  pt-1" ><a style="margin-top:2px" class="btn btn-danger remove-subauth  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');
//        // $(this).remove();
//   });

// $(document).on('click','.remove-subauth', function(){ 
// 	 $(this).parent().parent('.row').remove();
//  });

$('.authority-table tr td:first-child input').click(function(){
	if($(this).is(':checked')){
	   $(this).parent().parent().parent().find('input[type=checkbox]').prop('checked', true);
	}
	else {
		$(this).parent().parent().parent().find('input[type=checkbox]').prop('checked', false);
	}
});
$('.authority-table tr td.opt input').click(function(){
	var checkedNum = $('input[name="opt[]"]:checked').length;
	if($(this).is(':checked')){
	  $(this).parent().parent().parent().find('td:first-child input[type=checkbox]').prop('checked', true);
	}
	else if(checkedNum<=0){ 
	  $(this).parent().parent().parent().find('td:first-child input[type=checkbox]').prop('checked', false);
	}
});

$(document).on('click','.assign-sec input[type=radio]', function(){ 
	if($(this).attr('value')=="yes"){
    	$('#sectionss').show();
    }
    else {
    	$('#sectionss').hide();
    }
 });

 $('.publish').click(function(){
    $('#publish').modal('show')
 });

 function readMyURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#badge-img').attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#badge").change(function() {
  readMyURL(this);
});

// $('#btowhom').change(function(){
// 	if($(this).val()==2){
// 		 $('#broadcast_sel').show();
// 		 $('.select2').css('width','100%')
// 	}
// });
var v;
$('#bd-to').change(function(){
	  v= $(this).children("option:selected").val();
	   $("#btowhom").select2({
		    placeholder: "Select..",
		    allowClear: true
		});
	   $("#btowhom").val([])
});

$('#btowhom').change(function(){
 
		if(v==1 && $(this).val()==2){
			 $('#broadcast_sel').show();
	      	 $('.select2').css('width','100%');
	      	 $('#broadcast_sel_teacher').hide();

		}
		else if(v==2 && $(this).val()==2) {
			$('#broadcast_sel_teacher').show();
			 $('.select2').css('width','100%');
			 $('#broadcast_sel').hide();
		}
	  
});
 




 // add timetable
 $('.add-more-days').click(function(){ 

	// $('#add-days').append('<div class="row"><div class="col-lg-3 mb-1 form-group ">   <select class="select2 form-control select2-placeholder25" > <option value="1">Monday</option> <option value="2">Tuesday</option> <option value="3">Wednesday</option> </select> </div><div class="col-lg-3 mb-1 form-group "> <div class="row"> <div class="col-md-6">  <input type="text" placeholder="Select time" class="timepicker1 form-control" name=""> </div><div class="col-md-6 pl-0">  <input type="text" placeholder="Select time" class="timepicker1 form-control" name=""> </div></div></div><div class="col-lg-2 pr-0 mb-1 form-group ">   <select class="select2 form-control select2-placeholder8" >  <option value="1">Hindi</option> <option value="2">English</option> <option value="3">Maths</option> </select> </div><div class="col-lg-3 mb-1 form-group ">  <select class="select2 form-control select2-placeholder26" > <option value="1">Ram Singh</option> <option value="2">Amit Kumar</option> <option value="3">Renu Sharma</option> </select> </div><div class="text-right col-lg-1 " ><a style="margin-top:2px" class="btn btn-danger remove-subauth  btn-sm " href="javascript:;"   ><i class="fa fa-minus"></i></a>   </div></div>');
	var $tableBody = $('.t-table').find("tbody");
	$trLast = $tableBody.find("tr:last");
	$tableBody.append('<tr class="new-tr"> <td> <input type="text" placeholder="Select time" class="timepicker1 form-control" name="" placeholder="From"> <input type="text" placeholder="Select time" class="timepicker1 form-control " name="" placeholder="From"> </td><td> <select class="select2 form-control select2-placeholder8" > <option value="1">Hindi</option> <option value="2">English</option> <option value="3">Maths</option> </select> <span class="d-block sep"></span> <select class="select2 form-control select2-placeholder26" >> <option value="1">Ram Singh</option> <option value="2">Amit Kumar</option> <option value="3">Renu Sharma</option> </select> </td><td> <select class="select2 form-control select2-placeholder8" > <option value="1">Hindi</option> <option value="2">English</option> <option value="3">Maths</option> </select> <span class="d-block sep"></span> <select class="select2 form-control select2-placeholder26" ><option value="1">Ram Singh</option> <option value="2">Amit Kumar</option> <option value="3">Renu Sharma</option> </select> </td><td> <select class="select2 form-control select2-placeholder8" > <option value="1">Hindi</option> <option value="2">English</option> <option value="3">Maths</option> </select> <span class="d-block sep"></span> <select class="select2 form-control select2-placeholder26" ><option value="1">Ram Singh</option> <option value="2">Amit Kumar</option> <option value="3">Renu Sharma</option> </select> </td><td> <select class="select2 form-control select2-placeholder8" > <option value="1">Hindi</option> <option value="2">English</option> <option value="3">Maths</option> </select> <span class="d-block sep"></span> <select class="select2 form-control select2-placeholder26" > <option value="1">Ram Singh</option> <option value="2">Amit Kumar</option> <option value="3">Renu Sharma</option> </select> </td><td> <select class="select2 form-control select2-placeholder8" > <option value="1">Hindi</option> <option value="2">English</option> <option value="3">Maths</option> </select> <span class="d-block sep"></span> <select class="select2 form-control select2-placeholder26" > <option value="1">Ram Singh</option> <option value="2">Amit Kumar</option> <option value="3">Renu Sharma</option> </select> </td><td> <select class="select2 form-control select2-placeholder8" > <option value="1">Hindi</option> <option value="2">English</option> <option value="3">Maths</option> </select> <span class="d-block sep"></span> <select class="select2 form-control select2-placeholder26" > <option value="1">Ram Singh</option> <option value="2">Amit Kumar</option> <option value="3">Renu Sharma</option> </select> </td></tr>');
	 // $trNew = $trLast.clone();
	 // $trLast.after($trNew); 
	$('.timepicker1').timepicki();
	 $(".t-table tbody .new-tr td .select2").select2({
		  tags: true
	 });
	 $('.remove-days').show();
});

$('.remove-days').click(function(){ 
	 var $tableBody = $('.t-table').find("tbody");
	 $trLast = $tableBody.find("tr:last");
	 $trLength = $tableBody.find("tr.new-tr").length;
	 if($trLast.hasClass('new-tr')){
		 $trLast.remove();
	 }
	 if($trLength<=1){
		 $(this).hide();
	 }
});

// // full calendar
// document.addEventListener('DOMContentLoaded', function() {
//  var calendarEl = document.getElementById('calendar');

//  var calendar = new FullCalendar.Calendar(calendarEl, {
//    headerToolbar: {
// 	 start: 'title',
// 	 center: '',
// 	 end: 'prev,today,next'
//    },
//    initialView: 'dayGridMonth',
   
//    views: {
// 	 dayGridWeek: {
// 	   titleFormat: '{DD.{MM.}}YYYY'
// 	 },
// 	 listWeek: {
// 	   titleFormat: '{DD.{MM.}}YYYY'
// 	 }
//    },
//    events: [
// 	 {
// 			   title: 'P',                
// 			   start: '2022-04-01',
// 			   backgroundColor: '#7fc27c',
// 		   },  
// 		   {
// 			   title: 'P',                
// 			   start: '2022-04-02',
// 			   backgroundColor: '#7fc27c'
// 		   },
// 		   {
// 			   title: 'P',                
// 			   start: '2022-04-03',
// 			   backgroundColor: '#7fc27c'
// 		   },  
// 			 {
// 			   title: 'A',
// 			   start: '2022-04-04',
// 			   backgroundColor: '#ea9595'
// 		   }
// 		   ,  
// 			 {
// 			   title: 'H',
// 			   start: '2022-04-15',
// 			   backgroundColor: '#333'
// 		   }
// 		   ,  
// 			 {
// 			   title: 'H',
// 			   start: '2022-04-16',
// 			   backgroundColor: '#333'
// 		   }
//    ],
	

//    windowResize: function(view) {
// 	 var current_view = view.type;
// 	 var expected_view = $(window).width() > 800 ? 'dayGridMonth' : 'listWeek';
// 	 if (current_view !== expected_view) {
// 	   calendar.changeView(expected_view);
// 	 }
//    },
//  });

//  calendar.render();

//  if ($(window).width() < 800) {
//    calendar.changeView('listWeek');
//  }

//  $('input[class=event_filter]').change(function() {
//    calendar.render();
//  });
   
// });

// approve 
$(document).ready(function() {
   $('a.approve').click(function(){  
		$(this).parent().parent().find('.tags span').addClass('approved');
		$(this).parent().parent().find('.tags span').text('Approved');
		$(this).addClass('disabled');
		$(this).parent().find('.reject').addClass('disabled')
   });
   $('a.reject').click(function(){  
		$(this).parent().parent().find('.tags span').addClass('rejected');
		$(this).parent().parent().find('.tags span').text('Rejected');
		$(this).addClass('disabled');
		 $(this).parent().find('.approve').addClass('disabled')
   });

});

// coutry code textbox
// Vanilla Javascript
var input = document.querySelector("#phone");
 window.intlTelInput(input,({
   // options here
}));
$(document).ready(function() {
   $('.phone .iti__flag-container').click(function() { 
   var countryCode = $('.phone .iti__selected-flag').attr('title');
   var countryCode = countryCode.replace(/[^0-9]/g,'')
   $('#phone').val("");
   $('#phone').val("+"+countryCode+" "+ $('#phone').val());
   });
});
var input1 = document.querySelector("#phone1");
 window.intlTelInput(input1,({
   // options here
}));

$(document).ready(function() {
   $('.phone2 .iti__flag-container').click(function() { 
   var countryCode = $('.phone2 .iti__selected-flag').attr('title');
   var countryCode = countryCode.replace(/[^0-9]/g,'')
   $('#phone1').val("");
   $('#phone1').val("+"+countryCode+" "+ $('#phone1').val());
   });
});

