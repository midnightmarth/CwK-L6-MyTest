import flask
app = flask.Flask(__name__)

wsgi_app = app.wsgi_app #This line retrieves the WSGI (Web Server Gateway Interface) application from the Flask application instance. This is typically used when deploying the Flask application with a WSGI server such as Gunicorn or uWSGI

@app.route('/')
def hello(): # This is our default route
    return flask.render_template('index.html')



if __name__ == '__main__' :
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT= int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)