<!DOCTYPE html>
<%inherit file="wrapper.mak" />

<%block name="includes">
    % if meeting is not None and nickname is not None:
        <script type="text/javascript" src="/static/javascript/chat.js"></script>
    % endif
</%block>

% if meeting is None or nickname is None:
   <!-- <form name="enter_meeting" method="GET" action="/">
        <p>Enter your nickname and meeting number</p>
        Nickname: <input type="text" name="nickname" placeholder="&quot;Jim Smith&quot;"><br/>
        Meeting number: <input type="text" name="meeting" placeholder="&quot;12345678&quot;"><br/>
        <input type="submit" value="Submit">
    </form> -->

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/static/images/favicon.ico">

    <title>Signin</title>

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
      <form name="enter_meeting" method="GET" action="/" class="form-signin" role="form">
        <h2 class="form-signin-heading">Join a WebEx Meeting</h2><h3></h3>
        <input name="nickname" type="name" class="form-control" placeholder="Name" required autofocus>
        <input name="meeting" type="meeting_number" class="form-control" placeholder="Meeting Number" required>
  <!--      <input type="meeting_password" class="form-control" placeholder="Meeting Password" required> -->
		<!--
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
		-->
		<h3></h3>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Join</button>
      </form>
    
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
  </body>
</html>


% else:

<html lang="en">
  <head>
    <meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Team Valente</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
	<link rel="icon" href="/static/images/favicon.ico">

    <!-- Le styles -->
    <link href="static/css/bootstrap.min.css" rel="stylesheet">
	<link href="/static/css/dashboard.css" rel="stylesheet">
  </head>

  <body>
    <div id="wrap"><div id="main_global">
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href=""><img src="/static/images/Team_Valente_Webex_2.png" alt="Team Valente"></a>
        </div>
  
   
    
     
      
		<div class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <a style="position: relative; top: 20px; right: 16px;" href="/">Leave Meeting   <img src="/static/images/logout.png" width="30" height="30"></a>
          </ul>
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-2 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li id="link_home" class="active"><a href="#">Home</a></li>
            <li id="link_transcript"><a href="#">Transcript</a></li>
          </ul>
        </div>
        <div id="div_home" class="col-sm-7 col-sm-offset-2 col-md-7 col-md-offset-2 main">
	 <h3 class="sub-header"><input style="position: relative; top: 6px; left: 6px;" type="image" id="start_listening" src="/static/images/recording_off.png" title="Idle" class="recording_off" onclick="toggle(this);"/>&nbsp;&nbsp;Live Subtitles</h3>
                    <!-- <div class="row">
		     <img src="/static/images/Video.png" alt="Video">
          </div> -->
          
		  <dl class="dl-horizontal">
			<textarea id="chatlog" readonly="readonly"></textarea>
			<br />
			<form name = "chat_form"  id="chat_form">
				<input type="text" id="chatbox">
				<button type="submit" id="submit" >Send</button>
				<input type="button" id="start_listening" value="Start Listening" onclick="recognition.start()">
				<input type="button" id="stop_listening" value="Stop Listening" onclick="recognition.stop()"> 
			</form>
          </dl>
        </div>
		<div id="div_transcript" class="col-sm-7 col-sm-offset-2 col-md-7 col-md-offset-2 main">
          <h3 class="page-header">Transcript</h3>
	<input style="position: relative; top: 6px; left: 28px; bottom: 4px;" type="submit" class="btn btn-success" value="Retrieve Transcript"/><br></br>
			 <h3 class="page-header"></h3>
		  <dl class="dl-horizontal">


          </dl>
        </div>
        <div class="col-sm-3 col-sm-offset-9 col-md-3 col-md-offset-9 sidebar">
           <h3>Participants</h3><br height: .5em;>
		   <table class="table table-striped">
		      <thead></thead>
			  <tbody>
                 <tr>
                    <td>Shlomi Barsheshet</td>
                   
                 </tr>
				 <tr>
                    <td>Michael Brunger</td>
                  
                 </tr>
				 <tr>
                    <td>Jordan Buschman</td>
                 
                 </tr>
				 <tr>
                    <td>Teddy Chivetta</td>
                
                 </tr>
				 <tr>
                    <td>Rahul Daware</td>
               
                 </tr>
                 <tr>
                    <td>Andrew Green</td>
              
                 </tr>
				 <tr>
                    <td>Pratik Pankaj</td>
             
                 </tr>
				 <tr>
                    <td>Harika Sabella</td>
                 
                 </tr>
				 <tr>
                    <td>JL Valente</td>
                
                 </tr>
				 <tr>
                    <td>Jose Vega</td>
               
                 </tr>
			  </tbody>
           </table>
        </div>
      </div>
	</div></div>
    </div>
	<!--
	<div class="navbar navbar-fixed-bottom">
	<div class="navbar-inner">
	  <div class="container">
        <p class="muted credit"><center>&copy; 2014 Cisco and/or its affiliates. All rights reserved.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.webex.com"><img src="cisco_logo.png" width="70" height="35" alt="Cisco Logo"></a></center></p>
      </div>
	</div>
	</div>
	-->
	
	<div class="footer">
	  <div class="container">
        <p class="muted credit"><center>&copy; 2014 Cisco and/or its affiliates. All rights reserved.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.webex.com"><img src="/static/images/cisco_logo.png" width="70" height="35" alt="Cisco Logo"></a></center></p>
      </div>
	</div>

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script src="/static/javascript/bootstrap.min.js"></script>
	<script src="/static/javascript/myjs.js"></script>
	<script>$(document).ready(function(){$('#div_transcript').hide();$('#link_transcript').click(function(){$('#div_home').hide();$('#div_transcript').show();});$('#link_home').click(function(){$('#div_transcript').hide();$('#div_home').show();});});</script>
	<script>$(document).ready(function(){$('ul.nav > li').click(function(e){e.preventDefault();$('ul.nav > li').removeClass('active');$(this).addClass('active');});});</script>
  </body>
</html>



    
    
    <span id="ws-unsupported" class="hidden">API not supported</span>
% endif
