from app.database import db

class Role(db.Model):
   __tablename__ = 'roles'
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100), nullable=False)
   keyword = db.Column(db.String(50), nullable=False)

def __init__(self, name, keyword):
   self.name = name
   self.keyword = keyword

def __repr__(self):
        return '<Role %r>' % self.name