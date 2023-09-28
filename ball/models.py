from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Animal(db.Model):
    __tablename__ =  'animals' 
    
    id = db.Column(db.Integer, primary_key = True) 
    submitter = db.Column(db.String(100)) 
    animal = db.Column(db.Text) 
