<!DOCTYPE html>
<%@ page language="java" import="net.sf.json.JSONObject"%>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <title>SB Admin - Start Bootstrap Template</title>
  <%String path=request.getContextPath();%>
  <!-- Bootstrap core CSS-->
  <link href="<%=path%>/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom fonts for this template-->
  <link href="<%=path%>/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
  <!-- Page level plugin CSS-->
  <link href="<%=path%>/vendor/datatables/dataTables.bootstrap4.css" rel="stylesheet">
  <!-- Custom styles for this template-->
  <link href="<%=path%>/css/sb-admin.css" rel="stylesheet">
</head>

<body class="fixed-nav sticky-footer bg-dark" id="page-top">
  <!-- Navigation-->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
    <a class="navbar-brand" href="index.html">Start Bootstrap</a>
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <ul class="navbar-nav navbar-sidenav" id="exampleAccordion">
        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Dashboard">
          <a class="nav-link" href="index.html">
            <i class="fa fa-fw fa-dashboard"></i>
            <span class="nav-link-text">Dashboard</span>
          </a>
        </li>
<!--        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Charts">
          <a class="nav-link" href="charts.html">
            <i class="fa fa-fw fa-area-chart"></i>
            <span class="nav-link-text">Charts</span>
          </a>
        </li>
        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Tables">
          <a class="nav-link" href="tables.html">
            <i class="fa fa-fw fa-table"></i>
            <span class="nav-link-text">Tables</span>
          </a>
        </li>-->
        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Stocks">
          <a class="nav-link nav-link-collapse collapsed" data-toggle="collapse" href="#collapseComponents" data-parent="#exampleAccordion">
            <i class="fa fa-fw fa-wrench"></i>
            <span class="nav-link-text">Stocks</span>
          </a>
          <ul class="sidenav-second-level collapse" id="collapseComponents">
            <li>
              
                <form method="post" action="<%=path%>/servlet/Caller" name="predictionform">
                    <input type="hidden" name="optionStockSymbol" value="AMZN">
                    <input type="hidden" name="optionDailyPrice" value="close">
                    <input type="hidden" name="inputDate" value="50"> 
                </form>
                <a href="#AMZN" onclick="javascript:getprediction('AMZN')">AMZN</a>
                
                <% String data=(String)request.getSession().getAttribute("data");%> 
                <% String bayesian_close=(String)request.getSession().getAttribute("bayesian_close");%>
                <% String bayesian_open=(String)request.getSession().getAttribute("bayesian_open");%>
                <% String bayesian_high=(String)request.getSession().getAttribute("bayesian_high");%>
                <% String bayesian_low=(String)request.getSession().getAttribute("bayesian_low");%>
                <% String bayesian_acc=(String)request.getSession().getAttribute("bayesian_acc");%>
                <% String bayesian_rng=(String)request.getSession().getAttribute("bayesian_rng");%>
                <% String ann_close=(String)request.getSession().getAttribute("ann_close");%>
                <% String ann_high=(String)request.getSession().getAttribute("ann_high");%>
                <% String ann_open=(String)request.getSession().getAttribute("ann_open");%>
                <% String ann_low=(String)request.getSession().getAttribute("ann_low");%>
                <% String ann_acc=(String)request.getSession().getAttribute("ann_acc");%>
                <% String ann_rng=(String)request.getSession().getAttribute("ann_rng");%>                                                
                <% String lstm_close=String.valueOf(request.getSession().getAttribute("lstm_close")); %>
                <% String lstm_open=String.valueOf(request.getSession().getAttribute("lstm_open"));%>
                <% String lstm_high=String.valueOf(request.getSession().getAttribute("lstm_high"));%>
                
                <% String lstm_low=String.valueOf(request.getSession().getAttribute("lstm_low"));%>
                <% String lstm_rng=String.valueOf(request.getSession().getAttribute("lstm_rng"));%>   
                <% String stocksymbol=(String)request.getSession().getAttribute("stocksymbol");%>
                <% String real_time=(String)request.getSession().getAttribute("real_time");%>
                <% String real_open=(String)request.getSession().getAttribute("real_open");%>
                <% String real_close=(String)request.getSession().getAttribute("real_close");%>
                <% String real_high=(String)request.getSession().getAttribute("real_high");%>
                <% String real_low=(String)request.getSession().getAttribute("real_low");%>
                <% String real_volume=(String)request.getSession().getAttribute("real_volume");%>
                <% String highest=(String)request.getSession().getAttribute("highest_close");%>
                <% String lowest=(String)request.getSession().getAttribute("lowest_close");%>
                <% String rec=(String)request.getSession().getAttribute("recommendation");%>
            </li>
            <li>
              <a href="#BABA" onclick="javascript:getprediction('BABA')">BABA</a>
            </li>
            <li>
              <a href="#BIDU" onclick="javascript:getprediction('BIDU')">BIDU</a>
            </li>
            <li>
              <a href="#FB" onclick="javascript:getprediction('FB')">FB</a>
            </li>
            <li>
              <a href="#GOOGL" onclick="javascript:getprediction('GOOGL')">GOOGL</a>
            </li>
            <li>
              <a href="#JD" onclick="javascript:getprediction('JD')">JD</a>
            </li>
            <li>
              <a href="#MSFT" onclick="javascript:getprediction('MSFT')">MSFT</a>
            </li>
            <li>
              <a href="#NVDA" onclick="javascript:getprediction('NVDA')">NVDA</a>
            </li>
            <li>
              <a href="#TSLA" onclick="javascript:getprediction('TSLA')">TSLA</a>
            </li>
            <li>
              <a href="#WB" onclick="javascript:getprediction('WB')">WB</a>
            </li>
          </ul>
        </li>
      </ul>
      <ul class="navbar-nav sidenav-toggler">
        <li class="nav-item">
          <a class="nav-link text-center" id="sidenavToggler">
            <i class="fa fa-fw fa-angle-left"></i>
          </a>
        </li>
      </ul>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle mr-lg-2" id="messagesDropdown" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="fa fa-fw fa-envelope"></i>
            <span class="d-lg-none">Messages
              <span class="badge badge-pill badge-primary">12 New</span>
            </span>
            <span class="indicator text-primary d-none d-lg-block">
              <i class="fa fa-fw fa-circle"></i>
            </span>
          </a>
          <div class="dropdown-menu" aria-labelledby="messagesDropdown">
            <h6 class="dropdown-header">New Messages:</h6>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">
              <strong>David Miller</strong>
              <span class="small float-right text-muted">11:21 AM</span>
              <div class="dropdown-message small">Hey there! This new version of SB Admin is pretty awesome! These messages clip off when they reach the end of the box so they don't overflow over to the sides!</div>
            </a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">
              <strong>Jane Smith</strong>
              <span class="small float-right text-muted">11:21 AM</span>
              <div class="dropdown-message small">I was wondering if you could meet for an appointment at 3:00 instead of 4:00. Thanks!</div>
            </a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">
              <strong>John Doe</strong>
              <span class="small float-right text-muted">11:21 AM</span>
              <div class="dropdown-message small">I've sent the final files over to you for review. When you're able to sign off of them let me know and we can discuss distribution.</div>
            </a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item small" href="#">View all messages</a>
          </div>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle mr-lg-2" id="alertsDropdown" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="fa fa-fw fa-bell"></i>
            <span class="d-lg-none">Alerts
              <span class="badge badge-pill badge-warning">6 New</span>
            </span>
            <span class="indicator text-warning d-none d-lg-block">
              <i class="fa fa-fw fa-circle"></i>
            </span>
          </a>
          <div class="dropdown-menu" aria-labelledby="alertsDropdown">
            <h6 class="dropdown-header">New Alerts:</h6>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">
              <span class="text-success">
                <strong>
                  <i class="fa fa-long-arrow-up fa-fw"></i>Status Update</strong>
              </span>
              <span class="small float-right text-muted">11:21 AM</span>
              <div class="dropdown-message small">This is an automated server response message. All systems are online.</div>
            </a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">
              <span class="text-danger">
                <strong>
                  <i class="fa fa-long-arrow-down fa-fw"></i>Status Update</strong>
              </span>
              <span class="small float-right text-muted">11:21 AM</span>
              <div class="dropdown-message small">This is an automated server response message. All systems are online.</div>
            </a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">
              <span class="text-success">
                <strong>
                  <i class="fa fa-long-arrow-up fa-fw"></i>Status Update</strong>
              </span>
              <span class="small float-right text-muted">11:21 AM</span>
              <div class="dropdown-message small">This is an automated server response message. All systems are online.</div>
            </a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item small" href="#">View all alerts</a>
          </div>
        </li>
        <li class="nav-item">
          <form class="form-inline my-2 my-lg-0 mr-lg-2">
            <div class="input-group">
              <input class="form-control" type="text" placeholder="Search for...">
              <span class="input-group-append">
                <button class="btn btn-primary" type="button">
                  <i class="fa fa-search"></i>
                </button>
              </span>
            </div>
          </form>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-toggle="modal" data-target="#exampleModal">
            <i class="fa fa-fw fa-sign-out"></i>Logout</a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="content-wrapper">
    <div class="container-fluid">
      <!-- Breadcrumbs-->
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="#">Dashboard</a>
        </li>
        <li class="breadcrumb-item active">My Dashboard</li>
      </ol>
      
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-table"></i> Realtime stock data</div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
              <thead>
                <tr>
                  <th>Last Update</th>
                  <th>open($)</th>
                  <th>close($)</th>
                  <th>high($)</th>
                  <th>low($)</th>
                  <th>volume</th>
<!--
                  <th>Start date</th>
                  <th>Salary</th>
-->
                </tr>
              </thead>
<!--
              <tfoot>
                <tr>
                  <th>Name</th>
                  <th>Position</th>
                  <th>Office</th>
                  <th>Age</th>
                  <th>Start date</th>
                  <th>Salary</th>
                </tr>
              </tfoot>
-->
              <tbody>
                <tr>
                  <td><%=real_time%></td>
                  <td><%=real_open%></td>
                  <td><%=real_close%></td>
                  <td><%=real_high%></td>
                  <td><%=real_low%></td>
                  <td><%=real_volume%></td>
<!--
                  <td>2011/04/25</td>
                  <td>$320,800</td>
-->
                </tr>
              </tbody>
            </table>
          </div>
        </div>
<!--        <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>-->
      </div>
    </div>
    
    
    
          <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-table"></i> statistic stock data</div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
              <thead>
                <tr>
                  <th> highest stock price in the last ten days</th>
                  <th>Lowest stock price in the latest one year</th>
                  <th>recommendation</th>
					
<!--
                  <th>Start date</th>
                  <th>Salary</th>
-->
                </tr>
              </thead>
<!--
              <tfoot>
                <tr>
                  <th>Name</th>
                  <th>Position</th>
                  <th>Office</th>
                  <th>Age</th>
                  <th>Start date</th>
                  <th>Salary</th>
                </tr>
              </tfoot>
-->
              <tbody>
                <tr>
                  <td><%=highest%></td>
                  <td><%=lowest%></td>
                  <td><%=rec%></td>
    
<!--
                  <td>2011/04/25</td>
                  <td>$320,800</td>
-->
                </tr>
              </tbody>
            </table>
          </div>
        </div>
<!--        <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>-->
      </div>
    </div>
      <!-- Area Chart Example-->
      
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-area-chart"></i> Area Chart Example</div>
        <div class="card-body">
          <canvas id="myAreaChart_test1" width="100%" height="30"></canvas>
        </div>
<!--        <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>-->
      </div>
      
      
      
            <!-- Area Chart Example-->
      
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-area-chart"></i> Volume</div>
        <div class="card-body">
          <canvas id="myVolumeChart_test1" width="100%" height="30"></canvas>
        </div>
<!--        <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>-->
      </div>
      <!-- Example DataTables Card-->
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-table"></i> Stock Price Prediction</div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
              <thead>
                <tr>
                  <th>Method Name</th>
                  <th>Open($)</th>
                  <th>Close($)</th>
                  <th>High($)</th>
                  <th>Low($)</th>
                  <th>Error(%)</th>
                  <th>fluctuation range($)</th>
<!--
                  <th>Start date</th>
                  <th>Salary</th>
-->
                </tr>
              </thead>
<!--
              <tfoot>
                <tr>
                  <th>Name</th>
                  <th>Position</th>
                  <th>Office</th>
                  <th>Age</th>
                  <th>Start date</th>
                  <th>Salary</th>
                </tr>
              </tfoot>
-->
              <tbody>
                <tr>
                  <td>Bayesian</td>
                  <td><%=bayesian_open%></td>
                  <td><%=bayesian_close%></td>
                  <td><%=bayesian_high%></td>
                  <td><%=bayesian_low%></td>
                  <td><%=bayesian_acc%></td>
                  <td><%=bayesian_rng%></td>
<!--
                  <td>2011/04/25</td>
                  <td>$320,800</td>
-->
                </tr>
              </tbody>
              
              <tbody>
                <tr>
                  <td>ANN</td>
                  <td><%=ann_open%></td>
                  <td><%=ann_close%></td>
                  <td><%=ann_high%></td>
                  <td><%=ann_low%></td>
                  <td><%=ann_acc%></td>
                  <td><%=ann_rng%></td>
<!--
                  <td>2011/04/25</td>
                  <td>$320,800</td>
-->
                </tr>
              </tbody>
              
 			<tbody>
                <tr>
                  <td>LSTM</td>
                  <td><%=lstm_open%></td>
                  <td><%=lstm_close%></td>
                  <td><%=lstm_high%></td>
                  <td><%=lstm_low%></td>
                  <td></td>
                  <td></td>
<!--
                  <td>2011/04/25</td>
                  <td>$320,800</td>
-->
                </tr>
              </tbody>
              
            </table>
          </div>
        </div>
<!--        <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>-->
      </div>
    </div>
    <!-- /.container-fluid-->
    <!-- /.content-wrapper-->
    <footer class="sticky-footer">
      <div class="container">
        <div class="text-center">
          <small>Copyright © Group8 2018</small>
        </div>
      </div>
    </footer>
    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fa fa-angle-up"></i>
    </a>
    <!-- Logout Modal-->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
            <button class="close" type="button" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">×</span>
            </button>
          </div>
          <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
          <div class="modal-footer">
            <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
            <a class="btn btn-primary" href="login.php">Logout</a>
          </div>
        </div>
      </div>
    </div>
    <!-- Bootstrap core JavaScript-->
    <script src="<%=path%>/vendor/jquery/jquery.min.js"></script>
    <script src="<%=path%>/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <!-- Core plugin JavaScript-->
    <script src="<%=path%>/vendor/jquery-easing/jquery.easing.min.js"></script>
    <!-- Page level plugin JavaScript-->
    <script src="<%=path%>/vendor/chart.js/Chart.min.js"></script>
    <script src="<%=path%>/vendor/datatables/jquery.dataTables.js"></script>
    <script src="<%=path%>/vendor/datatables/dataTables.bootstrap4.js"></script>
    <!-- Custom scripts for all pages-->
    <script src="<%=path%>/js/sb-admin.min.js"></script>
    <!-- Custom scripts for this page-->
    <script src="<%=path%>/js/sb-admin-datatables.min.js"></script>
    <script src="<%=path%>/js/sb-admin-charts.js"></script>
  </div>
  
  <script>
//	function testjs()
//	{
//		var jsdata = '<%=data %>';
//		
//		alert("testjs");
//		
//	}
	
//	function getprediction (stock) {
//		document.forms['AMZNprediction'].submit();
//		//updatechart (stock);
//	}
	
	function onloadfunction()
	{
        var obj = JSON.parse('<%=data%>');
        //alert("hit " + obj.toString());
        
        updatechart(window.location.hash, obj); // get #parameter
	}
	
	
	window.onload=onloadfunction;
</script>
</body>

</html>
