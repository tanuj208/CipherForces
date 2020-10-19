from . import db 

class Algorithm(db.Model):
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