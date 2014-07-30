function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}



$(document).ready(function() {
    var socket = io.connect('/chat');

    var meeting = getParameterByName('meeting');
    var nickname = getParameterByName('nickname');

    socket.on('connect', function() {
        $("#chatlog").append(nickname + " has connected\n");
    	chatlog.scrollTop = chatlog.scrollHeight;
    });

    socket.emit("join", meeting);
    socket.emit("nickname", nickname);

    var chatlog = document.getElementById('chatlog');

    // Compatibility Check

    if (!('webkitSpeechRecognition' in window)) {
	    upgrade();
    } 	
    window.SpeechRecognition = window.SpeechRecognition       ||
                               window.webkitSpeechRecognition ||
                               null;
 
    if (window.SpeechRecognition === null) {
        document.getElementById('ws-unsupported').classList.remove('hidden');
        document.getElementById('stop_listening').setAttribute('disabled', 'disabled');
        document.getElementById('start_listening').setAttribute('disabled', 'disabled');
    } else {
        var recognition = new window.webkitSpeechRecognition();
   
        recognition.continuous = true;
        recognition.onresult = function(event) {
            for(var i = event.resultIndex; i < event.results.length; i++){
        	    if(event.results.length > 0){
        	        chatbox.value = event.results[i][0].transcript;
        	        $('#chat_form').submit();
        	    }
            }
        };
    }
    
 
    $(window).bind("beforeunload", function() {
        socket.disconnect();
    });

	   
    $('#start_listening').on('click', function(){
	if(document.getElementById('start_listening').className.indexOf("recording_off") > -1)
	{
		recognition.stop();

	}
	else
	{
		recognition.start();
	} 
	       

    });

	
    $('.recording_on').on('click', function() {
	    recognition.stop();
    });

    socket.on("chat", function(e) {
        $("#chatlog").append(e + "\n");
	    chatlog.scrollTop = chatlog.scrollHeight;
    });

    socket.on("user_disconnect", function(e) {
        $("#chatlog").append(e + " has disconnected\n");
    	chatlog.scrollTop = chatlog.scrollHeight;
    });

    socket.on("user_connect", function(e) {
        $("#chatlog").append(e + " has connected\n");
    	chatlog.scrollTop = chatlog.scrollHeight;
    });

    $("#chat_form").submit(function(e) {
        e.preventDefault();
        var val = $("#chatbox").val();
        socket.emit("chat", val);
        $("#chatbox").val("");
        $("#chatlog").append(nickname + ": " + val + "\n");

    });

    $("#end_meeting").submit(function(e) {
       // var meeting = getparameterByName('meeting');
        e.preventDefault();
        socket.emit("end", meeting)
        return false;
    });

    socket.on("end", function(e) {
        window.location.replace("/?meeting=" + e);
    });

    function toggle(el){
   if(el.className=="recording_off")
    {
        el.src='/static/images/recording_on.png';
        el.className="recording_on";
		el.title='Recording';
	
	
    }
    else if(el.className=="recording_on")
    {      
	el.src='/static/images/recording_off.png';
        el.className="recording_off";
		el.title='Idle';
	

    }

    return false;
}  




});



