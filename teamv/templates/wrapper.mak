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

        <!-- JQuery -->
        <script type="text/javascript" src="/static/javascript/jquery.min.js"></script>
        <!-- SocketIO Library -->
        <script type="text/javascript" src="/static/javascript/socket.io.min.js"></script>
        <link rel="stylesheet" href="/static/css/main_styles.css" rel="stylesheet">

        <!-- Bootstrap core CSS -->
        <link href="/static/css/bootstrap.min.css" rel="stylesheet">

        <!-- Custom styles for this template -->
        <link href="/static/css/signin.css" rel="stylesheet">

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
