#!/usr/bin/python3
'''
Starts a threaded lask web application listening on 0.0.0.0, port 5000
'''

from models import storage
from api.v1.views import app_views
from flask import Flask
app = Flask(__name__)

# TODO:
# +Register the blueprint app_views to your Flask instance app
# +Declare a method to handle `@app.teardown_appcontext`
#  that calls storage.close()

@app.teardown_appcontext
def teardown_storage():
    '''
    Closes or otherwise deallocates the storage instance if it exists.
    '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
