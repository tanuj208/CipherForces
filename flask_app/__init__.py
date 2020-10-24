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
    plaintext = db.Column(db.String(100))
    ciphertext = db.Column(db.String(100))
    attempts = db.Column(db.Integer)
    success = db.Column(db.Integer)	

    def __init__(self, id, name, type, description, challenge, hint, plaintext, ciphertext, attempts, success):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.challenge = challenge
        self.hint = hint
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.attempts = attempts
        self.success = success


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    return app

app = create_app()
CORS(app)

@app.route('/')
def Get_Data():
    data = Algorithm.query.all()
    all_rows = [{'id' : row.id, 'name' : row.name, 'type' : row.type, 'description' : row.description, 'challenge' : row.challenge, 'hint' : row.hint, 'plaintext' : row.plaintext, 'ciphertext' : row.ciphertext, 'attempts' : row.attempts, 'success' : row.success} for row in data]
    return (json.dumps(all_rows))
