# api/v1/views/index.py

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def api_status():
    """Return the status of the API"""
    return jsonify(status="OK")
