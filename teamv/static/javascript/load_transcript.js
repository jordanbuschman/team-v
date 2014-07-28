

function getURLParameter(name) {
  return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
}

function load_trans(){
	var meeting_num = getURLParameter("meeting");
	var filename = "log_" + meeting_num + ".log";
	// filename is not used yet, since logs aren't on s3 yet.	
	$.ajax({
		type: "GET", url: "https://s3-us-west-1.amazonaws.com/teamvlogfiles/down_file.txt", data: {},	
		crossDomian: true,
		success: function(data){
			$('#transcript').html(data.text);
		}
		,error: function() {
			$('#transcript').html('No transcript available');
		}		
	});
	//var request = createCORSRequest("GET", "https://s3-us-west-1.amazonaws.com/teamvlogfiles/down_file.txt");

/*	$.get("https://s3-us-west-1.amazonaws.com/teamvlogfiles/down_file.txt",
		 function(data){
			$('#transcript').html(data);
		}
	);*/
}
