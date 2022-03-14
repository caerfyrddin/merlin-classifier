import os
import json
from flask import Flask

from config.config import Config, FlaskConfig

g_config_file = 'config/config.py'
g_required_config = {
    'appName': str,
    'dataDirectory': str,
    'flaskConfig': FlaskConfig
}

class App:
    instance = None

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

        App.instance = App()
        App.instance.root = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        App.instance.config = config
        App.instance.validateConfig()
        App.instance.flask = flask
        App.instance.flask.config.from_object(App.instance.config.flaskConfig)

    @staticmethod
    def run():
        App.instance.flask.run()