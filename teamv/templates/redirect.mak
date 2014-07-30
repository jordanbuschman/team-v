<%inherit file="wrapper.mak" />

<html lang="en">
 <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/static/images/favicon.ico">

    <title>Meeting Ended</title>

  </head>

  <body>
    <div id="wrap">
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href=""><img src="/static/images/Cisco_Webex_Logo2.jpg" alt="Cisco WebEx"></a>
        </div>
      </div>
    </div>

    <div class="container">
        <br/><br/><br/>
	
	    <h2 class="form-signin-heading">This meeting has ended.</h2><h3></h3>
	    <br>
	    <div id = 'link_area'></div> <br><br><br>

     </div> <!-- /container -->
        </div>
        <div class="navbar navbar-fixed-bottom">
          <div class="container">
        <p class="muted credit"><center>&copy; 2014 Cisco and/or its affiliates. All rights reserved.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.webex.com"><img src="/static/images/cisco_logo2.png" width="70" height="35" alt="Cisco Logo"></a></center></p>
      </div>
        </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="/static/javascript/bootstrap.min.js"></script>

    <script>$(document).ready(function(){
	
	function getParameterByName(name) {
            name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
            var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
            results = regex.exec(location.search);
            return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
	}
	
	var meeting = getParameterByName('meeting')
	var div = document.getElementById('link_area')
	var link = document.createElement('a');
	link.href = "logs/" + meeting;
	link.innerHTML = "The transcript for meeting #" + meeting + " may be viewed here.";
	div.appendChild(link);
	br = document.createElement('br');
        div.appendChild(br);
        return false;
    });</script>

  </body>
</html>

