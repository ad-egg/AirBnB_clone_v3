#!/usr/bin/python3
""" TODO """
from api.v1.views import app_views
from flask import jsonify
from models import storage as st


# @app_views.route('/status', methods=['GET'], strict_slashes=False)
@app_views.route('/status')
def status_json_return():
    ''' Returns a JSON file with "status": "OK" '''
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_class_count():
    ''' TODO '''
    return jsonify({key: st.count(cls) for key, cls in st.classes.items()})
