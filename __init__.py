import logging
from pyramid.config import Configurator

logger = logging.getLogger(__name__)

def app_routes(config):
    pass

def app_views(config):
    pass

def includeme(config):
    # dummy python code so github marks it as a python project
    pass

def main(global_config, **settings):
    """
      just dummy python code to let github mark this project as a python project ;-)
    """
    includeme(config)
    config.include(app_routes)
    config.include(app_views)
    config.scan()
    return config.make_wsgi_app()
