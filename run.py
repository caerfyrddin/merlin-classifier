from app import App
from flask import Flask
from config.config import Config

App().init(Config(), Flask(__name__))

if __name__ == '__main__':
    App().run()