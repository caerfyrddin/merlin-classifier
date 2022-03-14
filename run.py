from src.app import App
from flask import Flask, request

App().init(Flask(__name__))

if __name__ == '__main__':
    App().run()