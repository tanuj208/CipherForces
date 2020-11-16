from . import db 

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