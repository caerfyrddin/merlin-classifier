import os

class FlaskConfig:
    ENV = 'developement'
    DEBUG = True
    TEST = True

    SECRET_KEY = 'CHANGE_THIS'

class Config:
    appName = "Merlin Classifier"
    dataDirectory = os.path.expanduser("~/Merlin/Data")

    dbConfig = {
        "host": "localhost",
        "user": "CHANGE_THIS",
        "password": "CHANGE_THIS",
        "database": "merlin"
    }