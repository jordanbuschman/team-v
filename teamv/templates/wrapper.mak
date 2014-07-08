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
        <script type="text/javascript" src="/static/javascript/index.js"></script>

        <link href="/static/css/mystyles.css" rel="stylesheet" type="text/css">

    </head>
    <body>
        <section class="wrapper-content">
            ${next.body()}
        </section>
    </body>
</html>
