<?php  $txt="Batch Management" ;  $subP="add-sub-to-course"; include('../header-1.php');  ?>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.1/css/bootstrap-select.css" />
    <div class="app-content content position-relative  ">
         
      <div class="content-wrapper">
        <div class="content-body "><!-- Revenue, Hit Rate & Deals -->
           <div class="col-lg-12 col-md-12 col-sm-12  ">
             <h4 class="head mb-2  ">Add Subjects to Course <a   class="btn btn-default   float-right btn-sm  mt--1 " href="subject-list.php" >Back to list</a></h4>
                <div class="card  form">
                  <div class="card-content ">
                      <div class="card-body"  >
                             <div class="row ">
                                <div class="col-lg-3 offset-md-2  mt-1  form-group ico no-ico">
                                      <label>Select Course Type </label>
                                       <select class=" form-control  "  >
                                         <option  class="d-none"> Select</option>
                                          <option value="1" >UG</option>
                                          <option value="2">PG</option>
                                    </select>
                                   </div>
                                  <div class="col-lg-5   mt-1  form-group ico no-ico">
                                      <label>Select Course </label>
                                       <select class="select2 form-control select2-placeholder4"    >
                                         <option class="d-none" > </option>
                                          <option value="1">B.Sc. - Maths</option>
                                          <option value="2">B.Sc. - Bio</option>
                                           <option value="3">B.Sc. - Ag</option>
                                          <option value="4">B.A. </option>
                                           <option value="5">B.Com.</option>
                                          <option value="6">BBA</option>
                                    </select>
                                   </div>

                                    
                                   <div class="col-lg-8 mx-auto     form-group sel_subj">
                                      <label>Subject Name</label>
                                        <select class="selectpicker d-block" multiple data-live-search="true">
                                          <option class="d-none"> </option>
                                          <option>Hindi</option>
                                          <option>English</option>
                                          <option>Physics</option>
                                          <option>Maths</option>
                                          <option>Zoology</option>
                                          <option>Finance</option>
                                          <option>Accounts</option>
                                         </select>
                                   </div>

                                   <div class="text-right col-lg-10 mt-1    ">
                                        <a  class="btn btn-primary   " href="javascript:;" data-toggle="modal" data-target="#success1" >Submit</a>
                                       
                                     </div>

                                      <div class="text-center col-lg-12 mt-1    ">
                                          <h5 class="or">OR</h5>
                                      </div>  

                                       <div class="upload col-lg-6 mx-auto mt-2   " >
                                        <h3>  Upload Sheet</h3>
                                        <label>
                                           <input type="file"  name="" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel">
                                            Choose File
                                           <span>Browse</span>
                                        </label>
                                        <div class="clearfix  "></div>
                                        <span id="file" class="file"></span>

                                        <button data-toggle="modal" data-target="#success" class="btn btn-info  ">Upload <i class="fa fa-upload"></i></button>

                                    </div> 
                                    
          
                                      
                              </div>
                      </div>
                  </div>
              </div>

               
            </div>
      </div>
     </div>
   </div>

   <!-- Modal -->
   <div class="modal fade small with-img" id="success" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
           <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body text-center">
           <img src="../app-assets/images/success-icon-10.png">
           <p> Subject list has been uploaded successsfully.  </p>
           <a href="subject-list.php" class="btn btn-primary btn-sm"  >OK</a>
           
        </div>
         
      </div>
    </div>
  </div>
  <!-- Modal -->
   <div class="modal fade small with-img" id="success1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
           <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body text-center">
           <img src="../app-assets/images/success-icon-10.png">
           <p> Subject list has been updated successsfully.  </p>
           <a href="#" data-dismiss="modal" class="btn btn-primary btn-sm"  >OK</a>
           
        </div>
         
      </div>
    </div>
  </div>
 
<?php include('../footer-1.php')  ?>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.13.1/js/bootstrap-select.min.js"></script>
<script type="text/javascript">
  $('.selectpicker').selectpicker();
</script>