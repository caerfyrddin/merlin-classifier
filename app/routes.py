from app import App
from app.models.photo import Photo

flask = App.instance.flask

G_HTTP_NO_CONTENT = 204

@flask.route('/dispatch')
def wakeup():
    App.instance.dispatcher.run()

    return ('', G_HTTP_NO_CONTENT)

@flask.route('/testdb')
def testdb():
    pending = Photo.db_fetch_pending()

    for item in pending:
        print(item)

    return ('', G_HTTP_NO_CONTENT)