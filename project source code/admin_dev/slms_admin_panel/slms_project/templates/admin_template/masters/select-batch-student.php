<?php  $txt="Batch Management"; include('../header-1.php');  ?>
    <div class="app-content content position-relative  ">
         
      <div class="content-wrapper">
        <div class="content-body "><!-- Revenue, Hit Rate & Deals -->
           <div class="col-lg-12 col-md-12 col-sm-12 mt-1  ">
             <h4 class="head mb-2  ">Select Batch Students | Batch ID: <strong>BID001</strong> <a   class="btn btn-default   float-right btn-sm  mt--1 " href="batch-list.php" >Back to list</a></h4>
                <div class="card  form pt-0 pl-0 pr-0">
                  <div class="card-content pt-0">
                      <div class="card-body pt-0 pl-0 pr-0"  >
                         <div class="top-options mx-auto  mb-2  text-center col-md-12  ">
                             <div class="form-group radios radios1 pl-2" >
                                <label><span>Select Method</span> </label>
                                <label>
                                    <input type="radio" checked="" name="b_type" id="manual"><span>Manual Entry</span>
                                </label>
                                <label>
                                    <input type="radio" name="b_type" id="uploadF"><span>Upload Excel/CSV File</span>
                                </label>
                                 
                             </div>
                            </div>

                            <div class="manual-entry ">
                             <div class="row ">
                                <div class="col-lg-2   mb-2 form-group ico  pr-0  "><p class="pt-1">Select/Enter Student </p> </div>
                                  <div class="col-lg-8   mb-2 form-group ico pl-2">
                                   <i class="fa fa-search"></i>
                                      <select class="select2 form-control select2-placeholder3" id="default-select">
                                         <option  > </option>
                                          <option value="1">Student 1</option>
                                          <option value="2">Student 1</option>
                                           <option value="3">Student 3</option>
                                          <option value="4">Student 4</option>
                                           <option value="5">Student 5</option>
                                          <option value="6">Student 6</option>
                                    </select>
                                   </div>
                                    <div class="col-lg-2   mb-2 form-group ico pl-2 text-center">
                                      <a href="javascript:;" class="btn btn-primary add-students">+ Add</a>
                                    </div>

                                      <div class="col-lg-12">
                                         <div class="table-responsive  ">
                                            <table id="students" class="display table  html-table table-striped">
                                                <thead>
                                                    <tr>
                                                        <th>Student Name</th>
                                                        <th>Registration ID</th>
                                                        <th>Mail ID</th>
                                                        <th>Contact No.</th>
                                                        <th> Gender</th>
                                                        <th></th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr class="not-added"><td colspan="6" class="text-center">No student added</td></tr>
                                                </tbody>
                                            </table>
                                         
                                        </div>
                                      </div>  
                             </div>
                           </div>

                            <div class="upload-csv">
                             <div class="row ">
                                <div class="col-lg-7  "> 
                                    <div class="table-responsive  ">
                                          <table  id="sel_val_tbl" class="display table  html-table sel_val_tbl  ">
                                              <thead>
                                                  <tr>
                                                      <th>Student Name <div><select><option>A</option><option>B</option><option>C</option></select></div></th>
                                                      <th>Registration ID<div><select><option>A</option><option>B</option><option>C</option></select></div></th>
                                                      <th>Mail ID<div><select><option>A</option><option>B</option><option>C</option></select></div></th>
                                                      <th>Contact No.<div><select><option>A</option><option>B</option><option>C</option></select></div></th>
                                                      <th> Gender<div><select><option>A</option><option>B</option><option>C</option></select></div></th>
                                                      
                                                  </tr>

                                              </thead>
                                              <tbody>
                                                  <tr ><td > No student added </td><td  >  </td><td  >  </td><td ></td><td  >  </td> </tr>
                                              </tbody>
                                          </table>
                                      </div>

                                </div>

                                 <div class="col-lg-5  "> 
                                     <div class="upload  " >
                                        <h3>  Upload Sheet</h3>
                                        <label>
                                           <input type="file"  name="" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel">
                                            Choose File
                                           <span>Browse</span>
                                        </label>
                                        <div class="clearfix  "></div>
                                        <span id="file" class="file"></span>

                                        <button class="btn btn-info btn-upload ">Upload <i class="fa fa-upload"></i></button>

                                    </div> 

                                     <div class="upload   col-assign">
                                         <h5>Uploaded Sheet Preview</h5>
                                          <div class="table-res mt-0">
                                            <table class="display table  html-table">
                                               <thead>
                                                <tr class="text-left  ">
                                                 <th>Registration No <br>G</th> 
                                                  <th> Name<br>  A</th>
                                                  <th>Contact<br> B </th>
                                                  
                                                  <th>Email <br>D</th>
                                                   
                                                  <th>Gender<br> F</th>
                                                </tr>
                                                </thead>
                                               <tbody>
                                                <tr>
                                                 <td  >  </td>
                                                 <td>    </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>

                                                </tr>
                                                 <tr>
                                                 <td  >  </td>
                                                 <td>    </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>

                                                </tr>
                                                 <tr>
                                                 <td  >  </td>
                                                 <td>    </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>
                                                 <td>  </td>

                                                </tr>
                                                 
                                              
                                               </tbody>

                                            </table>
                                          </div>
                                    </div>  
                                 </div>

                              </div>
                            </div>
                      </div>
                  </div>
              </div>

               <div class="text-right  pt-0 bottom-btn">
                   <a  class="btn btn-primary pl-5 pr-5" data-toggle="modal" data-target="#alert" href="javascript:;">Submit</a>
               </div>
               <div class="text-right  pt-0 bottom-btn1">
                   <a class="btn btn-primary pl-5 pr-5"  href="preview-data.php">Preview  & Submit</a>
               </div>
          </div>
      </div>
     </div>
   </div>

   <!-- Modal -->
  <div class="modal fade small" id="alert" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
           <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body text-center">
           <p>Are you sure want to add 55 new student to   <br>Batch ID <strong>BID001</strong>.  </p>
           
            <a href="" class="btn btn-dark btn-sm mr-1" data-dismiss="modal">No</a>
           <a href="" class="btn btn-primary btn-sm" data-dismiss="modal" data-toggle="modal" data-target="#success">Yes</a>
           
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
           <p> Students have been successsfully added to   <br>Batch ID <strong>BID001</strong>.  </p>
           
            
           <a href="" class="btn btn-primary btn-sm" data-dismiss="modal"  >OK</a>
           
        </div>
         
      </div>
    </div>
  </div>
 
<?php include('../footer-1.php')  ?>