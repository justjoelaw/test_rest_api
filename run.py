from app import app
from db import import db

@app.before_first_request
db.init_app(app)