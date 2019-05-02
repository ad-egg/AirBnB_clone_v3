#!/usr/bin/python3
"""DOCSTRING FOR MODULE"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def ret_json_obj():
    """route on app_views object that returns a JSON"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def no_cls_objs():
    """endpoint that retrieves the number of each objects by type"""
    no_objs_d = {}
    for class in storage.classes.keys():
        no_objs_d[class] = storage.count(class)
    return jsonify(no_objs_d)
