import os
import json
from flask import Flask

g_config_file = 'config/config.json'
g_resources_dir = 'resources'

class App:
    instance = None
    
    @staticmethod
    def init(flask: Flask):
        if App.instance is not None:
            raise RuntimeError('App has already been initialized.')

        App.instance = App()

        App.instance.root = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

        config_path = os.path.join(App.instance.root, g_config_file)

        try:
            with open(config_path, encoding = 'utf8') as config_file:
                config = json.load(config_file)

                App.instance.name = config['name']
        except EnvironmentError as exc:
            raise RuntimeError('Missing config file') from exc
        except KeyError as exc:
            raise RuntimeError('Invalid config file') from exc

        App.instance.flask = flask