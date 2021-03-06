
<!doctype html>
<html lang="en">
  

<head>
    <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <title></title>
      
      <!-- Favicon -->
      <link rel="shortcut icon" href="http://iqonic.design/themes/instadash/html/assets/images/favicon.ico" />
      <?php include "include/css.php"; ?>

      <style>
        .voice_call_status
        {
          font-size:14px;
        }
        .voice_call_status select, .voice_call_status input[type="date"]
        {
          width:100%;
          border-radius:1px;
          border:1px solid gray;
          background:#dedede;
        }
        .callstatusul1 ul
        {
          margin:0;
          padding:0;
        }
        .callstatusul1 ul li
        {
          list-style:none;
          float:left;
          margin-right:60px;
          font-weight: bold;
        }
        .btn1
        {
          border-radius:1px;
          border:1px solid  gray;
          background:#dedede;
          color:black;
          float:right;
        }
        .editorstyle
        {
          border:1px solid gray;
          min-height:350px;
          width:100%;
          background: #dedede;
          margin-top:30px;
        }
      </style>

       </head>
       
  <body class="  ">
    <!-- loader Start -->
    <div id="loading">
          <div id="loading-center">
          </div>
    </div>
    <!-- loader END -->
    <!-- Wrapper Start -->
    
              <?php
					include "include/side.php";
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
                       <center> <h4 class="mb-0">Voice Call Status</h4></center>
                    </div> 
                  
              </nav>
          </div>
      </div>
      <div class="content-page">
     <div class="container-fluid voicecall_status_form">
        
        <div class="row">
            <div class="col-lg-12">
               <div class="card">
                  <div class="card-body voice_call_status">
                   
                    <div class="row">
                      <div class="col-lg-3">
                         <div class="row">
                          <div class="col-lg-6">
                            Select Report Type:
                          </div>
                          <div class="col-lg-6">
                             <select class="form-control form-control-sm">
                           <option selected="">View Report</option>
                           <option value="1">50</option>
                          
                        </select>
                          </div>
                        </div>
                      </div>
                      <div class="col-lg-3">
                       <div class="row">
                          <div class="col-lg-6">
                            <label>Select Report Date:</label>
                          </div>
                           <div class="col-lg-6">
                             <input class="form-control form-control-sm" type="date" name="date">
                          </div>
                       </div>
                     </div> 
                       <div class="col-lg-4">
                         <div class="row">
                          <div class="col-lg-4">
                            Select File:
                          </div>
                          <div class="col-lg-8">
                             <select class="form-control form-control-sm">
                           <option selected="">View Report</option>
                           <option value="1">50</option>
                          
                        </select>
                          </div>
                        </div>
                      </div> 
                        <div class="col-lg-2">
                         <div class="row">
                          <div class="col-lg-6">
                            Status:
                          </div>
                          <div class="col-lg-6">
                             <select class="form-control form-control-sm">
                           <option selected="">All</option>
                           <option value="1">50</option>
                          
                        </select>
                          </div>
                        </div>
                      </div> 
                       
                      </div><br/>

                      <div class="row">

                        <div class="col-lg-10 callstatusul1">
                          <ul>
                            <li>Total Call: </li>
                            <li>Connected: </li>
                            <li>Interested: </li>
                            <li>Busy: </li>
                            <li>Not Reachable: </li>
                            <li>Failed: </li>
                          </ul>
                        </div>

                         <div class="col-lg-2">
                            <button class="btn1" value="submit"> Get Report</button>
                        </div>
                      </div>
                     <div class="row">
                      <div class="editorstyle">
                      </div>
                     </div>
                    </div>
                 
                 <br/>
                  
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
   <?php include "include/js.php"; ?>
  </body>


</html>