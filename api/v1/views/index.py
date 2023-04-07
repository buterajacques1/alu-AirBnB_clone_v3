#!/usr/bin/python3
"""
This module defines a route that returns the status of the API
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})
