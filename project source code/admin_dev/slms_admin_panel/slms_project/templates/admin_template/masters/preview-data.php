<?php $txt="Batch Management" ;  $subP="add-course"; include('../header-1.php')  ?>
    <div class="app-content content position-relative  ">
      <div class="content-wrapper  ">
        <div class="content-body "><!-- Revenue, Hit Rate & Deals -->
             
             <div class="col-lg-12 col-md-12 col-sm-12  ">
               <h4 class="head mb-2  ">Preview Student List | Batch ID: <strong>BID001</strong>  <a   class="btn btn-default   float-right btn-sm  mt--1 " href="select-batch-student.php" >Back</a></h4>
             </div>
             <div class="table-responsive  ">
                <table id="example1"  class="display table data-table">
                    <thead>
                        <tr>
                             <th>S.No.</th>
                             <th>Student Name</th>
                              <th>Registration ID</th>
                              <th>Mail ID</th>
                              <th>Contact No.</th>
                              <th> Gender</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr  >
                            <td>1</td>
                            <td> Amit singh</td>
                            <td>AM454555</td>
                            <td>amit@gmail.com</td>
                            <td>8575885588</td>
                            <td  >
                                 Male
                            </td>

                        </tr>
                        
                        <tr  >
                              <td>2</td>
                            <td> Ram Kumar</td>
                            <td>RK454555</td>
                            <td>ram@gmail.com</td>
                            <td>9875885588</td>
                            <td  >
                                 Male
                            </td>

                        </tr>
                         <tr  >
                            <td>3</td>
                            <td> Kamlesh singh</td>
                            <td>KS454555</td>
                            <td>kamlesh@gmail.com</td>
                            <td>8575885588</td>
                            <td  >
                                 Male
                            </td>

                        </tr>
                         <tr  >
                            <td>4</td>
                            <td>Anuj Pathak</td>
                            <td>AP454555</td>
                            <td>anuj@gmail.com</td>
                            <td>8875885588</td>
                            <td  >
                                 Male
                            </td>

                        </tr>
                         <tr  >
                            <td>5</td>
                            <td> Pankaj Yadav</td>
                            <td>PY454555</td>
                            <td>pankakj@gmail.com</td>
                            <td>8575885588</td>
                            <td  >
                                 Male
                            </td>

                        </tr>
                         <tr  >
                            <td>6</td>
                            <td> Ankit Kumar</td>
                            <td>AK454555</td>
                            <td>ankit@gmail.com</td>
                            <td>8575885588</td>
                            <td  >
                                 Male
                            </td>

                        </tr>

                         <tr  >
                            <td>7</td>
                            <td> Sunil singh</td>
                            <td>SS454555</td>
                            <td>sunil@gmail.com</td>
                            <td>8575885588</td>
                            <td  >
                                 Male
                            </td>

                        </tr>
                    </tbody>
                </table>
             
            </div>
            <div class="text-center"><a href="" class="btn btn-dark btn-sm mt-2">Load More</a> </div>
           <div class="text-right  pt-2 bottom-btn">
                   <a  class="btn btn-primary pl-5 pr-5" data-toggle="modal" data-target="#alert" href="javascript:;">Submit</a>
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