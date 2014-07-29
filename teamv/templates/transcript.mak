<%inherit file="wrapper.mak" />

<h2>Transcript of Meeting #${meeting}</h2>
<hr />

<pre id="log-file">
% if is_local:
<%include file="logs/log_${meeting}.log" />
% endif
</pre>

<hr />

% if not is_local:
<script type="text/javascript">
    function createCORSRequest(method, url) {
        var xhr = new XMLHttpRequest();
        if ("withCredentials" in xhr) {
            xhr.open(method, url, true);
        } else if (typeof XDomainRequest != "undefined") {
            xhr = new XDomainRequest();
            xhr.open(method, url);
        } else {
            xhr = null;
        }
        return xhr;
    }

    $(document).ready(function() {
        var url = "https://s3-us-west-1.amazonaws.com/teamvlogfiles/log_${meeting}.log";
        var request = createCORSRequest("get", url);
        request.withCredentials = true;
        request.setRequestHeader('Access-Control-Allow-Credentials', 'http://localhost:5000/logs/${meeting}');
        if (request) {
            request.onload = function() {
                $('#log-file').html(request.responseText);
            };
            request.send();
        }
    });
</script>
% endif
