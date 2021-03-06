<?php  $txt="Masters" ; $subP="topics"; include('../header-1.php');  ?>
    <div class="app-content content position-relative  ">
         
      <div class="content-wrapper">
        <div class="content-body "> 
          <div class="top-options">
            <div class="row">
              <div class="col-md-3"><h3 >Upload Topic List </h3></div>
                 <div class="col-md-9 text-right ">
                    <a href="subject-list.php" class="btn  btn-default  btn-sm"><i class="fa fa-arrow-left"></i>   Back to List</a>
                 </div>
           </div>
           </div>
           <div class="col-lg-12 col-md-8 mx-auto col-sm-12 p-0  ">
                <div class="card  form p-4  ">
                  <div class="card-content ">
                      <div class="card-body"  >
                             <div class="row ">
                                   <div class="upload col-lg-8 mx-auto  " >
                                    <h3>  Upload Sheet</h3>
                                    <label>
                                       <input type="file"  name="" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel">
                                        Choose File
                                       <span>Browse</span>
                                    </label>
                                    <div class="clearfix  "></div>
                                    <span id="file" class="file"></span>

                                   
                                </div> 
                                    
                           </div>
                             
                      </div>
                  </div>
              </div>

              <div class="text-right    pt-1 mb-4">
                    <a   class="btn btn-primary btn-lg pl-3 pr-3  " href="javascript:;" data-toggle="modal" data-target="#success"><i class="fa fa-save "></i> Save</a>
                   
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
           <p>Topic list has been uploaded successsfully.  </p>
           <a href="subject-list.php" class="btn btn-primary btn-sm"  >OK</a>
        </div>
         
      </div>
    </div>
  </div>

    
<?php include('../footer-1.php')  ?>