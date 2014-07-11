$(document).ready(function() {
    var socket = io.connect('/chat');

    if (!('webkitSpeechRecognition' in window)) {
	  upgrade();
    } 	

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
        $("#chatlog").append(e + "<br />");
    });

    socket.on("user_disconnect", function() {
        $("#chatlog").append("user disconnected" + "<br />");
    });

    socket.on("user_connect", function() {
        $("#chatlog").append("user connected" + "<br />");
    });


    $("#chat_form").submit(function(e) {
        e.preventDefault();
        var val = $("#chatbox").val();
        socket.emit("chat", val);
        $("#chatbox").val("");
    });

});
