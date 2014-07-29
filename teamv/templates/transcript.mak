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
    $(document).ready(function() {
        var url = "https://s3-us-west-1.amazonaws.com/teamvlogfiles/log_${meeting}.log";
        $.post("/auth", { meeting: ${meeting} })
            .done(function(response) {
                $.ajax({
                    url: "https://teamvlogfiles.s3.amazonaws.com/log_${meeting}.log",
                    data: {'Authorization': response.auth},
                    type: "GET",
                    success: function(data) {
                        alert(data);
                    }
                });
        });
    });
</script>
% endif
