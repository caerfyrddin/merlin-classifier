import os

class FlaskConfig:
    ENV = 'developement'
    DEBUG = True
    TEST = True

    SECRET_KEY = 'oiaunf9eciojmwff90u0e'

class Config:
    appName = "Merlin Classifier"
    dataDirectory = os.path.expanduser("~/Merlin/Data")