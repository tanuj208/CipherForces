from . import db 

class Algorithm(db.Model):
    # __tablename__ = "algorithm"
    # __table_args__ = {'extend_existing': True} 
    
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))
    # type = db.Column(db.String(50))
    # description = db.Column(db.String(100))
    # challenge = db.Column(db.String(100))
    # hint = db.Column(db.String(100))
    # solution = db.Column(db.String(100))
    # attempts = db.Column(db.Integer)
    # success = db.Column(db.Integer)
    # level = db.Column(db.Integer)
    __tablename__ = "algorithm"
    __table_args__ = {'extend_existing': True} 
    
    length = 5000
    s_len = 100
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(s_len))
    type = db.Column(db.String(s_len))
    description = db.Column(db.String(length))
    challenge = db.Column(db.String(length))
    hint = db.Column(db.String(length))
    solution = db.Column(db.String(length))
    attempts = db.Column(db.Integer)
    success = db.Column(db.Integer)	
    level = db.Column(db.String(s_len))
    allow_encrypt = db.Column(db.String(10))
    allow_decrypt = db.Column(db.String(10))