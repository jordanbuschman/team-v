function makeHttpObject() {
  try {return new XMLHttpRequest();}
  catch (error) {}
  try {return new ActiveXObject("Msxml2.XMLHTTP");}
  catch (error) {}
  try {return new ActiveXObject("Microsoft.XMLHTTP");}
  catch (error) {}

  throw new Error("Could not create HTTP request object.");
}


function getPolicySign() {
    $.get("/sign", function(data) {
	var policy = data.policy;
	var signature = data.signature;
	var access_key = data.key;

	var f = document.createElement("form");
	f.setAttribute('method', "get");
	f.setAttribute('action', "http://teamvlogfiles.s3.amazonaws.com/");
	var acl = document.createElement("input");
	acl.setAttribute('type', "hidden");
	acl.setAttribute('value',"public-read");
	acl.setAttribute('name', "acl");
	//var sar = document.createElement("input");
	//sar.setAttribute('name', "success_action_request");
	//sar.setAttribute('type', "hidden");
	var key = document.createElement("input");
	key.setAttribute('type', "hidden");
	key.setAttribute('name', "AccessKeyId");
	key.setAttribute('value', access_key);
	

    });
}




