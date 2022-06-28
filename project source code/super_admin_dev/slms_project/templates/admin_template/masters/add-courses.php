<?php  $txt="Batch Management" ; $subP="add-course"; include('../header-1.php');  ?>
    <div class="app-content content position-relative  ">
         
      <div class="content-wrapper">
        <div class="content-body "><!-- Revenue, Hit Rate & Deals -->
           <div class="col-lg-12 col-md-12 col-sm-12  ">
             <h4 class="head mb-2  ">Add Courses <a   class="btn btn-default   float-right btn-sm  mt--1 " href="course-list.php" >Back to list</a></h4>
                <div class="card  form">
                  <div class="card-content ">
                      <div class="card-body"  >
                             <div class="row ">
                                  <div class="col-lg-3 mt-1  form-group">
                                      <label>Course ID </label>
                                      <input type="text" class="form-control" placeholder="Enter course id" value="" />
                                   </div>
                                    <div class="col-lg-3 mt-1   form-group">
                                      <label>Course Type</label>
                                      <select class="form-control">
                                         <option class="d-none">Select</option>
                                        <option>UG</option>
                                        <option>PG</option>
                                      </select>
                                   </div>
                                   <div class="col-lg-6 mt-1   form-group">
                                      <label>Course Name</label>
                                      <input type="text" class="form-control" placeholder="Enter course name" value="" />
                                   </div>

                                   <div class="text-right col-lg-12   pt-1">
                                        <a  class="btn btn-primary   " href="javascript:;" data-toggle="modal" data-target="#success1" >Submit</a>
                                       
                                     </div>

                                      <div class="text-center col-lg-12 mt-1    ">
                                          <h5 class="or">OR</h5>
                                      </div>  

                                       <div class="upload col-lg-6 mx-auto mt-2 " >
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
           <p> Course list has been uploaded successsfully.  </p>
           <a href="course-list.php" class="btn btn-primary btn-sm"  >OK</a>
        </div>
         
      </div>
    </div>
  </div>

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
           <p> Course has been addedd successsfully. </p>
           <a href="#" data-dismiss="modal" class="btn btn-primary btn-sm">OK</a>
        </div>
         
      </div>
    </div>
  </div>
 
<?php include('../footer-1.php')  ?>