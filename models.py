#imports
from sqlalchemy import Column, String, Integer, create_engine, Boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dbsuser:dbspw@localhost:5432/dbsdb'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    return db

#Publisher class
class Publisher(db.Model):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    fname = Column(String)
    lname = Column(String)
    privilege = Column(String)
    gender = Column(String)
    pioneer = Column(Boolean)

    def __init__(self, email, fname, lname, gender, privilege, pioneer):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.privilege = privilege,
        self.pioneer = pioneer

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def patch(self):
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email,
            'gender': self.gender,
            'privilege': self.privilege,
            'pioneer': self.pioneer
        }
        
