
<style>
 #loader1 
 {
  position: absolute;
  left: 20%;
  top: 20%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
#loader2
 {
  position: absolute;
  left: 50%;
  top: 22%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
#loader3
 {
  position: absolute;
  left: 30%;
  top: 20%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
#loader4
 {
  position: absolute;
  left: 34%;
  top: 20%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
#loader5
 {
  position: absolute;
  left: 38%;
  top: 20%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
#loader6
 {
  position: absolute;
  left: 42%;
  top: 20%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}#loader7
 {
  position: absolute;
  left: 46%;
  top: 20%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
#loader8
 {
  position: absolute;
  left: 50%;
  top: 20%;
  z-index: 1;
  width: 20px;
  height: 20px;
  background:white;
  border: 3px solid #f3f3f3;
  border-radius: 50%;
  border-top: 3px solid #3498db;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
.towerdiv, .towerdiv1, .towerdiv2, .towerdiv3, .towerdiv4, .towerdiv5, .towerdiv6, .towerdiv7,
.towerdiv8, .towerdiv9,
{
	position:relative;
}
@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Add animation to "page content" */
.animate-bottom {
  position: relative;
  -webkit-animation-name: animatebottom;
  -webkit-animation-duration: 1s;
  animation-name: animatebottom;
  animation-duration: 1s
}

@-webkit-keyframes animatebottom {
  from { bottom:-100px; opacity:0 } 
  to { bottom:0px; opacity:1 }
}

@keyframes animatebottom { 
  from{ bottom:-100px; opacity:0 } 
  to{ bottom:0; opacity:1 }
}

</style>
<?php 
	echo $data_id = $_REQUEST['data_id'];

	

 ?>


				<div class="row">
					<div class="col-lg-1">
					<h4> Com1 </h4>
					
					<i class="fa fa-signal" aria-hidden="true"></i>
					</div>
					<div class="col-lg-11 simback">
						<ul class="tower">
							<li>
								<div id="startcont"  class="towerdiv">
								<!--<i class=" mt-12 fa fa-wifi" aria-hidden="true"></i>--><br/>
								<a href="#">sim1</a>
								<?php
								 ?>
									<div id="loader1">
								</div>
							<?php	 ?>
								
								
								</div>
							</li>
							<li>
								<div id="startcont1" onclick="myFunction1()" class="towerdiv1">
<br/>
								<a href="#">sim2</a>
								
								<?php 
								$sim=2;
								if ($sim>=1) {  

									}else{ ?>
								<div id="loader2">
								</div>
							<?php }
								 ?>
								
								</div>
							</li>
							<li>
								<div id="startcont1_3" onclick="myFunction1_3()" class="towerdiv2">
								<br/>
								<a href="#">sim3</a>								
								
								<div id="loader3">
								</div>
								</div>
							</li>
							<li>
								<div id="startcont1_4" onclick="myFunction1_4()" class="towerdiv3">
								<br/>
								<a href="#">sim4</a>																
								
								<div id="loader4">
								</div>
								</div>
							</li>
							<li>
								<div id="startcont1_5" onclick="myFunction1_5()" class="towerdiv4">
								<br/>
								<a href="#">sim5</a>
															
								
								<div id="loader5">
								</div>
								</div>
							</li>
							<li>
								<div id="startcont1_6" onclick="myFunction1_6()" class="towerdiv5">
								<br/>
								<a href="#">sim6</a>							
															
								
								<div id="loader6">
								</div>
								</div>
							</li>
							<li>
								<div id="startcont1_7" onclick="myFunction1_7()" class="towerdiv7">
								<br/>
								<a href="#">sim7</a>
								
								
									<div id="loader7">
								</div>
								</div>
							</li>
							<li>
								<div id="startcont1_8" onclick="myFunction1_8()" class="towerdiv8">
								<br/>
								<a href="#">sim8</a>																
								
								<div id="loader8">					
								</div>
								</div>
							</li>
						</ul><br/>
					</div>
				</div><br/> <br/>
				<div class="row">
					<div class="col-lg-1">
					<h4> Com2 </h4>
					<i class="fa fa-signal" aria-hidden="true"></i>
					<div id="loader1" style="display:none">
								</div>
					</div>
					
					<div class="col-lg-11 simback">
						<ul class="tower">
							<li>
								<div id="startcont1_1" onclick="myFunction1()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_1" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_1" class="towerdiv1_1">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
							<li>
								<div id="startcont1_18" onclick="myFunction1_18()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_18" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_18" class="towerdiv1_18">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
							<li>
								<div id="startcont1_19" onclick="myFunction1_19()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_19" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_19" class="towerdiv1_19">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
							<li>
								<div id="startcont1_20" onclick="myFunction1_20()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_20" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_20" class="towerdiv1_20">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
							<li>
								<div id="startcont1_21" onclick="myFunction1_21()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_21" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_21" class="towerdiv1_21">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
							<li>
								<div id="startcont1_22" onclick="myFunction1_22()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_22" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_22" class="towerdiv1_22">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
							<li>
								<div id="startcont1_23" onclick="myFunction1_23()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_23" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_23" class="towerdiv1_23">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
							<li>
								<div id="startcont1_24" onclick="myFunction1_24()" class="towerdiv">
								<br/>
								<a href="#">sim8</a>
								<div id="loader1_24" style="display:none">					
								</div>								
								</div>
								<div style="display:none;" id="myDiv1_24" class="towerdiv1_24">
								<br/>
								<a href="#">sim8</a>
								</div>
							</li>
						</ul><br/>
					</div>
				</div>
				
			