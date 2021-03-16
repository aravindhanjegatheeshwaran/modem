
<!doctype html>
<html lang="en">
  

<head>
    <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <title></title>
      
      <!-- Favicon -->
      <link rel="shortcut icon" href="http://iqonic.design/themes/instadash/html/assets/images/favicon.ico" />
      <?html include "include/css.html"; ?>

      <style>

        ul
        {
          margin:0;
          padding:0;
        }
              .voicecall_form
              {
                font-size:12px !important;
              }
              .voicecall_form .form-control
              {
                border-radius:1px;
              }
      .voicecall_form1 li, .voicecall_form2 li, .voicecall_form3 li
        {
          float:left;  
          list-style:none;
          margin:3px;
        }
        .voicecall_form2 li
        {
          float:left;
          list-style: none;
         margin-right:10px;
         margin-top:3px;
        }
     .voicecall_form1 li .btn
        {
          background:#dedede;
          color:black;
          margin:3px;
          border-radius:1px; 
          font-size:12px;
        }
        .voicecall_form3 .btn
        {
          background:#dedede;
          color:black;
          margin:3px;
          margin-right:6px;
          border-radius:1px; 
          font-size:12px;
        }
        .voicecall_form2
        {
          font-weight: bold;
          font-size:13px;
        }
         .sec_table
         {
          border:1px solid gray;
          min-height:350px;
          background:#dedede;
         }
         .sec_table table th
         {
          background: white;
         }
      </style>
       </head>
        }
        }
  <body class="  ">
    <!-- loader Start -->
    <div id="loading">
          <div id="loading-center">
          </div>
    </div>
    <!-- loader END -->
    <!-- Wrapper Start -->
    <div class="wrapper">
      
     
              <?html
					include "include/side.html";
			  ?>
              
              <div class="p-3"></div>
          </div>
          </div>       <div class="iq-top-navbar">
          <div class="iq-navbar-custom">
              <nav class="navbar navbar-expand-lg navbar-light p-0">
              <div class="iq-navbar-logo d-flex align-items-center justify-content-between">
                  <i class="ri-menu-line wrapper-menu"></i>
                  <a href="index.html" class="header-logo">
                      <img src="../assets/images/logo.png" class="img-fluid rounded-normal light-logo" alt="logo">
                      <img src="../assets/images/logo-white.png" class="img-fluid rounded-normal darkmode-logo" alt="logo">
                      
                  </a>
              </div>
                 <div class="d-flex align-items-center justify-content-between welcome-content">
                    <div class="navbar-breadcrumb">
                       <center> <h4 class="mb-0">Voice Call</h4></center>
                    </div> 
                  
              </nav>
          </div>
      </div>
      <div class="content-page">
     <div class="container-fluid voicecall_form">
        
        <div class="row">
            <div class="col-lg-12">
               <div class="card">
                  <div class="card-body">
                    <div class="row">
                      <div class="col-lg-8">
                        <ul class="voicecall_form1">
                          <li>
                            Select Audio
                          </li>
                            <li>
                              <div class="form-group">
                    
                        <select class="form-control form-control-sm">
                           <option selected=""></option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                     </div> </li>

                     <li>
                      <button type="submit" class="btn ">Pick Audio</button>
                     </li>
                     <li>
                      <button type="submit" class="btn ">View Loaded Audio</button>
                     </li>
                     
                     <li>
                      <button type="submit" class="btn ">Manage DTMF</button>
                     </li>
                     <li>
                      <button type="submit" class="btn">Export to CSV</button>
                     </li>
                        </ul>
                     </div>
                   
                    <div class="col-lg-4">
                      <ul class="voicecall_form2">
                        <li>Total Call:  <span>0 </span></li>
                        <li>Ongoing Call: <span>0</span> </li>
                        <li>Connected:  <span>0</span></li>
                      </ul>
                    </div>
                 </div>
                 <div class="row">
                      <div class="col-lg-7">
                        <ul class="voicecall_form3">
                          <li>
                            Select Contacts
                          </li>
                            <li>
                              <div class="form-group">
                    
                        <select class="form-control form-control-sm">
                           <option selected=""></option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                     </div> </li>

                     <li>
                      <span>Call Duration </span>
                     </li>
                     <li>
                      <div class="form-group">
                    
                        <select class="form-control form-control-sm">
                           <option selected="">30</option>
                           <option value="1">50</option>
                           <option value="2">100</option>
                           <option value="3">150</option>
                        </select>
                     </div>
                     </li>
                     
                     <li>
                      <button type="submit" class="btn ">Start</button>
                     </li>
                     <li>
                      <button type="submit" class="btn">Stop</button>
                     </li>
                     <li>
                      <button type="submit" class="btn">Reset</button>
                     </li>
                        </ul>
                     </div>
                   
                    <div class="col-lg-5">
                      <ul class="voicecall_form2">
                        <li>Not Reachable:  <span>0 </span></li>
                        <li>Interested: <span>0</span> </li>
                        <li>Busy:  <span>0</span></li>
                        <li>Failed:  <span>0</span></li>
                      </ul>
                    </div>
                 </div>
                 
                 <br/>
                  <div class="row sec_table">
                  <table  class="table  table-bordered" >
                           <thead>
                              <tr>
                                <th>Port Name</th>
                                 <th>Port Status</th>
                                 <th>Calling No</th>
                                 <th>Status</th>
                                 <th>Interested</th>
                                 <th>Busy</th>
                                 <th>Not Reachable</th>
                                 <th>Failed</th>
                                 <th>Mobile No</th>
                                 <th>Call Time</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                               
                                 
                              </tr>
                           </tbody>
                        </table>
               
                 </div>

                  </div>
               </div>
            </div>
          </div>
          
        </div>
        
        <!-- Page end  -->
    </div>
      </div>
    </div>
    <!-- Wrapper End-->
    <footer class="iq-footer">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-6">
                    <ul class="list-inline mb-0">
                        <li class="list-inline-item"><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li class="list-inline-item"><a href="terms-of-service.html">Terms of Use</a></li>
                    </ul>
                </div>
                <div class="col-lg-6 text-right">
                    Copyright 2020 <a href="#">Insta Dash</a> All Rights Reserved.
                </div>
            </div>
        </div>
    </footer>
   <?html include "include/js.html"; ?>
  </body>


</html>