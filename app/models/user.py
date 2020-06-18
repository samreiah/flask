from app.database import db
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

class User(db.Model):
   __tablename__ = 'users'
   id = db.Column('id', db.Integer, primary_key = True)
   ssnid = db.Column( db.Integer,  unique=True, nullable=False)
   customerid = db.Column(db.Integer,  unique=True, nullable=False)
   password = db.Column(db.String(255), nullable=False)
   name = db.Column(db.String(100))
   addrln1 = db.Column(db.String(200), nullable=True) 
   addrln2 = db.Column(db.String(200), nullable=True) 
   city = db.Column(db.String(50))
   state = db.Column(db.String(50))
   pin = db.Column(db.String(10))
   createdat = db.Column(db.DateTime(timezone=False), nullable=False, default=datetime.now)
   updatedat = db.Column(db.DateTime(timezone=False), nullable=False, default=datetime.now, onupdate=datetime.now)

def __init__(self, ssnid, customerid, name, password, addrln1, addrln2, city, state, pin, createdat,  updatedat):
   self.ssnid = ssnId
   self.customerId = customerId
   self.name = name
   self.password = password
   self.addrln1 = addrLn1
   self.addrln2 = addrLn2
   self.city = city
   self.state = state
   self.pin = pin
   self.createdat = createdAt
   self.updatedat = updatedAt

def full_name(self):
   return '%s %s' % (self.first_name, self.last_name)

