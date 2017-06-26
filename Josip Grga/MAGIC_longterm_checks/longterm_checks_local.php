<?php



// List of parameters to check
$ltm_params = eval("return ".file_get_contents("ltm_checks.txt").";");
//echo $ltm_params[1];
$totalpages = count($ltm_params)-1;
// Dictionary for translating parameters to Graph titles
$graphtitles = eval("return ".file_get_contents("cc_daq.txt").";");
// Files with datacheck plots limits (different for each telescope)
$DClimitsM1 = eval("return ".file_get_contents("limitsM1.txt").";");
$DClimitsM2 = eval("return ".file_get_contents("limitsM2.txt").";");
// Dictionary for translating the database parameter names to datacheck limits names
$limitsDictionary = eval("return ".file_get_contents("limit_dict.txt").";");



// database connection info
//$conn = mysql_connect('localhost','nbaran','jfd6a32') or trigger_error("SQL", E_USER_ERROR);
//$db = mysql_select_db('long_term_monitoring_database',$conn) or trigger_error("SQL", E_USER_ERROR);

$conn = mysqli_connect('localhost','root','password');
$database = mysqli_select_db($conn, 'long_term_monitoring_database');
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


// find out how many rows are in the table - i don't care about this
$sql = "SELECT COUNT(*) FROM dataset_params";
$result = mysqli_query($conn, $sql) or trigger_error("SQL", E_USER_ERROR);
$r = mysqli_fetch_row($result);
$numrows = $r[0];


//$totalpages = ceil($numrows / $rowsperpage);

// get the current page or set a default
if (isset($_GET['currentpage']) && is_numeric($_GET['currentpage'])) {
   // cast var as int
   $currentpage = (int) $_GET['currentpage'];
} else {
   // default page num
   $currentpage = 1;
} // end if

// if current page is greater than total pages...
if ($currentpage > $totalpages) {
   // set current page to last page
   $currentpage = $totalpages;
} // end if
// if current page is less than first page...
if ($currentpage < 1) {
   // set current page to first page
   $currentpage = 1;
} // end if



//$now   = new DateTime;
//$cloneY = clone $now;    
//$cloneY->modify( '-365 day' );
//$cloneM = clone $now;    
//$cloneM->modify( '-30 day' );
//$datefromY = $cloneY->format( 'Y-m-d' );
//$datefromM = $cloneM->format( 'Y-m-d' );

// Fix for  PHP < 5.2.0

//$Mago = 30; // days
//$Mtimestamp = time() - ($Mago * 86400);
//$Yago = 365; // days
//$Ytimestamp = time() - ($Yago * 86400);
//$datefromY =date('Y-m-d',$Ytimestamp);
//$datefromM = date('Y-m-d',$Mtimestamp);
$datefromY=2013-03-29;
$datefromM=2013-04-28;
//$currenttime = time()/86400/365;
//echo $datefromM . $datefromY . $currenttime;


// get the info from the db 
$sql = "SELECT name, id, date, mean, rms FROM dataset_params WHERE date > '$datefromY' AND name = '$ltm_params[$currentpage]' AND  telescope ='M1'";
$sql2 = "SELECT name, id, date, mean, rms FROM dataset_params WHERE date > '$datefromM' AND name = '$ltm_params[$currentpage]' AND  telescope ='M1'";
$sql3 = "SELECT name, id, date, mean, rms FROM dataset_params WHERE date > '$datefromY' AND name = '$ltm_params[$currentpage]' AND  telescope ='M2'";
$sql4 = "SELECT name, id, date, mean, rms FROM dataset_params WHERE date > '$datefromM' AND name = '$ltm_params[$currentpage]' AND  telescope ='M2'";
//$sql = "SELECT name, id, date, mean, rms FROM dataset_params WHERE date > '2015-11-01' AND name = 'calq_int'";
$result  = mysqli_query($conn, $sql) or trigger_error("SQL", E_USER_ERROR);
$result2 = mysqli_query($conn, $sql2) or trigger_error("SQL", E_USER_ERROR);
$result3 = mysqli_query($conn, $sql3) or trigger_error("SQL", E_USER_ERROR);
$result4 = mysqli_query($conn, $sql4) or trigger_error("SQL", E_USER_ERROR);

//$testvariable = mysqli_fetch_row($result);
//echo $testvariable[4];
//echo $result;
// process DataCheck limits for the correct telescope, set all the numbers in one array
// M1
  $paramArray = "[";
  $parameter = $ltm_params[$currentpage];
   if (isset($_POST['$parameter']))
   {
	   if (count($limitsDictionary["$parameter"])<2) {
          $tmppar = $limitsDictionary["$parameter"];
              $paramArray .= $DClimitsM1["$tmppar"].", ";
   }else {
                  foreach($limitsDictionary["$parameter"] as $sublist ){
                          $paramArray .= $DClimitsM1["$sublist"].", ";
                              }
   }}
    $limitArray =  rtrim($paramArray,", ")."]";
// M2
  $paramArray2 = "[";
  if (isset($_POST['$parameter']))
  {
    $parameter = $ltm_params[$currentpage];
    if (count($limitsDictionary["$parameter"])<2) {
          $tmppar = $limitsDictionary["$parameter"];
              $paramArray2 .= $DClimitsM2["$tmppar"].", ";
            } else {
                  foreach($limitsDictionary["$parameter"] as $sublist ){
                          $paramArray2 .= $DClimitsM2["$sublist"].", ";
                              }
  }}
      $limitArray2 =  rtrim($paramArray2,", ")."]";
//---------------------------------------



// Forming the plot data arrays, which will be directly fed to dygraphs

$newthing = "[";
// while there are rows to be fetched...
while ($list = mysqli_fetch_assoc($result)) {
   $newthing .= "[ new Date(\"".$list['date']."\"),[".$list['mean'].", ".$list['rms']."]],";
   //echo "+";
} // end while
$plotdata = rtrim($newthing,",")."]";


$newthing2   = "[";
$newregress2 = "[";
// while there are rows to be fetched...
while ($list = mysqli_fetch_assoc($result2)) {
   $newthing2   .= "[ new Date(\"".$list['date']."\"),[".$list['mean'].", ".$list['rms']."]],";
   $newregress2 .= "[ ".$list['date'].", ".$list['mean']."],";
} // end while
$plotdata2 = rtrim($newthing2,",")."]";
$regressiondata2 = rtrim($newregress2,",")."]";

$newthing3 = "[";
// while there are rows to be fetched...
while ($list = mysqli_fetch_assoc($result3)) {
   $newthing3 .= "[ new Date(\"".$list['date']."\"),[".$list['mean'].", ".$list['rms']."]],";
} // end while
$plotdata3 = rtrim($newthing3,",")."]";

$newthing4 = "[";
// while there are rows to be fetched...
while ($list = mysqli_fetch_assoc($result4)) {
   $newthing4 .= "[ new Date(\"".$list['date']."\"),[".$list['mean'].", ".$list['rms']."]],";
} // end while
$plotdata4 = rtrim($newthing4,",")."]";


/******  build the pagination links ******/
// range of num links to show
$range = 3;

$linksstring="";
// if not on page 1, don't show back links
if ($currentpage > 1) {
   // show << link to go back to page 1
   //echo " <a href='{$_SERVER['PHP_SELF']}?currentpage=1'><<</a> ";
   $linksstring.=" <a href='{$_SERVER['PHP_SELF']}?currentpage=1' ><<</a> ";
   // get previous page num
   $prevpage = $currentpage - 1;
   // show < link to go back to 1 page
   //echo " <a href='{$_SERVER['PHP_SELF']}?currentpage=$prevpage'><</a> ";
   $linksstring.=" <a href='{$_SERVER['PHP_SELF']}?currentpage=$prevpage'><</a> ";
} // end if 

// loop to show links to range of pages around current page
for ($x = ($currentpage - $range); $x < (($currentpage + $range) + 1); $x++) {
   // if it's a valid page number...
   if (($x > 0) && ($x <= $totalpages)) {
      // if we're on current page...
      if ($x == $currentpage) {
         // 'highlight' it but don't make a link
         //echo " [<b>$x</b>] ";
         $linksstring.= " [<b>$x</b>] ";
      // if not current page...
      } else {
         // make it a link
         //echo " <a href='{$_SERVER['PHP_SELF']}?currentpage=$x'>$x</a> ";
         $linksstring.= " <a href='{$_SERVER['PHP_SELF']}?currentpage=$x'>$x</a> ";
      } // end else
   } // end if 
} // end for
                 
// if not on last page, show forward and last page links        
if ($currentpage != $totalpages) {
   // get next page
   $nextpage = $currentpage + 1;
    // echo forward link for next page 
   //echo " <a href='{$_SERVER['PHP_SELF']}?currentpage=$nextpage'>></a> ";
   $linksstring.= " <a href='{$_SERVER['PHP_SELF']}?currentpage=$nextpage'>></a> ";
   // echo forward link for lastpage
   //echo " <a href='{$_SERVER['PHP_SELF']}?currentpage=$totalpages'>>></a> ";
   $linksstring.= " <a href='{$_SERVER['PHP_SELF']}?currentpage=$totalpages'>>></a> ";
} // end if
/****** end build pagination links ******/
?>

<html>
 <head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
<!-- <script type="text/javascript"  src="js/dygraph-combined.js"></script>-->
<script src="//cdnjs.cloudflare.com/ajax/libs/dygraph/1.1.1/dygraph-combined.js"></script>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="css/2bootstrap.min.css">
<!-- Optional theme -->
<link rel="stylesheet" href="css/grid.css">
<!-- Latest compiled and minified JavaScript -->
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</head>
 <body>
 <div class="pageHeader" style="background-color: #000">
     <p class="lead" style="color: #fff">
        <IMG SRC="MAGIC logo black.png" ALT="MAGIC logo" WIDTH=30 HEIGHT=30>  MAGIC Long Term Monitoring </p>
     <p class="lead" style="color: #fff"> 
	 <div class="graphTitles">
        <?php echo $graphtitles["$ltm_params[$currentpage]"];?>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
		<div class="drop-down">
		<select id="selectParam">
														<option value="selectparam1" selected="" >Select parameter</option>
														<option class ="parameter" value="calq_cal">1.Calibration runs: Calibration Charge</option>
														<option class ="parameter" value="npe_int">2.Interleaved runs: Number of Photoelectrons</option>
														<option class ="parameter" value="cfact_int">3.Interleaved runs: C Factor</option>
														<option class ="parameter" value="arrtm_cal">4.Calibration runs: Arrival Time</option>
														<option class ="parameter" value="arrtmrms_cal">5.Calibration runs: Arrival Time RMS</option>
														<option class ="parameter" value="pix1041">6.Calibration laser monitoring diode, pix1041</option>
														<option class ="parameter" value="muon_psf">7.PSF from muons</option>
														<option class ="parameter" value="muon_size">8.Mean muon size</option>
														<option class ="parameter" value="sbigpsf_b">9.PSF from SBig, B filter</option>
														<option class ="parameter" value="sg_devaz">10.Azimuthal Misspointing*Sin(Zenith)</option>
														<option class ="parameter" value="sg_devzd">11.Zenith Misspointing</option>
														<option class ="parameter" value="sg_camcx">12.Camera Centre X</option>
														<option class ="parameter" value="sg_camcy">13.Camera Centre Y</option>
														<option class ="parameter" value="campixtemp_daq">14.Pixel Temperature Camera, DAQ data</option>
														<option class ="parameter" value="rec_temp">15.Recievers Temperature</option>
														<option class ="parameter" value="camlv1temp">16.LV1 Temperature</option>
														<option class ="parameter" value="camlv2temp">17.LV2 Temperature</option>
														<option class ="parameter" value="camlv1hum">18.LV1 Humidity</option>
														<option class ="parameter" value="camlv2hum">19.LV2 Humidity</option>
														<option class ="parameter" value="camcoolchasiasftopleft">20.Camera Cooling, ChasiasFTopLeft Temperature</option>
														<option class ="parameter" value="camcoolfrontbottright">21.Camera Cooling: FrontBottRight Humidity</option>
														<option class ="parameter" value="sumt_cbt1">22.Sum-Trigger-II Clip board temperatures 1</option>
														<option class ="parameter" value="sumt_cbt2">23.Sum-Trigger-II Clip board temperatures 2</option>
														<option class ="parameter" value="sumt_astrob">24.Sum-Trigger-II Astro-board temperature</option>
														<option class ="parameter" value="sumt_rack">25.Cooling: Heat exchangers internal temperatures</option>
														<option class ="parameter" value="calbtemp1">26.Calibration Box Temperature</option>
														<option class ="parameter" value="calbtemp2">27.Calibration Box Temperature, next to heating plate</option>
														<option class ="parameter" value="calbhum">28.Calibration Box Humidity</option>
														
												
						
					</select></div>
      <div id="links"> <?php echo $linksstring; ?> </div>

     </p>
 </div>
</div>

<p></p> 


<div class="main-wrap container">
<div class="container">

 <div class="row" style="background-color: rgba(86,61,124,.15)">
   <div class="col-md-6" >   M1: 1 year (to today)   </div>
   <div class="col-md-6" >   M1: 1 month (to today)  </div>
 </div>

 <div class="row">
   <div class="col-md-6" >      
       <div id="graphdiv1"></div>
       <div style="text-align:center; width: 480px">
          <button style="color: green;" id="ry1">Regression</button>
          <button id="clear1">Clear Line</button>
          <div id="list1"></div>
       </div>
   </div>

   <div class="col-md-6">
      <div id="graphdiv2"></div>
       <div style="text-align:center; width: 480px">
          <button style="color: green;" id="ry2">Regression</button>
          <button id="clear2">Clear Line</button>
          <div id="list2"></div>
       </div>
   </div>

 </div>

 <div class="row" style="background-color: rgba(86,61,124,.15)">
   <div class="col-md-6" >   M2: 1 year (to today)   </div>
   <div class="col-md-6" >   M2: 1 month (to today)  </div>
 </div>

 <div class="row">
   <div class="col-md-6" >
      <div id="graphdiv3"></div>
       <div style="text-align:center; width: 480px">
          <button style="color: green;" id="ry3">Regression</button>
          <button id="clear3">Clear Line</button>
          <div id="list3"></div>
       </div>
   </div>

   <div class="col-md-6">
      <div id="graphdiv4"></div>
       <div style="text-align:center; width: 480px">
          <button style="color: green;" id="ry4">Regression</button>
          <button id="clear4">Clear Line</button>
          <div id="list4"></div>
       </div>
   </div>

 </div>

 <div >
     <span class="dyhelp"> <b> HOVER</b> over the graph to display values for specific dates</span>
                         </br>
     <span class="dyhelp"><b>CLICK AND DRAG</b> on the graph to zoom in on a specific date or y-value range</span>
                         </br>
     <span class="dyhelp"><b>DOUBLE CLICK</b> to reset to the default date range</span>
 </div>

</div>
</div>

<script type="text/javascript">


$('#selectParam').change(function() {
    var selectedValue=$(this).val();
	switch(selectedValue){
		case "calq_cal":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=1'
		break;
		case "npe_int":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=2'
		break;
		case "cfact_int":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=3'
		break;
		case "arrtm_cal":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=4'
		break;
		case "arrtmrms_cal":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=5'
		break;
		case "pix1041":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=6'
		break;
		case "muon_psf":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=7'
		break;
		case "muon_size":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=8'
		break;
		case "sbigpsf_b":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=9'
		break;
		case "sg_devaz":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=10'
		break;
		case "sg_devzd":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=11'
		break;
		case "sg_camcx":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=12'
		break;
		case "sg_camcy":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=13'
		break;
		case "campixtemp_daq":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=14'
		break;
		case "rec_temp":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=15'
		break;
		case "camlv1temp":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=16'
		break;
		case "camlv2temp":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=17'
		break;
		case "camlv1hum":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=18'
		break;
		case "camlv2hum":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=19'
		break;
		case "camcoolchasiasftopleft":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=20'
		break;
		case "camcoolfrontbottright":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=21'
		break;
		case "sumt_cbt1":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=22'
		break;
		case "sumt_cbt2":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=23'
		break;
		case "sumt_astrob":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=24'
		break;
		case "sumt_rack":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=25'
		break;
		case "calbtemp1":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=26'
		break;
		case "calbtemp2":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=27'
		break;
		case "calbhum":
		self.location='<?php echo ($_SERVER['PHP_SELF']); ?>?currentpage=28'
		break;

		
		default:
		break;
	}
   
});



function singleErrorPlotter(e) {
  var ctx = e.drawingContext;
  var points = e.points;
  var g = e.dygraph;
  var color = e.color;
  ctx.save();
  ctx.strokeStyle = e.color;
  ctx.lineWidth = 0.8;
    
  for (var i = 0; i < points.length; i++) {
    var p = points[i];
    var center_x = p.canvasx;
    if (isNaN(p.y_bottom)) continue;

    var low_y = g.toDomYCoord(p.yval_minus),
        high_y = g.toDomYCoord(p.yval_plus);

    ctx.beginPath();
    ctx.moveTo(center_x, low_y);
    ctx.lineTo(center_x, high_y);
    ctx.stroke();
  }

  ctx.restore();
}


$(document).ready(function () {

   var regression, clearLines, writeslope;  // defined below
   var g1,g2,g3,g4;
   var coeffs =  null;

   // get limits from php, then convert string to array of numbers
   var limitsArray1 = JSON.parse("<?php echo $limitArray;?>");
   var limitsArray2 = JSON.parse("<?php echo $limitArray2;?>");

   document.getElementById("ry1").onclick   = function() { regression(g1); writeslope(1,coeffs); };
   document.getElementById("clear1").onclick = function() { clearLines(g1); };
   document.getElementById("ry2").onclick   = function() { regression(g2); writeslope(2,coeffs); };
   document.getElementById("clear2").onclick = function() { clearLines(g2); };
   document.getElementById("ry3").onclick   = function() { regression(g3); writeslope(3,coeffs); };
   document.getElementById("clear3").onclick = function() { clearLines(g3); };
   document.getElementById("ry4").onclick   = function() { regression(g4); writeslope(4,coeffs); };
   document.getElementById("clear4").onclick = function() { clearLines(g4); };

  regression = function(g) {
     //var htmlslope = "";
     // Only run the regression over visible points.
     var range = g.xAxisRange();
     var sum_xy = 0.0, sum_x = 0.0, sum_y = 0.0, sum_x2 = 0.0, num = 0;
     for (var i = 0; i < g.numRows(); i++) {
        var x = g.getValue(i, 0);
        if (x < range[0] || x > range[1]) continue;

        var y = g.getValue(i, 1)[0];
        if (y === null || y === undefined) continue;
        if (y.length == 2) {
            // using fractions
            y = y[0] / y[1];
          }

          num++;
          sum_x += x;
          sum_y += y;
          sum_xy += x * y;
          sum_x2 += x * x;
        }

        var a = (sum_xy - sum_x * sum_y / num) / (sum_x2 - sum_x * sum_x / num);
        var b = (sum_y - a * sum_x) / num;

        coeffs = [b, a];
        if (typeof(console) != 'undefined') {
          console.log("g.getvalue(1,0) " , g.getValue(2, 0));
          console.log("g.getvalue(1,1) " , g.getValue(2, 1)[0]);
          console.log("coeffs: [" + b + ", " + a + "]");
        }

        g.updateOptions({});  // forces a redraw.

        // add text with regression slope
        //gnumber
        //var listname = "list"+gnumber;
        //htmlslope += "<span id='ohoho'> slope="+a*1000*3600*24+"/day</span></br>";
        //document.getElementById("list").innerHTML = htmlslope;
        //targetDiv.innerHTML = htmlslope;
      };

      clearLines = function(g) {
         coeffs = null;
         g.updateOptions({});
      };


      function drawLines(ctx, area, g) {
          //console.log("layout type " ,typeof(g));
          //console.log("layout type " ,g);
          //console.log("xaxis " ,g.xAxisRange());
         
        
 
        if (typeof(g) == 'undefined') return;  // won't be set on the initial draw.
        //dyg = this.dygraph;
        var range = g.xAxisRange();

        if (typeof(console) != 'undefined') {
          //console.log("range " ,range);
        }

        var x1 = range[0];
        var x2 = range[1];

        // Find out if graph g refers to M1 or M2, by getting the div element's id
          var gProps = Object.getOwnPropertyNames(g);
          for (var i = 0; i < gProps.length; i++) {
                      var propName = gProps[i];
                        }
            var str = g[gProps[3]];
          var strid = str.id;
          if (String.prototype.includes){
            if (strid.includes("graphdiv1") || strid.includes("graphdiv2")){ 
               var  limitsArray = limitsArray1;
            } else if (strid.includes("graphdiv3") || strid.includes("graphdiv4")) {
               var  limitsArray = limitsArray2;
            }
          } else { 
             if (strid.contains("graphdiv1") || strid.contains("graphdiv2")){ 
                var  limitsArray = limitsArray1;
             } else if (strid.contains("graphdiv3") || strid.contains("graphdiv4")) {
                var  limitsArray = limitsArray2;
             }
          }
         
         for (var i = 0; i < limitsArray.length; i++) {
             var y3 = limitsArray[i];
             var y4 = limitsArray[i];
             var p3 = g.toDomCoords(x1, y3);
             var p4 = g.toDomCoords(x2, y4);
             var colorlimit = 'rgb(218,69,237)';
             ctx.save();
             ctx.strokeStyle = colorlimit;
             ctx.setLineDash([5, 10]);
             ctx.lineWidth = 1.5;
             ctx.beginPath();
             ctx.moveTo(p3[0], p3[1]);
             ctx.lineTo(p4[0], p4[1]);
             ctx.closePath();
             ctx.stroke();
             ctx.restore();
         }


          if (coeffs) {  
             var a = coeffs[1];
             var b = coeffs[0];

             var y1 = a * x1 + b;
             var y2 = a * x2 + b;

             var p1 = g.toDomCoords(x1, y1);
             var p2 = g.toDomCoords(x2, y2);

             var c = Dygraph.toRGB_(g.getColors());
             c.r = Math.floor(255 - 0.5 * (255 - c.r));
             c.g = Math.floor(255 - 0.5 * (255 - c.g));
             c.b = Math.floor(255 - 0.5 * (255 - c.b));
             c.r = 245; //255 - c.r;
             c.g = 71; //255 - c.g;
             c.b = 71; //255 - c.b;
             var color = 'rgb(' + c.r + ',' + c.g + ',' + c.b + ')';
             ctx.save();
             ctx.strokeStyle = color;
             ctx.lineWidth = 1.5;
             ctx.beginPath();
             ctx.moveTo(p1[0], p1[1]);
             ctx.lineTo(p2[0], p2[1]);
             ctx.closePath();
             ctx.stroke();
             ctx.restore();
          } //if coeffs
      }


     function writeslope(num,coeffs){
            if (!coeffs) return;
        // add text with regression slope
        var htmlslope = "";
        var listname = "list"+num;
        //console.log("list id " ,listname);
        //console.log("slope " ,coeffs[1]*1000*3600*24);
        htmlslope += "<span id='ohoho'> slope = "+(coeffs[1]*1000*3600*24).toPrecision(3)+" / day</span></br>";
        document.getElementById(listname).innerHTML = htmlslope;
     }


       g4 = new Dygraph(
             document.getElementById("graphdiv4"), 
             <?php echo $plotdata4;?>,
            {
               strokeWidth: 0.2,
               pointSize: 2,
               digitsAfterDecimal: 3,
               drawPoints: true,
               highlightCircleSize: 4,
               labels: [ "Date", " <?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ],
               xlabel:  "Date",
               ylabel:  "<?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ,
               underlayCallback: drawLines,
               errorBars: true,
               includeZero: true,
               sigma: 1.0,
          connectSeparatedPoints: false,
          plotter: [
            singleErrorPlotter,
            Dygraph.Plotters.linePlotter
          ]
             }
        );

       g3 = new Dygraph(
             document.getElementById("graphdiv3"), 
             <?php echo $plotdata3;?>,
             {
               strokeWidth: 0.2,
               pointSize: 2,
               digitsAfterDecimal: 3,
               drawPoints: true,
               highlightCircleSize: 4,
               labels: [ "Date", " <?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ],
               xlabel:  "Date",
               ylabel:  "<?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ,
               underlayCallback: drawLines,
               errorBars: true,
               includeZero: true,
               sigma: 1.0,
          connectSeparatedPoints: false,
          plotter: [
            singleErrorPlotter,
            Dygraph.Plotters.linePlotter
          ]
             }
        );

       g2 = new Dygraph(
             document.getElementById("graphdiv2"), 
             <?php echo $plotdata2;?>,
             {
               strokeWidth: 0.2,
               pointSize: 2,
               digitsAfterDecimal: 3,
               drawPoints: true,
               highlightCircleSize: 4,
               labels: [ "Date", " <?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ],
               xlabel:  "Date",
               ylabel:  "<?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ,
               underlayCallback: drawLines,
               errorBars: true,
               includeZero: true,
               sigma: 1.0,
          connectSeparatedPoints: false,
          plotter: [
            singleErrorPlotter,
            Dygraph.Plotters.linePlotter
          ]
             }
        );

       g1 = new Dygraph(
             document.getElementById("graphdiv1"), 
             <?php echo $plotdata;?>,
             {
               strokeWidth: 0.2,
               pointSize: 2,
               digitsAfterDecimal: 3,
               drawPoints: true,
               highlightCircleSize: 4,
               labels: [ "Date", " <?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ],
               xlabel:  "Date",
               ylabel:  "<?php echo $graphtitles["$ltm_params[$currentpage]"];?>" ,
               underlayCallback: drawLines,
               errorBars: true,
               includeZero: true,
               sigma: 1.0,
               connectSeparatedPoints: false,
               plotter: [
                   singleErrorPlotter,
                   Dygraph.Plotters.linePlotter
               ],
             }
        );
    });
</script>



</body>

</html>
