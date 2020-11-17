from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import json
from flask import request
from flask_cors import CORS

db = SQLAlchemy()

class Algorithm(db.Model):
    __tablename__ = "algorithm"
    __table_args__ = {'extend_existing': True} 
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    description = db.Column(db.String(100))
    challenge = db.Column(db.String(100))
    hint = db.Column(db.String(100))
    solution = db.Column(db.String(100))
    attempts = db.Column(db.Integer)
    success = db.Column(db.Integer)	
    level = db.Column(db.Integer)
    allow_encrypt = db.Column(db.String(10))
    allow_decrypt = db.Column(db.String(10))

    def __init__(self, id, name, type, description, challenge, hint, solution, attempts, success, level, allow_encrypt, allow_decrypt):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.challenge = challenge	
        self.hint = hint
        self.solution = solution
        self.attempts = attempts
        self.success = success
        self.level = level
        self.allow_decrypt = allow_decrypt
        self.allow_encrypt = allow_encrypt


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    return app

app = create_app()
CORS(app)