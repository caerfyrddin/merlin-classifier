import logging
import os
import traceback
from flask import Flask
from app.dispatcher import Dispatcher

from config.config import Config, FlaskConfig

g_config_file = 'config/config.py'
g_required_config = {
    'appName': str,
    'dataDirectory': str,
    'flaskConfig': FlaskConfig
}

logging.basicConfig(level = logging.WARNING)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class App:
    instance = None

    test = 0

    def validateConfig(self) -> bool:
        for key in g_required_config:
            if not hasattr(self.config, key):
                raise RuntimeError('Missing config key "' + key + '"') \
                    from RuntimeError('Invalid config file')
            if not type(getattr(self.config, key)) is g_required_config[key]:
                raise RuntimeError('Invalid "' + key + '" value type') \
                    from RuntimeError('Invalid config file')
        return True
    
    @staticmethod
    def init(config: Config, flask: Flask):
        if App.instance is not None:
            raise RuntimeError('App has already been initialized.')

        log.debug('Initializing app')

        App.instance = App()
        App.instance.root = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        App.instance.config = config
        App.instance.validateConfig()
        
        log.debug('Initializing Flask')

        App.instance.flask = flask
        from app import routes

        App.instance.flask.config.from_object(App.instance.config.flaskConfig)

        App.instance.dispatcher = Dispatcher()

    @staticmethod
    def run():
        log.debug('Running app')

        App.instance.flask.run()