import os
from . import create_app # from __init__ file
from flask_cors import CORS
app = create_app()

CORS(app)

from .users import routes
from .dashboards import routes
from .tickets import routes

if __name__ == "__main__":
    app.run()
