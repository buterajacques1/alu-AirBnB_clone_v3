# api/v1/app.py

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close_db(error):
    """Close the database"""
    storage.close()


if __name__ == "__main__":
    from os import environ
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
