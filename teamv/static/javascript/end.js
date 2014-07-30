function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));

$(document).ready(function(){
                 // For End Meeting button

    var meeting = getParameterByName('meeting');
    var form = document.getElementById("end_meeting");
    var m_num = document.createElement('input');
    m_num.type = 'hidden';
    m_num.name = 'meeting';
    m_num.value = meeting;
    form.action = '/end?meeting=' + meeting;
    form.appendChild(m_num);

    return false;
});
/*
$(document).ready(function(){
    var socket = io.connect('/chat');
    $("#end_meeting").submit(function(e) {
	var meeting = getparameterByName('meeting');
        e.preventDefault();
        socket.emit("end", meeting)
        return false;
    });

    socket.on("end", function(e) {
        window.location.replace("/?meeting=" + e);
    });
});
*/
