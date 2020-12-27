#imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

#variables
db_user = 'dbsuser'
db_pw = 'dbspw'
db_server = 'localhost'
db_port = '5432'
db_name = 'dbsdb'
db_path = 'postgres://{}:{}@{}:{}/{}'.format(db_user,db_pw,db_server,db_port,db_name)
db = SQLAlchemy()

#setup_db(app)
def setup_db(app, database_path=db_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#Publisher class
class Publisher(db.Model):
    __tablename__ = 'publishers'
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    fname = Column(String)
    lname = Column(String)

    def __init__(self, email, fname, lname):
        self.email = email
        self.fname = fname
        self.lname = lname

