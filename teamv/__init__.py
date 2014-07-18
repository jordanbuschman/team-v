from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('transcript', '/logs/{meeting}')
    config.add_route('start_meeting', '/start/{meeting}')
    config.add_route('end_meeting', '/end/{meeting}')
    config.add_route('socketio', 'socket.io/*remaining')
    config.scan()

    return config.make_wsgi_app()
