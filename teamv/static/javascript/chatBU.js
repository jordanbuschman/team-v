$(document).ready(function() {
    var socket = io.connect('/chat');//, {secure: true});

// get Username

    var username = prompt("Enter screen name", "Anonymous User");

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
	    chatbox.value = username+" : "+event.results[i][0].transcript;
	    $('#chat_form').submit();
	    }
	}
    };
    }
    
   $('#stop_listening').on('click', function(){
	recognition.stop();
   });

   $('#start_listening').on('click', function() {
	recognition.start();
    });

    $(window).bind("beforeunload", function() {
        socket.disconnect();
    });

    socket.on("chat", function(e) {
        $("#chatlog").append(e + "\n");
	chatlog.scrollTop = chatlog.scrollHeight;
    });

    socket.on("user_disconnect", function() {
        $("#chatlog").append("> User disconnected" + "\n");
    	chatlog.scrollTop = chatlog.scrollHeight;
    });

    socket.on("user_connect", function() {
        $("#chatlog").append("> User connected" + "\n");
    	chatlog.scrollTop = chatlog.scrollHeight;
    });


    $("#chat_form").submit(function(e) {
        e.preventDefault();
        var val = $("#chatbox").val();
        socket.emit("chat", val);
        $("#chatbox").val("");
    });

});
