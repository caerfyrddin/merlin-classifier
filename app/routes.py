from app import App

flask = App.instance.flask

@flask.route('/')
def index():
    return 'Hello world'
