$(document).ready(function() {
    var socket = io.connect('/chat');

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

    $("#join").click(function(e) {
      socket.emit('join', 'test')
    })
});
