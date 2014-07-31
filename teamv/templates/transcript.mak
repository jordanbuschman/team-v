<%inherit file="wrapper.mak" />

<h2>Transcript of Meeting #${meeting}</h2>
<hr />

<div id="status">
</div>
<pre id="log-file">
% if is_local:
<%include file="logs/log_${meeting}.log" />
% endif
</pre>

<hr />

% if not is_local:
<script type="text/javascript">
    $(document).ready(function() {
        $.post("/auth", { meeting: ${meeting} })
            .done(function(response) {
                $.ajax({
                    url: "https://teamvlogfiles.s3.amazonaws.com/log_${meeting}.log",
                    data: {'Authorization': response.auth},
                    type: "GET",
                    success: function(data) {
                        $("#log-file").html(data);
                        $("#status").html("<p>This meeting is over.</p>");
                    }
                });
        });
    });
</script>
% endif
