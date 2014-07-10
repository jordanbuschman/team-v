<!DOCTYPE html>

<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            % if title is not UNDEFINED:
                ${title}
            % else:
                Team Valente
            % endif
        </title>

        <script type="text/javascript" src="/static/javascript/jquery.min.js"></script>
        <script type="text/javascript" src="/static/javascript/socket.io.min.js"></script>
        <script type="text/javascript" src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="/static/css/main_styles.css" rel="stylesheet">

        <%block name="includes" />

    </head>
    <body>
        <section class="wrapper-content">
            <div class="container">
                ${next.body()}
            </div class="container">
        </section>
    </body>
</html>
