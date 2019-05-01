#!/usr/bin/python3
""" Flask app """

from models import storage
from api.v1.views import app_views
from flask import Flask
app = Flask(__name__)

# TODO:
# +Register the blueprint app_views to your Flask instance app
# +Declare a method to handle `@app.teardown_appcontext`
#  that calls storage.close()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True)
