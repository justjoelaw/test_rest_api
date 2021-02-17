from app import app
from db import db

@app.before_first_request
db.init_app(app)