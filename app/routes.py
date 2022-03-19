from app import App
from app.models.photo import Photo

flask = App.instance.flask

G_HTTP_NO_CONTENT = 204

@flask.route('/dispatch')
def wakeup():
    App.instance.dispatcher.run()

    return ('', G_HTTP_NO_CONTENT)