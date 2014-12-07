#!/usr/bin/env python

import os
from flask import Flask
from flask import send_file
from werkzeug import SharedDataMiddleware
from flask.ext.restful import Api
from rest_api import *

app = Flask(__name__)
api = Api(app)
api.add_resource(Reddit, '/api/reddit')
api.add_resource(Hackernews, '/api/hackernews')
api.add_resource(Bloomberg, '/api/bloomberg')

#Serve static files from '/'
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
	'/': os.path.join(os.path.dirname(__file__), '')
})

@app.route("/")
def index():
    return send_file('templates/index.html', cache_timeout=0)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

